from time import sleep

from download import Download
from entrance import Entrance
from read import Read

init_entrance = Entrance()
init_download = Download(init_entrance)
init_read = Read(init_entrance, init_download)


class Find(object):

    def __init__(self, entrance, read):
        self.entrance = entrance
        self.read = read

    def find_text(self):
        self.read.read_btn()
        sleep(1)
        # 滚动到页面垂直位置500px的位置
        self.entrance.driver.execute_script("window.scrollTo(0, 500);")


if __name__ == '__main__':
    find_test = Find(init_entrance, init_read)
    find_test.find_text()
