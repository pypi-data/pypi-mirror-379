import cv2
import math
import random
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from PIL import ImageFont, ImageDraw, Image
import os
import time
import importlib.resources as pkg_resources
import XMWAI.assets  # 引入资源目录


# ---------- 工具函数：从 assets 读取资源 ----------
def get_asset_path(filename: str) -> str:
    """
    获取包内资源的绝对路径 (兼容 pip 安装后的情况)
    """
    with pkg_resources.path(XMWAI.assets, filename) as p:
        return str(p)


class SnakeGame:
    def __init__(self, width=720, height=720, snakeInitLength=150, snakeGrowth=50,
                 snakeLineWidth=10, snakeHeadSize=15, foodPaths=None, foodNames=None, foodScores=None,
                 obstaclePaths=None, fontPath=None):

        self.resolution = (width, height)
        self.snakeInitLength = snakeInitLength
        self._snakeGrowth = snakeGrowth
        self._snakeHeadSize = snakeHeadSize
        self._foodScores = foodScores if foodScores is not None else [3, 2, 1]
        self.snakeLineWidth = snakeLineWidth

        # 默认资源路径
        if foodPaths is None:
            foodPaths = [get_asset_path("h.png"),
                         get_asset_path("s.png"),
                         get_asset_path("t.png")]
        if foodNames is None:
            foodNames = ["汉堡", "薯条", "甜甜圈"]
        if obstaclePaths is None:
            obstaclePaths = [get_asset_path("g.png"),
                             get_asset_path("l.png"),
                             get_asset_path("m.png")]
        if fontPath is None:
            fontPath = get_asset_path("微软雅黑.ttf")

        self.foodPaths = foodPaths
        self.foodNames = foodNames
        self.obstaclePaths = obstaclePaths
        self.fontPath = fontPath

        self.cap = None
        self.detector = None
        self.snake = None
        self.foodManager = None
        self.obstacleManager = None
        self.img = None
        self.overlayTexts = []

        self.timer = 30
        self.start_time = None

        self._init_game_objects()
        self.open_window()

    # ----------- 属性自动同步 -----------
    @property
    def snakeHeadSize(self):
        return self._snakeHeadSize

    @snakeHeadSize.setter
    def snakeHeadSize(self, value):
        self._snakeHeadSize = value
        if self.snake:
            self.snake.headSize = value

    @property
    def foodScores(self):
        return self._foodScores

    @foodScores.setter
    def foodScores(self, scores):
        self._foodScores = scores
        if self.foodManager:
            self.foodManager.foodScores = scores

    @property
    def snakeGrowth(self):
        return self._snakeGrowth

    @snakeGrowth.setter
    def snakeGrowth(self, value):
        self._snakeGrowth = value

    # ---------------- 工具函数 ----------------
    def _putChineseText(self, img, text, pos, fontSize=40, color=(0, 0, 255)):
        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        try:
            font = ImageFont.truetype(self.fontPath, fontSize)
        except OSError:
            font = ImageFont.load_default()
        draw.text(pos, text, font=font, fill=color)
        return np.array(img_pil)

    def _init_game_objects(self):
        self.snake = self.Snake(color=(0, 0, 255), initLength=self.snakeInitLength,
                                lineWidth=self.snakeLineWidth, headSize=self._snakeHeadSize)
        self.foodManager = self.FoodManager(
            self.foodPaths, self.foodNames, self._foodScores)
        self.obstacleManager = self.ObstacleManager(self.obstaclePaths)
        self.obstacleManager.randomObstacles()

    def _render_frame(self, show_food=True, show_obstacle=True):
        success, self.img = self.cap.read()
        if not success:
            return
        self.img = cv2.flip(self.img, 1)
        hands, self.img = self.detector.findHands(self.img, flipType=False)
        player_head = tuple(hands[0]['lmList'][8][0:2]) if hands else None

        if not self.snake.gameOver and player_head:
            self.snake.update(self.img, player_head, self.obstacleManager)

        if not self.snake.gameOver and player_head and show_food:
            cx, cy = player_head
            rx, ry = self.foodManager.foodPoint
            w, h = self.foodManager.wFood, self.foodManager.hFood
            if rx - w//2 <= cx <= rx + w//2 and ry - h//2 <= cy <= ry + h//2:
                self.snake.score += self.foodManager.foodScores[self.foodManager.foodIndex]
                self.snake.allowedLength += self._snakeGrowth
                self.foodManager.randomFoodLocation(self.obstacleManager)

        if show_obstacle:
            self.img = self.obstacleManager.draw(self.img)
            self.obstacleManager.moveObstacles(
                self.resolution[0], self.resolution[1])

        if show_food:
            self.img = self.foodManager.draw(self.img)

    # ---------------- 对外接口 ----------------
    def open_window(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.resolution[0])
        self.cap.set(4, self.resolution[1])
        self.detector = HandDetector(detectionCon=0.7, maxHands=1)
        success, self.img = self.cap.read()
        if not success:
            print("摄像头打开失败")
            return
        self.img = cv2.flip(self.img, 1)
        cv2.imshow("AI Snake", self.img)
        cv2.waitKey(1)

    def hand(self):
        if self.cap is None:
            print("请先调用 open_window()")
            return
        if self.detector is None:
            self.detector = HandDetector(detectionCon=0.8, maxHands=1)
        while True:
            success, self.img = self.cap.read()
            if not success:
                break
            self.img = cv2.flip(self.img, 1)
            hands, self.img = self.detector.findHands(self.img, flipType=False)
            cv2.imshow("AI Snake", self.img)
            key = cv2.waitKey(1) & 0xFF
            if hands or key == ord('q'):
                break

    def display(self):
        if self.img is None:
            self._render_frame(show_food=False)
        self.foodManager.randomFoodLocation(self.obstacleManager)
        self._render_frame(show_food=True)
        self.overlayTexts = [
            (f'玩家分数：{self.snake.score}', (50, 50), 30, (255, 0, 255)),
            (f'倒计时：{self.timer} 秒', (50, 120), 30, (255, 0, 255))
        ]
        img_copy = self.img.copy()
        for txt, pos, size, color in self.overlayTexts:
            img_copy = self._putChineseText(img_copy, txt, pos, size, color)
        cv2.imshow("AI Snake", img_copy)
        cv2.waitKey(1)

    # ---------------- 重置游戏 ----------------
    def reset_game(self):
        self.snake.reset()
        self.snake.headSize = self._snakeHeadSize
        self.obstacleManager.randomObstacles()
        self.foodManager.foodScores = self._foodScores
        self.foodManager.randomFoodLocation(self.obstacleManager)
        self.start_time = time.time()
        self.timer = 30
        if self.cap is None or not self.cap.isOpened():
            self.open_window()

    # ---------------- 游戏结束 ----------------
    def gameover(self, path=None, size=(100, 100)):
        if path is None:
            path = get_asset_path("1.png")

        if os.path.exists(path):
            gameover_img = cv2.imread(path)
            gameover_img = cv2.resize(gameover_img, self.resolution)
        else:
            gameover_img = np.zeros(
                (self.resolution[1], self.resolution[0], 3), np.uint8)
            cv2.putText(gameover_img, "Game Over Image Missing!", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        gameover_img = self._putChineseText(
            gameover_img, f"最终分数：{self.snake.score}", size, 40, (68, 84, 106))

        while True:
            cv2.imshow("AI Snake", gameover_img)
            key = cv2.waitKey(0) & 0xFF
            if key == ord('r'):  # 重启游戏
                self.reset_game()
                self.start()
                break
            elif key == ord('q'):  # 退出游戏
                if self.cap is not None:
                    self.cap.release()
                cv2.destroyAllWindows()
                break

    # ---------------- 游戏主循环 ----------------
    def start(self):
        if self.cap is None or not self.cap.isOpened():
            self.open_window()
        self.start_time = time.time()
        self.timer = 30

        while True:
            if self.snake.gameOver or self.timer == 0:
                # 游戏结束，进入 gameover 界面
                self.gameover()
                break

            self._render_frame(show_food=True, show_obstacle=True)
            elapsed = int(time.time() - self.start_time)
            self.timer = max(0, 30 - elapsed)

            self.overlayTexts = [
                (f'玩家分数：{self.snake.score}', (50, 50), 30, (255, 0, 255)),
                (f'倒计时：{self.timer} 秒', (50, 120), 30, (255, 0, 255))
            ]

            if self.img is not None:
                img_copy = self.img.copy()
                for txt, pos, size, color in self.overlayTexts:
                    img_copy = self._putChineseText(
                        img_copy, txt, pos, size, color)
                cv2.imshow("AI Snake", img_copy)

            key = cv2.waitKey(1)
            if key == ord('r'):  # 游戏中途重置
                self.reset_game()
            elif key == ord('q'):
                if self.cap is not None:
                    self.cap.release()
                cv2.destroyAllWindows()
                break

    # ---------------- 内部类：蛇 ----------------
    class Snake:
        def __init__(self, color, initLength=150, lineWidth=10, headSize=15):
            self.points = []
            self.currentLength = 0
            self.allowedLength = initLength
            self.previousHead = None
            self.score = 0
            self.color = color
            self.gameOver = False
            self.lineWidth = lineWidth
            self.headSize = headSize

        def reset(self):
            self.points = []
            self.currentLength = 0
            self.allowedLength = 150
            self.previousHead = None
            self.score = 0
            self.gameOver = False

        def update(self, imgMain, currentHead, obstacleManager=None):
            if self.gameOver:
                return
            cx, cy = currentHead
            if cx is None or cy is None:
                return
            if self.previousHead is None:
                self.previousHead = (cx, cy)
            px, py = self.previousHead

            alpha = 0.7
            cx = int(px * (1 - alpha) + cx * alpha)
            cy = int(py * (1 - alpha) + cy * alpha)

            maxStep = 50
            dx = cx - px
            dy = cy - py
            distance = math.hypot(dx, dy)
            if distance > maxStep:
                steps = int(distance / maxStep)
                for i in range(1, steps + 1):
                    ix = int(px + dx * i / steps)
                    iy = int(py + dy * i / steps)
                    self.points.append((ix, iy))
                    self.currentLength += maxStep
            else:
                self.points.append((cx, cy))
                self.currentLength += distance

            self.previousHead = (cx, cy)

            while self.currentLength > self.allowedLength:
                if len(self.points) > 1:
                    removed_dx = self.points[1][0] - self.points[0][0]
                    removed_dy = self.points[1][1] - self.points[0][1]
                    removed_dist = math.hypot(removed_dx, removed_dy)
                    self.currentLength -= removed_dist
                self.points.pop(0)

            for i in range(1, len(self.points)):
                cv2.line(
                    imgMain, self.points[i-1], self.points[i], self.color, self.lineWidth)

            snakeHeadColor = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
            cv2.circle(imgMain, (cx, cy), self.headSize,
                       snakeHeadColor, cv2.FILLED)

            h, w, _ = imgMain.shape
            margin = 5
            if cx <= margin or cx >= w - margin or cy <= margin or cy >= h - margin:
                self.gameOver = True

            if obstacleManager:
                for ox, oy, ow, oh, *_ in obstacleManager.obstacles:
                    if ox <= cx <= ox + ow and oy <= cy <= oy + oh:
                        self.gameOver = True

    # ---------------- 内部类：食物 ----------------
    class FoodManager:
        def __init__(self, foodPaths, foodNames, foodScores):
            self.foodImages = []
            for path in foodPaths:
                if os.path.exists(path):
                    self.foodImages.append(
                        cv2.imread(path, cv2.IMREAD_UNCHANGED))
                else:
                    self.foodImages.append(np.zeros((50, 50, 4), np.uint8))
            self.foodNames = foodNames
            self.foodScores = foodScores
            self.foodIndex = 0
            self.hFood, self.wFood = 0, 0
            self.foodPoint = 0, 0
            self.randomFoodLocation()

        def randomFoodLocation(self, obstacleManager=None):
            max_attempts = 100
            for _ in range(max_attempts):
                self.foodPoint = random.randint(
                    50, 1230), random.randint(50, 670)
                self.foodIndex = random.randint(0, len(self.foodImages)-1)
                self.hFood, self.wFood, _ = self.foodImages[self.foodIndex].shape
                if obstacleManager:
                    overlap = False
                    for ox, oy, ow, oh, *_ in obstacleManager.obstacles:
                        if ox < self.foodPoint[0] < ox + ow and oy < self.foodPoint[1] < oy + oh:
                            overlap = True
                            break
                    if not overlap:
                        return
            return

        def draw(self, imgMain):
            rx, ry = self.foodPoint
            imgMain = cvzone.overlayPNG(imgMain, self.foodImages[self.foodIndex],
                                        (rx - self.wFood//2, ry - self.hFood//2))
            return imgMain

    # ---------------- 内部类：障碍 ----------------
    class ObstacleManager:
        def __init__(self, obstaclePaths):
            self.obstacleImages = []
            for path in obstaclePaths:
                if os.path.exists(path):
                    self.obstacleImages.append(
                        cv2.imread(path, cv2.IMREAD_UNCHANGED))
                else:
                    self.obstacleImages.append(np.zeros((50, 50, 4), np.uint8))
            self.obstacles = []

        def randomObstacles(self):
            self.obstacles.clear()
            for img in self.obstacleImages:
                h, w, _ = img.shape
                x = random.randint(150, 1230)
                y = random.randint(50, 670)
                dx = random.choice([-5, 5])
                dy = random.choice([-5, 5])
                self.obstacles.append([x, y, w, h, dx, dy, img])

        def moveObstacles(self, wMax, hMax):
            for obs in self.obstacles:
                x, y, ow, oh, dx, dy, img = obs
                x += dx
                y += dy
                if x <= 0 or x + ow >= wMax:
                    dx *= -1
                if y <= 0 or y + oh >= hMax:
                    dy *= -1
                obs[0], obs[1], obs[4], obs[5] = x, y, dx, dy

        def draw(self, imgMain):
            for obs in self.obstacles:
                x, y, w, h, dx, dy, img = obs
                imgMain = cvzone.overlayPNG(imgMain, img, (int(x), int(y)))
            return imgMain
