# 自己写的入口包
import os
from time import sleep

from entrance import Entrance
# 自己导入By，方便使用页面元素
from selenium.webdriver.common.by import By

from input import Input

init_entrance = Entrance()
init_entrance.go('https://app.flowoss.com/zh-CN')

init_input = Input(init_entrance)


class Output(object):

    def __init__(self, entrance, input):
        self.entrance = entrance
        self.input = input

    def input_btn(self):
        self.input.input_file('//*[@id="layout"]/div/div/div[5]/div/div[1]/div[2]/div[2]/button[2]/input', file_path)
        self.entrance.find_and_click('//*[@id="layout"]/div/div/div[5]/div/div[1]/div[2]/div[2]/button[1]')
        sleep(1)


if __name__ == '__main__':
    file_path = os.path.expanduser(
        'D:\\软件测试学习\\资料\\洪\\Google软件测试之道 ([美]James Whittaker　Jason Arbon　Jeff Carollo 著) (Z-Library).epub')
    output_test = Output(init_entrance, init_input)
    output_test.input_btn()
