# 自己写的入口包
from time import sleep

from entrance import Entrance
# 自己导入By，方便使用页面元素
from selenium.webdriver.common.by import By

from download import Download

# 实例化一个 Entrance 类的对象，并将这个新创建的实例赋值给变量 init_entrance。
init_entrance = Entrance()
init_entrance.go('https://app.flowoss.com/zh-CN')

init_download = Download(init_entrance)


class Output(object):

    def __init__(self, entrance, download):
        # self 是类实例的引用，用于访问类的属性和方法。在类的方法中，self 是自动传入的第一个参数，它代表了类的当前实例。
        # self.entrance = entrance 这行代码的意思是：将外部传入的 entrance 参数
        # （它可能是一个对象、值或任何类型的数据）赋值给当前类实例的entrance 属性。
        self.entrance = entrance
        self.download = download

    def input_btn(self):
        self.download.click_btn()
        self.entrance.find_and_click('//*[@id="layout"]/div/div/div[5]/div/div[1]/div[2]/div[2]/button[1]')
        sleep(3)


if __name__ == '__main__':
    output_test = Output(init_entrance, init_download)
    output_test.input_btn()
