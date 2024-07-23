# 自己写的入口包
from time import sleep

from entrance import Entrance
# 自己导入By，方便使用页面元素
from selenium.webdriver.common.by import By

init_entrance = Entrance()
init_entrance.go('https://app.flowoss.com/zh-CN')


class Download(object):

    def __init__(self, entrance):
        self.entrance = entrance

    def click_btn(self):
        self.entrance.find_and_click('//*[@id="layout"]/div/div/div[5]/div/div[1]/div[2]/div[1]/button')
        sleep(5)


if __name__ == '__main__':
    download_test = Download(init_entrance)
    download_test.click_btn()
