# Author: SH
# Data: 2019/8/5
# Status
# Comment: 配套该目录中的appconfig使用，当超出activity就拉到指定activity

import os
import re
import xml.dom.minidom as xmldom
import time

class Mtest():
    def __init__(self):
        dom = xmldom.parse('app_config.xml')
        root = dom.documentElement              # 将 XML 数据在内存中解析成一个树，通过对树的操作来操作XML
        self.packagename = root.getElementsByTagName('packagename')[0].firstChild.data
        self.mainactivity = root.getElementsByTagName('mainactivity')[0].firstChild.data        # 主activity
        self.interval = int(root.getElementsByTagName('interval')[0].firstChild.data)
        self.count = int(root.getElementsByTagName('count')[0].firstChild.data)
        self.whiteactivity = root.getElementsByTagName('whiteactivity')[0].firstChild.data.replace('\n', '').replace(
            ' ', '').split(',')

    def get_now_activity(self):
        '''
        获取当前所在activity，判断其是否在白名单里，如果在就做操作，如果不在就拉回主页面（当然你可以设置拉回任何页面，甚至随机）
        :return:
        '''
        os.system("adb devices")
        content = os.popen('adb shell dumpsys activity  |findstr "mResumedActivity" ').read()  # 获取当前所在activity
        pattern = re.compile(r'/[a-zA-Z0-9\.]+')            # 用正则表达式规则：将其取出输出alist[0],r'--标识不转义，\.转义为'.'
        alist = pattern.findall(content)                        # 查找所有结果
        macitivity = self.packagename + '/' + self.mainactivity  # 拼接目的activity
        excuteshell = 'adb shell am start -n ' + macitivity
        if alist[0] not in self.whiteactivity:
            print('当前activity:' + alist[0])
            print('--------------开始返回主activity----------------')
            os.system(excuteshell)  # 可拉回主页面
        else:
            print('当前activity:' + alist[0] + '不需要返回')

    def check(self):
        for _ in range(self.count):
            time.sleep(self.interval)
            self.get_now_activity()

if __name__ == '__main__':
    test = Mtest()
    test.check()