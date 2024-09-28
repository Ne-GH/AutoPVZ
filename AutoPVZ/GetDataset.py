import win32gui
import pyautogui


class GetDataset:

    def __init__(self):
        self.image_count = 0
        self.height = None
        self.width = None
        self.left_top = None


    def get_window_pos(self):
        hWnd = win32gui.FindWindow(None, "植物大战僵尸杂交版v2.1 ")
        left, top, right, bot = win32gui.GetWindowRect(hWnd)
        self.left_top = (left, top)
        self.width = right - left
        self.height = bot - top

    def get_image(self,image_name):
        image = pyautogui.screenshot(region=(self.left_top[0], self.left_top[1], self.width, self.height))
        image.save(image_name + '_' + str(self.image_count) + '.png')
        self.image_count += 1

    def get_dataset(self):
        self.get_window_pos()
        self.get_image('image')


