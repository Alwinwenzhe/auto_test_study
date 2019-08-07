# Author: SH
# Data: 2019/6/18
# Status 
# Comment:GUI自动化

import pyautogui,time

time.sleep(3)
########鼠标控制############
print(pyautogui.position())         # print current position
print(pyautogui.size())                    # print screen weight and height
pyautogui.moveTo(100,101,0.5)      # move mouse to position
pyautogui.click(100,105)           # click specified position
pyautogui.doubleClick()      # double click specified position，如果没指定位置，就是双击当前位置
# pyautogui.click(button='right')     #在当前位置点击鼠标右键
pyautogui.moveTo(30,130)
# pyautogui.mouseDown(30,130,button='left')               #按下鼠标左键
time.sleep(1)
# pyautogui.dragTo(130,130,duration=1,button='left')           #按下鼠标左键并拖动到指定位置
# pyautogui.dragRel(30,130,duration=1,button='left')         #拖动桌边的迅雷图标到相对位置

# pyautogui.scroll()                  #滚动当前屏幕

#########屏幕控制##############
im = pyautogui.screenshot()         #获取当前屏幕快照
print(im.getpixel((30,130)))        #获取固定点坐标的像素颜色，返回的是rgb元组；注意参数传入的是xy合体坐标
result = pyautogui.pixelMatchesColor(30,130,(97, 161, 256))     # 得到的结果值是False，因为正确值是：97, 161, 255

print(result)

#########键盘###############
time.sleep(5)
print(pyautogui.position())

#桌面上点击pyautogui.txt,进行编辑
pyautogui.moveTo(112, 41)
pyautogui.doubleClick()
time.sleep(3)
pyautogui.typewrite('hello',1)      #输入文本
pyautogui.typewrite(['enter'])      #调用enter键
pyautogui.typewrite(['tab'])        #调用tab键
pyautogui.typewrite('123')
pyautogui.keyDown('shift')          #按下shift
pyautogui.typewrite('4')            #这里输入的是中文的￥
pyautogui.keyUp('shift')            #松开shift
time.sleep(1)
pyautogui.hotkey('ctrl','a')        #热键可以接受多个案件的字符串参数，按顺序按下，按相反顺序释放
time.sleep(1)
pyautogui.hotkey('ctrl','c')
time.sleep(1)
pyautogui.typewrite(['pagedown'])   #焦点切换到最后
time.sleep(1)
pyautogui.hotkey('ctrl','v')        #注意不要再当前位置粘贴，否则没效果