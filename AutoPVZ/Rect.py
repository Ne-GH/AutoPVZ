from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QColor

class Rect(QWidget):
    def __init__(self):
        super().__init__()

        # 设置无边框窗口、保持在顶部和背景透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 设置窗口大小
        self.setGeometry(100, 100, 400, 300)

        # 获取窗口句柄
        hwnd = self.winId().__int__()

        # 设置分层和透明样式
        self.set_click_through(hwnd)

    def show(self):
        super.show()
