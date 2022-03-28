# -*- coding: utf-8 -*-
# @Time     :2022/3/2 15:11
# @Author   :Yussio
# @File     :click.py
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:59:31 2018
@author: desert
"""
# move the indicator every 5 minutes

import pyautogui

import pyautogui
import time

pyautogui.FAILSAFE = False

import time

# move the indicator every 5 minutes
while True:
    time.sleep(20)  # 设置5分钟
    x, y = pyautogui.position()
    pyautogui.click(button='right')
