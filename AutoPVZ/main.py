#对后台窗口截图
import win32gui

#获取后台窗口的句柄，注意后台窗口不能最小化
hWnd = win32gui.FindWindow("Chrome_WidgetWin_1","在线翻译_有道 - Google Chrome") #窗口的类名可以用Visual Studio的SPY++工具获取
#获取句柄窗口的大小信息
left, top, right, bot = win32gui.GetWindowRect(hWnd)
width = right - left
height = bot - top