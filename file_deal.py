# -*- coding: utf-8 -*-
# @Time     :2022/1/24 15:54
# @Author   :Yussio
# @File     :file_deal.py

#导库
import xlwings as xw

#创建①
'''
wb = xw.Book()
wb.save('1.xlsx')
wb.close()
'''
#创建②
'''
app=xw.App(visible=False,add_book=False)
wb=app.books.add()
wb.save('1.xlsx')
wb.close()
app.quit() #结束进程
'''

#open file
app = xw.App(visible=False,add_book=False)
app.display_alerts=False
app.screen_updating=False
wb = app.books.open('G:\\douban.xlsx')

#实例化
sheet1 = wb.sheets[0]

sheet1.range('A1').value = 'python知识学堂'


print('value of D2:',sheet1.range('D2').value)
print(wb.fullname)
wb.save('G:\\workspace\douban.xlsx')
wb.close()
app.quit()

