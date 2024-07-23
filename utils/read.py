# 自己写的入口包
from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from entrance import Entrance
# 自己导入By，方便使用页面元素
from selenium.webdriver.common.by import By

from download import Download

init_entrance = Entrance()
init_entrance.go('https://app.flowoss.com/zh-CN')

init_download = Download(init_entrance)


class Read(object):

    def __init__(self, entrance, download):
        self.entrance = entrance
        self.download = download

    # def read_btn(self):
    #     self.download.click_btn()
    #     sleep(1)
    #     # 颠颠的，获取的xpath是下载完样书后的，但是自动化测试能跨步骤得到后面的数据吗，但是我不知道怎么实现自动获取下载后列表的图书xpath
    #     self.entrance.find_and_click('//*[@id="layout"]/div/div/div[5]/div/div[2]/ul/div/div[1]/img')
    #     sleep(10)
    #     # 想要实现页面滑动，但没有实现
    #     # self.entrance.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     # self.entrance.driver.execute_script("window.scrollTo(0, 2000);")
    #     # js = 'window.scrollTo(0, document.body.scrollHeight)'
    #     # self.entrance.driver.execute_script(js)
    #     # 使用CSS选择器找到div
    #     scrollable_div = self.entrance.driver.find_element(By.CSS_SELECTOR, '.epub-container')
    #     # scrollable_div = self.entrance.driver.find_element_by_css_selector('.epub-container')
    #     # 使用JavaScript滚动到这个div的底部
    #     self.entrance.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", scrollable_div)
    #     sleep(3)
    def read_btn(self):
        self.download.click_btn()
        sleep(1)  # 等待下载按钮点击后的响应
        self.entrance.find_and_click('//*[@id="layout"]/div/div/div[5]/div/div[2]/ul/div/div[1]/img')
        # 这里假设点击后页面会更新，并包含.epub-container元素
        try:
            # 等待.epub-container元素可见
            scrollable_div = WebDriverWait(self.entrance.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.epub-container'))
            )

            # 计算并滚动到.epub-container的底部
            self.entrance.driver.execute_script(
                "arguments[0].scrollTo(0, arguments[0].scrollHeight);", scrollable_div
            )
            sleep(3)  # 等待滚动完成和其他可能的页面响应

        except TimeoutException:
            print("无法找到.epub-container元素")


if __name__ == '__main__':
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    read_test = Read(init_entrance, init_download)
    read_test.read_btn()
