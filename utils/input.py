# 自己写的入口包
from time import sleep

from entrance import Entrance
# 自己导入By，方便使用页面元素
from selenium.webdriver.common.by import By
import os

init_entrance = Entrance()
init_entrance.go('https://app.flowoss.com/zh-CN')


class Input(object):

    def __init__(self, entrance):
        self.entrance = entrance

    def input_file(self, xpath, file_path):
        self.entrance.find_and_input(xpath, file_path)
        sleep(1)


if __name__ == '__main__':
    file_path = os.path.expanduser(
        '"D:\\flow\\data\\Google软件测试之道 ([美]James Whittaker　Jason Arbon　Jeff Carollo 著) (Z-Library).epub"')
    input_test = Input(init_entrance)
    input_test.input_file('//*[@id="layout"]/div/div/div[5]/div/div[1]/div[2]/div[2]/button[2]/input', file_path)
