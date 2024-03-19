"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
"""

import wx
# import array
# import numpy as npy
import datetime
from lunardate import LunarDate
# This is a sample Python script.
# import time
# from typing import Union
#
#
# row = 0
# col = 0
# row_buf = npy.zeros((16), dtype=npy.uint8)
# rtemp =0
# ctemp=0
#
# # flag_led=[[0 for i in range(11)] for i in range(12)]
# flag_led = npy.zeros((11, 12), dtype=npy.uint8)
# flag = 0
# datasend = [1, 0, 1, 0, 13, 10]


# 文本输入对话框(TextEntryDialog)

# import wx

# 下拉列表框(wx.ComboBox)



distros1 = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
distros2 = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二",
            "十三", "十四", "十五",
            "十六", "十七", "十八", "十九", "二十", "二十一", "二十二", "二十三", "二十四", "二十五", "二十六",
            "二十七", "二十八", "二十九", "三十",
            "三十一"]
distros3 = ["子时", "丑时", "寅时", "卯时", "辰时", "巳时", "午时", "未时", "申时", "酉时", "戌时", "亥时"]

dist = ["大安", "流连", "速喜", "赤口", "小吉", "空亡"]

input_text = ["一月", "初一", "子时"]
input_num = [1, 2, 3]
output_text = ["大安", "流连", "速喜"]


class SampleComboBox(wx.Frame):

    def __init__(self, *args, **kw):
        super(SampleComboBox, self).__init__(*args, **kw)

        self.InitUi()

    def InitUi(self):
        global input_text, input_num, distros1, distros2, distros3, dist, output_text
        # 设置标题
        self.SetTitle("小六壬推算(农历：月、日、时辰)")
        # 设置窗口尺寸
        self.SetSize(400, 240)

        panel = wx.Panel(self)

        bgh = 20
        bgv = 30
        bg2h = 50

        today = datetime.datetime.today()

        # tt=datetime.date.today()
        # print(tt)


        # current_Year = str(today.year)
        # current_Month = str(today.month)
        # current_Day = str(today.day)
        # current_Hour = str(today.hour)
        # current_Minute = str(today.minute)
        # current_Second = str(today.second)

        tt2 = LunarDate.fromSolarDate(today.year,today.month,today.day)
        # print(tt2.year)
        # print(tt2.month)
        # print(tt2.day)
        # print('====================')

        # a1=today.hour // 10
        # a2=today.hour-a1*10
        # b1=today.minute//10
        # b2=today.minute-b1*10
        # add=a1+a2+b1+b2
        # print(a1)
        # print(a2)
        ttt=today.hour+1
        shichen=0
        # ttt=3+1
        if (ttt//2==0 and today.minute>0) or (ttt//2==0 and today.second>0):
            # print(distros3[0])
            shichen=0
        elif (ttt//2==1 and today.minute>0) or (ttt//2==1 and today.second>0):
            # print(distros3[1])
            shichen = 1
        elif (ttt//2==2 and today.minute>0) or (ttt//2==2 and today.second>0):
            # print(distros3[2])
            shichen = 2
        elif (ttt//2==3 and today.minute>0) or (ttt//2==3 and today.second>0):
            # print(distros3[3])
            shichen = 3
        elif (ttt//2==4 and today.minute>0) or (ttt//2==4 and today.second>0):
            # print(distros3[4])
            shichen = 4
        elif (ttt//2==5 and today.minute>0) or (ttt//2==5 and today.second>0):
            # print(distros3[5])
            shichen = 5
        elif (ttt//2==6 and today.minute>0) or (ttt//2==6 and today.second>0):
            # print(distros3[6])
            shichen = 6
        elif (ttt//2==7 and today.minute>0) or (ttt//2==7 and today.second>0):
            # print(distros3[7])
            shichen = 7
        elif (ttt//2==8 and today.minute>0) or (ttt//2==8 and today.second>0):
            # print(distros3[8])
            shichen = 8
        elif (ttt//2==9 and today.minute>0) or (ttt//2==9 and today.second>0):
            # print(distros3[9])
            shichen = 9
        elif (ttt//2==10 and today.minute>0) or (ttt//2==10 and today.second>0):
            # print(distros3[10])
            shichen = 10
        elif (ttt//2==11 and today.minute>0) or (ttt//2==11 and today.second>0):
            # print(distros3[11])
            shichen =11





        today=str(today)
        today_lunar=str(tt2.year)+"年"+" "+distros1[tt2.month]+" "+distros2[tt2.day]+" "+distros3[shichen]
        # /a=
        wx.StaticText(panel, label="使用说明：选取当前农历月、日、时辰" + "\n" + "即可得到所想念头对应事物的状态", pos=(bgh*7, bgv-10))

        wx.StaticText(panel, label="月:", pos=(bgh, bgv+5))
        wx.StaticText(panel, label="日:", pos=(bgh, bgv + 45+5))
        wx.StaticText(panel, label="时:", pos=(bgh, bgv + 45 * 2+5))

        wx.StaticText(panel, label="当前时刻(阳历):"+today, pos=(bgh, bgv + 41 * 3))
        wx.StaticText(panel, label="当前时刻(阴历):" + today_lunar, pos=(bgh, bgv + 41 * 3+20))

        # 创建一个只读下拉列表，可选择Linux的各种发行版本
        cb1 = wx.ComboBox(panel, pos=(bg2h-5, bgv), choices=distros1, style=wx.CB_READONLY)
        cb1.SetSelection(0)
        cb1.Bind(wx.EVT_COMBOBOX, self.OnSelectyue)

        # 创建一个只读下拉列表，可选择Linux的各种发行版本
        cb2 = wx.ComboBox(panel, pos=(bg2h-5, bgv + 45), choices=distros2, style=wx.CB_READONLY)
        cb2.SetSelection(0)
        cb2.Bind(wx.EVT_COMBOBOX, self.OnSelectri)
        # ri = distros2.index(e.GetString())
        # print("hhh:"+ri)

        # 创建一个只读下拉列表，可选择Linux的各种发行版本
        cb3 = wx.ComboBox(panel, pos=(bg2h-5, bgv + 45 * 2), choices=distros3, style=wx.CB_READONLY)
        cb3.SetSelection(0)
        cb3.Bind(wx.EVT_COMBOBOX, self.OnSelectshi)

        # 用于显示结果
        self.stcInfo = wx.StaticText(panel, label="", pos=(150, bgv+45))
        self.Centre()

    def OnSelectyue(self, e):
        global input_text, input_num, distros1, dist, output_text
        input_text[0] = e.GetString()
        yue = distros1.index(e.GetString())
        input_num[0] = yue % 6
        # print(yue)
        # print(dist[input_num[0]])
        output_text[0] = dist[input_num[0]]
        # print(output_text)
        # self.stcInfo.SetLabel("农历月日时: " + input_text)
        self.stcInfo.SetLabel(
            "输入的月日时:  " + input_text[0] + "  " + input_text[1] + "  " + input_text[2]
            + "\n" + "输出的结果： " + output_text[0] + "  " + output_text[1] + "  " + output_text[2])

    def OnSelectri(self, e):
        global input_text, input_num, distros2, dist, output_text
        input_text[1] = e.GetString()
        ri = distros2.index(e.GetString())
        input_num[1] = (ri + input_num[0]) % 6
        # print(dist[input_num[1]])
        output_text[1] = dist[input_num[1]]
        # self.stcInfo.SetLabel("农历月日时: " + input_text)
        self.stcInfo.SetLabel(
            "输入的月日时:  " + input_text[0] + "  " + input_text[1] + "  " + input_text[2]
            + "\n" + "输出的结果： " + output_text[0] + "  " + output_text[1] + "  " + output_text[2])

    def OnSelectshi(self, e):
        global input_text, input_num, distros3, dist, output_text
        input_text[2] = e.GetString()
        shi = distros3.index(e.GetString())
        input_num[2] = (shi + input_num[1]) % 6
        # print(shi)
        # print(dist[input_num[2]])
        output_text[2] = dist[input_num[2]]
        self.stcInfo.SetLabel(
            "输入的月日时:  " + input_text[0] + "  " + input_text[1] + "  " + input_text[2]
            + "\n" + "输出的结果： " + output_text[0] + "  " + output_text[1] + "  " + output_text[2])

    # def random(self, t):
    #     a1= current_Hour %10


def main():
    app = wx.App()
    sample = SampleComboBox(None)
    sample.Show()
    app.MainLoop()


if __name__ == "__main__":
    # current_time = datetime.datetime.now()
    # today = datetime.datetime.today()
    # current_Year = today.year
    # current_Month = today.month
    # current_Day = today.day
    # current_Hour = today.hour
    # current_Minute = today.minute
    # current_Second = today.second
    # print(current_time)

    main()
