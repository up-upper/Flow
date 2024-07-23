# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# 1.导包
# selenium 4
# 导入驱动 可以访问api
from selenium import webdriver
# 导入浏览器的服务 唤醒浏览器
from selenium.webdriver.chrome.service import Service as ChromeService
# webdriver manager驱动管理
# 会自动识别本机浏览器版本，通过本机浏览器版本下载驱动
from webdriver_manager.chrome import ChromeDriverManager
# 用谷歌比较标准
# 导入time
# 导入By，方便我们使用页面元素。
from selenium.webdriver.common.by import By
from time import sleep


# import urllib3
# #
# http = urllib3.PoolManager()
# response = http.request('GET', 'https://app.flowoss.com/zh-CN', timeout=urllib3.Timeout(connect=1.0, read=5.0))

class Entrance(object):
    def __init__(self):
        # 每个selenium项目都要有一个浏览器驱动，去唤醒浏览器的服务
        # 类需要一个driver
        # webdriver需要指明浏览器，Chrome Edge等
        # 导入对应浏览器的驱动的地址，
        # 如果不使用驱动管理器就必须自己手动下载
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # self.driver = webdriver.Chrome(service=ChromeService())

    def go(self, url):
        self.driver.get(url)
        sleep(3)

    def find_and_input(self, xpath, file_path):
        # send_keys()相当于输入
        self.driver.find_element(By.XPATH, xpath).send_keys(file_path)

    def find_and_click(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()
        sleep(3)

    def quit(self):
        self.driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # entrance_1 = Entrance()
    # entrance_1.go('https://app.flowoss.com/zh-CN')
    # entrance_1.quit()

    entrance_2 = Entrance()
    entrance_2.go('https://www.flowoss.com/zh-CN')
    entrance_2.find_and_click('//*[@id="__next"]/div/main/div/div[1]/div[1]/a')
    entrance_2.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
