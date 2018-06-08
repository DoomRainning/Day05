# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:31:40 2018

@author: lenovo
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 08:31:18 2018

@author: lenovo
"""

#1.导包
import urllib.request as r
import json
import time
import matplotlib.pyplot as plt
from pylab import * 

#支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']  
temp_ls=[]
time_ls=[]
city_1=[]
    #判断选择
    #3.城市查询


def get_city(z):
     if z=="1":
             city='leshan'
     else:
             city=input('请输入城市拼音：')
     return(city)
    

def Information_output(z):
    if z=="1":
             city='leshan'
             time.sleep(1)
             print("你所查询的信息如下：")
             print(Check_Information(city))
             print("感谢您的使用，再见！")
             time.sleep(1)
    elif z=="2":
             city=input('请输入城市拼音：')
             time.sleep(1)
             print("你所查询的信息如下：")
             time.sleep(1)
             print(Check_Information(city))   
             print("感谢您的使用，再见！")
             time.sleep(1)
    else:
            city=input('请输入您所需要保存信息的城市拼音')
            time.sleep(1)
            print("信息保存成功！！！")
            print("感谢您的使用，再见！")
            time.sleep(1)
        
    #2.欢迎界面
def Welcome_window():
    print('欢迎使用城市天气查询系统')
    time.sleep(1)
    print('尊敬的使用者，您是第一次使用本系统吗？ ')
    time.sleep(1)
    a=input('请输入 YES or NO ')
    return a
      
    #用户选择  
def Choose_Information(a):
    if a=='YES':
        time.sleep(1)
        print('欢迎第一次使用天气查询系统')
        time.sleep(1)
        print('1.查看当前城市天气   2.查看其它城市天气  3.天气信息存储')
        z=input("菜单是:")
    else:
        time.sleep(1)
        print('1.查看当前城市天气   2.查看其它城市天气  3.天气信息存储')
        z=input("菜单是：")
    return(z)


    #信息查询 
def Check_Information(city): 
    city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996 ".format(city)
    info=r.urlopen(city_address).read().decode('utf-8','ignore')
    data=json.loads(info)
    index=int(len(data['list']))
    ls=[]
    for i in range(0,index):
        day=data['list'][i]
        time=day['dt_txt']
        temp=day['main']['temp']
        description=day['weather'][0]['description']
        temp_max=day['main']['temp_max']
        pressure=day['main']['pressure']
        time_ls.append(time)
        temp_ls.append(temp)
        information_weather=('{}: 当前时间:{} 温度为:{} 天气情况:{} 最高温度:{} 气压为:{}'.format(city,time,temp,description,temp_max,pressure))
        ls.append(information_weather)
        #print(information_weather)
        return(information_weather)
    return(ls)



    #4.信息存储
def Save_City_name(city):
    city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996 ".format(city)
    info=r.urlopen(city_address).read().decode('utf-8','ignore')
    data=json.loads(info)
    index=int(len(data['list']))
    information_weather=[]
    fo = open("foo.txt", "w")
    for i in range(0,index):
            day=data['list'][i]
            time=day['dt_txt']
            temp=day['main']['temp']
            description=day['weather'][0]['description']
            temp_max=day['main']['temp_max']
            pressure=day['main']['pressure']
            time_ls.append(time)
            temp_ls.append(temp)
            information_weather=('{} 当前时间{}温度为{}，天气情况{}，最高温度{}，气压为{}'.format(city,time,temp,description,temp_max,pressure))
            fo.write(information_weather+'\n')
    fo.close()
    print ("文件名: ", fo.name)
    print ("是否已关闭 : ", fo.closed)
    print ("访问模式 : ", fo.mode)
# 关闭打开的文件

def plot_lines():                       #支持中文
        mpl.rcParams['font.sans-serif'] = ['SimHei'] 
        names=time_ls
        x = range(len(names))
        y=temp_ls
        plt.plot(x, y, marker='o', mec='r', mfc='w',label=u'温度变化曲线')
        plt.legend()  # 让图例生效
        plt.xticks(x, names, rotation=80)
        plt.margins(0)
        plt.subplots_adjust(bottom=0.15)
        plt.xlabel(u"time(s)时间") #X轴标签
        plt.ylabel("温度") #Y轴标签
        plt.title("Temperature:"+"  "+str(get_city(z))) #标题
        plt.show()
a=Welcome_window()
z=Choose_Information(a)
Information_output(z)

    
    
    
