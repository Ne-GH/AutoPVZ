import sys
import ctypes
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor, QPen


class LayeredWindow(QWidget):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # 设置无边框窗口、保持在顶部和背景透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 设置窗口大小
        self.setGeometry(x, y, width, height)


        # 获取窗口句柄
        hwnd = self.winId().__int__()

        # 设置分层和透明样式
        self.set_click_through(hwnd)

    def set_click_through(self, hwnd):
        # 设置 WS_EX_LAYERED 和 WS_EX_TRANSPARENT 属性，以允许鼠标点击穿透
        GWL_EXSTYLE = -20
        WS_EX_LAYERED = 0x80000
        WS_EX_TRANSPARENT = 0x20

        # 获取当前窗口样式
        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

        # 设置分层和透明属性（使窗口点击穿透）
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style | WS_EX_LAYERED | WS_EX_TRANSPARENT)

    def paintEvent(self, event):
        self.setGeometry(self.x, self.y, self.width, self.height)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 设置画笔颜色和宽度（仅用于边框）
        painter.setPen(QPen(QColor(0, 255, 0, 255), 2))  # 绿色边框，宽度为3像素

        # 绘制空心矩形
        painter.drawRect(0, 0, self.width, self.height)  # 使用调整后的坐标

    def move_to(self, x, y, width = None, height = None):
        self.x = x
        self.y = y

        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

        self.update()

val = 0
def test(window):
    global val
    window.move_to(val,val)
    val += 5




if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer = QTimer()

    x = 0
    # 创建一个分层窗口
    layered_window = LayeredWindow(100,100,100,100)
    layered_window.show()
    timer.timeout.connect(lambda :test(layered_window))
    timer.start(100)

    sys.exit(app.exec())
