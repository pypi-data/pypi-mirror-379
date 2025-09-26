# -*- coding: utf-8 -*-
"""
snake_core.py
标准版 SnakeGame（摄像头 + 手势控制）
与 main.py 配合使用：ai = XMWAI.SnakeGame(...); ai.hand(); ai.display(); ai.start(); ai.gameover(...)
"""

import os
import time
import math
import random

import cv2
import numpy as np
import cvzone
from cvzone.HandTrackingModule import HandDetector
from PIL import Image, ImageDraw, ImageFont

# ------------- 资源路径（包内 assets 目录） -------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")


def _safe_read_image(path, default_shape=(50, 50, 4)):
    """
    读取 PNG（带 alpha）或返回空透明图像（避免 None 导致 shape 失败）
    """
    if path and os.path.exists(path):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if img is None:
            return np.zeros(default_shape, dtype=np.uint8)
        return img
    else:
        return np.zeros(default_shape, dtype=np.uint8)


class SnakeGame:
    def __init__(self, width=720, height=720, snakeInitLength=150, snakeGrowth=50,
                 snakeLineWidth=10, snakeHeadSize=15, foodPaths=None, foodNames=None, foodScores=None,
                 obstaclePaths=None, fontPath=None):
        """
        初始化游戏参数并加载资源（图片、字体）
        参数尽量与 main.py 调用保持一致
        """
        # 基本参数
        # 宽, 高（cv2.set 采用 3 -> width, 4 -> height）
        self.resolution = (width, height)
        self.snakeInitLength = snakeInitLength
        self._snakeGrowth = snakeGrowth
        self._snakeHeadSize = snakeHeadSize
        self.snakeLineWidth = snakeLineWidth
        self._foodScores = foodScores if foodScores is not None else [3, 2, 1]

        # 资源默认路径（包内 assets）
        if fontPath is None:
            fontPath = os.path.join(ASSETS_DIR, "微软雅黑.ttf")
        if foodPaths is None:
            foodPaths = [
                os.path.join(ASSETS_DIR, "h.png"),
                os.path.join(ASSETS_DIR, "s.png"),
                os.path.join(ASSETS_DIR, "t.png")
            ]
        if foodNames is None:
            foodNames = ["汉堡", "薯条", "甜甜圈"]
        if obstaclePaths is None:
            obstaclePaths = [
                os.path.join(ASSETS_DIR, "g.png"),
                os.path.join(ASSETS_DIR, "l.png"),
                os.path.join(ASSETS_DIR, "m.png")
            ]

        # 赋值
        self.fontPath = fontPath
        self.foodPaths = foodPaths
        self.foodNames = foodNames
        self.obstaclePaths = obstaclePaths

        # 摄像头 / 手势检测等对象
        self.cap = None
        self.detector = None
        self.img = None

        # 游戏对象（稍后初始化）
        self.snake = None
        self.foodManager = None
        self.obstacleManager = None

        # 覆盖文字（画面左上）
        self.overlayTexts = []

        # 计时器
        self.timer = 30
        self.start_time = None

        # 加载并初始化内部游戏对象
        self._init_game_objects()

        # 注意：不在 init 中自动打开摄像头（让用户在 main 中调用 open_window 或 hand/start）
        # 如果你希望自动打开摄像头，请调用 self.open_window()
        # self.open_window()

    # ---------------- 属性同步（方便外部设置） ----------------
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

    # ----------------- 工具：在 OpenCV 图像上写中文 -----------------
    def _putChineseText(self, img, text, pos, fontSize=40, color=(0, 0, 255)):
        """
        在 BGR numpy 图像上绘制中文（使用 PIL）
        pos: (x, y) 左上角
        color: BGR 元组（PIL 需要 RGB，但我们直接使用 BGR 也能显示）
        """
        try:
            img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        except Exception:
            img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        try:
            font = ImageFont.truetype(self.fontPath, fontSize)
        except Exception:
            font = ImageFont.load_default()
        # PIL 的颜色是 RGB
        # 给定的 color 是 BGR（一致化处理）
        b, g, r = color
        draw.text(pos, text, font=font, fill=(r, g, b))
        img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        return img

    # ----------------- 初始化游戏对象 -----------------
    def _init_game_objects(self):
        # 内部类实例化
        self.snake = self.Snake(color=(0, 0, 255), initLength=self.snakeInitLength,
                                lineWidth=self.snakeLineWidth, headSize=self._snakeHeadSize)
        self.foodManager = self.FoodManager(
            self.foodPaths, self.foodNames, self._foodScores)
        self.obstacleManager = self.ObstacleManager(self.obstaclePaths)
        # 随机生成障碍
        self.obstacleManager.randomObstacles()

    # ----------------- 摄像头与窗口控制 -----------------
    def open_window(self):
        """打开摄像头并显示第一帧（如失败会打印错误）"""
        self.cap = cv2.VideoCapture(0)
        # 设置分辨率（注意：cv2.set(3) 对应宽，(4) 对应高）
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
        """
        快速测试手部检测（按 q 或检测到手后退出）
        供用户检查摄像头与手势模块是否正常
        """
        if self.cap is None:
            self.open_window()
        if self.detector is None:
            self.detector = HandDetector(detectionCon=0.8, maxHands=1)

        while True:
            success, img = self.cap.read()
            if not success:
                break
            img = cv2.flip(img, 1)
            hands, img = self.detector.findHands(img, flipType=False)
            cv2.imshow("AI Snake", img)
            key = cv2.waitKey(1) & 0xFF
            if hands or key == ord('q'):
                break

    # ----------------- 渲染与显示 -----------------
    def _render_frame(self, show_food=True, show_obstacle=True):
        """读取摄像头一帧并渲染蛇、食物和障碍（内部使用）"""
        if self.cap is None:
            return
        success, self.img = self.cap.read()
        if not success:
            return
        self.img = cv2.flip(self.img, 1)
        hands, self.img = self.detector.findHands(self.img, flipType=False)
        player_head = tuple(hands[0]['lmList'][8][0:2]) if hands else None

        # 更新蛇的位置
        if not self.snake.gameOver and player_head:
            self.snake.update(self.img, player_head, self.obstacleManager)

        # 检查是否吃到食物
        if not self.snake.gameOver and player_head and show_food:
            cx, cy = player_head
            rx, ry = self.foodManager.foodPoint
            w, h = self.foodManager.wFood, self.foodManager.hFood
            if (rx - w // 2) <= cx <= (rx + w // 2) and (ry - h // 2) <= cy <= (ry + h // 2):
                # 加分并延长蛇的允许长度
                self.snake.score += self.foodManager.foodScores[self.foodManager.foodIndex]
                self.snake.allowedLength += self._snakeGrowth
                # 随机重新放置食物（避免与障碍重叠）
                self.foodManager.randomFoodLocation(self.obstacleManager)

        # 障碍物移动与绘制
        if show_obstacle:
            self.img = self.obstacleManager.draw(self.img)
            self.obstacleManager.moveObstacles(
                self.resolution[0], self.resolution[1])

        # 食物绘制
        if show_food:
            self.img = self.foodManager.draw(self.img)

    def display(self):
        """
        在窗口上绘制分数和倒计时（只是渲染一帧供展示）
        调用者可以在 start() 前调用一次显示初始状态
        """
        if self.img is None:
            # 尝试渲染一帧（不显示食物）
            self._render_frame(show_food=False)
        self.foodManager.randomFoodLocation(self.obstacleManager)
        self._render_frame(show_food=True)

        # 覆盖文字（玩家分数与倒计时）
        self.overlayTexts = [
            (f'玩家分数：{self.snake.score}', (50, 50), 30, (255, 0, 255)),
            (f'倒计时：{self.timer} 秒', (50, 120), 30, (255, 0, 255))
        ]
        img_copy = self.img.copy()
        for txt, pos, size, color in self.overlayTexts:
            img_copy = self._putChineseText(img_copy, txt, pos, size, color)
        cv2.imshow("AI Snake", img_copy)
        cv2.waitKey(1)

    # ----------------- 重置与结束 -----------------
    def reset_game(self):
        """重置游戏到初始状态"""
        self.snake.reset()
        self.snake.headSize = self._snakeHeadSize
        self.obstacleManager.randomObstacles()
        self.foodManager.foodScores = self._foodScores
        self.foodManager.randomFoodLocation(self.obstacleManager)
        self.start_time = time.time()
        self.timer = 30
        if self.cap is None or not self.cap.isOpened():
            self.open_window()

    def gameover(self, path=None, size=(100, 100)):
        """
        显示游戏结束画面并提供 r（重启）或 q（退出）选项
        path: 自定义结束图片路径（相对于包内 assets），默认使用 assets/1.png
        size: 未使用但保留下来以兼容外部调用
        """
        if path is None:
            path = os.path.join(ASSETS_DIR, "1.png")
        else:
            # 若传入相对文件名（如 "1.png"），优先在 assets 中寻找
            if not os.path.isabs(path):
                path = os.path.join(ASSETS_DIR, path)

        if os.path.exists(path):
            gameover_img = cv2.imread(path)
            # 缩放到窗口大小（以覆盖窗口）
            gameover_img = cv2.resize(gameover_img, self.resolution)
        else:
            # 如果没有找到图片，生成一个黑色背景并写提示
            gameover_img = np.zeros(
                (self.resolution[1], self.resolution[0], 3), np.uint8)
            cv2.putText(gameover_img, "Game Over Image Missing!", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        # 在结束画面写最终分数（使用中文绘制）
        gameover_img = self._putChineseText(
            gameover_img, f"最终分数：{self.snake.score}", (50, 200), 40, (68, 84, 106))

        # 等待用户按键：r 重启, q 退出
        while True:
            cv2.imshow("AI Snake", gameover_img)
            key = cv2.waitKey(0) & 0xFF
            if key == ord('r'):
                self.reset_game()
                self.start()
                break
            elif key == ord('q'):
                if self.cap is not None:
                    self.cap.release()
                cv2.destroyAllWindows()
                break

    # ----------------- 游戏主循环 -----------------
    def start(self):
        """游戏主循环（会阻塞直到退出或游戏结束）"""
        if self.cap is None or not getattr(self.cap, "isOpened", lambda: False)():
            self.open_window()
        if self.detector is None:
            self.detector = HandDetector(detectionCon=0.7, maxHands=1)

        self.start_time = time.time()
        self.timer = 30

        while True:
            # 若游戏结束或倒计时结束，进入结束界面
            if self.snake.gameOver or self.timer == 0:
                self.gameover("1.png", (520, 520))
                break

            self._render_frame(show_food=True, show_obstacle=True)

            # 更新倒计时
            elapsed = int(time.time() - self.start_time)
            self.timer = max(0, 30 - elapsed)

            # 覆盖文字显示
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
            elif key == ord('q'):  # 退出
                if self.cap is not None:
                    self.cap.release()
                cv2.destroyAllWindows()
                break

    # ================= 内部类：Snake =================
    class Snake:
        def __init__(self, color, initLength=150, lineWidth=10, headSize=15):
            """
            简洁的蛇实现：维护点列表，根据 allowedLength 保持长度
            color: BGR 颜色
            """
            self.points = []
            self.currentLength = 0.0
            self.allowedLength = initLength
            self.previousHead = None
            self.score = 0
            self.color = color
            self.gameOver = False
            self.lineWidth = lineWidth
            self.headSize = headSize

        def reset(self):
            """重置蛇的状态"""
            self.points = []
            self.currentLength = 0.0
            self.allowedLength = 150
            self.previousHead = None
            self.score = 0
            self.gameOver = False

        def update(self, imgMain, currentHead, obstacleManager=None):
            """
            根据当前手的位置更新蛇（平滑插值 + 限步 + 修剪超长部分）
            currentHead: (x, y)
            """
            if self.gameOver:
                return
            if currentHead is None:
                return

            cx, cy = currentHead
            if self.previousHead is None:
                self.previousHead = (cx, cy)
            px, py = self.previousHead

            # 平滑插值，避免抖动
            alpha = 0.7
            cx = int(px * (1 - alpha) + cx * alpha)
            cy = int(py * (1 - alpha) + cy * alpha)

            # 限制最大步长（避免瞬移导致计算异常）
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

            # 当长度大于允许长度时，从头部开始删除点
            while self.currentLength > self.allowedLength and len(self.points) > 1:
                removed_dx = self.points[1][0] - self.points[0][0]
                removed_dy = self.points[1][1] - self.points[0][1]
                removed_dist = math.hypot(removed_dx, removed_dy)
                self.currentLength -= removed_dist
                self.points.pop(0)

            # 绘制蛇身（线段）
            for i in range(1, len(self.points)):
                cv2.line(
                    imgMain, self.points[i - 1], self.points[i], self.color, self.lineWidth)

            # 绘制蛇头（变色圆）
            snakeHeadColor = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))
            cv2.circle(imgMain, (cx, cy), self.headSize,
                       snakeHeadColor, cv2.FILLED)

            # 窗口边界检测
            h, w = imgMain.shape[:2]
            margin = 5
            if cx <= margin or cx >= w - margin or cy <= margin or cy >= h - margin:
                self.gameOver = True

            # 与障碍物碰撞检测（若存在障碍管理器）
            if obstacleManager is not None:
                for ox, oy, ow, oh, *_ in obstacleManager.obstacles:
                    if ox <= cx <= ox + ow and oy <= cy <= oy + oh:
                        self.gameOver = True

    # ================= 内部类：FoodManager =================
    class FoodManager:
        def __init__(self, foodPaths, foodNames, foodScores):
            """
            foodPaths: list of 图片路径（带 alpha 的 PNG 推荐）
            foodNames: list 名称（可选）
            foodScores: list 对应分数（与 foodPaths 长度一致或可复用）
            """
            self.foodImages = []
            # 读取每个图片（若不存在，则使用透明占位）
            for path in foodPaths:
                img = _safe_read_image(path)
                self.foodImages.append(img)

            self.foodNames = foodNames
            self.foodScores = foodScores if foodScores is not None else [
                3] * len(self.foodImages)
            self.foodIndex = 0
            # 宽高初始化为占位值（读取后更新）
            self.hFood, self.wFood = 50, 50
            self.foodPoint = (100, 100)
            # 初始放置
            self.randomFoodLocation()

        def randomFoodLocation(self, obstacleManager=None):
            """
            随机放置食物位置，避免与障碍重叠（最多尝试 max_attempts 次）
            坐标范围依据典型摄像头分辨率设定，可根据需要调整
            """
            max_attempts = 200
            # 摄像头分辨率默认使用 1280x720 或 self 所在外部被设置的分辨率
            # 这里我们使用一个可信任的范围：x in [50,  self_max_w - 50], y in [50, self_max_h - 50]
            # 为了不依赖外部，我们使用默认 0..1280 / 0..720 范围，但在 draw 时不会溢出
            for _ in range(max_attempts):
                # 随机食物类型
                self.foodIndex = random.randint(0, len(self.foodImages) - 1)
                img = self.foodImages[self.foodIndex]
                # 确保 shape 可用（img 可能是 2D/3D ）
                try:
                    h, w = img.shape[:2]
                except Exception:
                    h, w = 50, 50
                self.hFood, self.wFood = h, w
                # 随机位置（靠内侧，避免边缘）
                rx = random.randint(50, max(50, 1280 - 50))
                ry = random.randint(50, max(50, 720 - 50))
                self.foodPoint = (rx, ry)
                # 如果传入障碍管理器，检查是否与任一障碍重叠
                if obstacleManager:
                    overlap = False
                    for ox, oy, ow, oh, *_ in obstacleManager.obstacles:
                        if ox < rx < ox + ow and oy < ry < oy + oh:
                            overlap = True
                            break
                    if overlap:
                        continue
                # 找到一个不重叠的位置
                return
            # 若多次尝试失败，则保留最后的值
            return

        def draw(self, imgMain):
            """把当前食物图片覆盖到主图上（使用 cvzone.overlayPNG 以支持 alpha）"""
            rx, ry = self.foodPoint
            # 防止越界
            try:
                h, w = self.foodImages[self.foodIndex].shape[:2]
            except Exception:
                h, w = 50, 50
            self.hFood, self.wFood = h, w
            # overlayPNG 需要左上角坐标
            top_left = (int(rx - w // 2), int(ry - h // 2))
            try:
                imgMain = cvzone.overlayPNG(
                    imgMain, self.foodImages[self.foodIndex], top_left)
            except Exception:
                # 如果 overlay 失败，尝试简单贴图（忽略 alpha）
                try:
                    imgMain[top_left[1]:top_left[1] + h, top_left[0]:top_left[0] + w] = \
                        cv2.resize(
                            self.foodImages[self.foodIndex][:, :, :3], (w, h))
                except Exception:
                    pass
            return imgMain

    # ================= 内部类：ObstacleManager =================
    class ObstacleManager:
        def __init__(self, obstaclePaths):
            """
            obstaclePaths: list 图片路径
            self.obstacles: list of [x, y, w, h, dx, dy, img]
            """
            self.obstacleImages = []
            for path in obstaclePaths:
                img = _safe_read_image(path)
                self.obstacleImages.append(img)
            self.obstacles = []

        def randomObstacles(self):
            """基于 obstacleImages 生成一组随机位置和速度的障碍物"""
            self.obstacles.clear()
            for img in self.obstacleImages:
                try:
                    h, w = img.shape[:2]
                except Exception:
                    h, w = 50, 50
                # 随机位置（避免太靠边）
                x = random.randint(150, max(150, 1280 - w - 10))
                y = random.randint(50, max(50, 720 - h - 10))
                dx = random.choice([-5, 5])
                dy = random.choice([-5, 5])
                self.obstacles.append([x, y, w, h, dx, dy, img])

        def moveObstacles(self, wMax, hMax):
            """更新每个障碍的位置并在边界反弹"""
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
            """把所有障碍物绘制到主图上"""
            for obs in self.obstacles:
                x, y, w, h, dx, dy, img = obs
                try:
                    imgMain = cvzone.overlayPNG(imgMain, img, (int(x), int(y)))
                except Exception:
                    # fallback: 直接简单覆盖（忽略 alpha）
                    try:
                        imgMain[int(y):int(y) + h, int(x)
                                    :int(x) + w] = img[:, :, :3]
                    except Exception:
                        pass
            return imgMain
