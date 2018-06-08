# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:37:47 2018

@author: lenovo
"""

import time
print('欢迎使用全球天气app')
time.sleep(1)
print('1.查看当前城市天气',   
      '2.查看其他城市天气',  
      '3.保存当前城市')
time.sleep(1)
menno=input('请输入菜单：')
temp_ls=[]
time_ls=[]
city_1=[]
if menno=='1':
    import urllib.request as r
    city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric ".format("leshan")
    info=r.urlopen(city_address).read().decode('utf-8','ignore')
    city_1.append("leshan")
            
    import json
    data=json.loads(info)
    index=int(len(data['list']))
    for i in range(0,index):
        day=data['list'][i]
        time=day['dt_txt']
        time_ls.append(time)
        temp=day['main']['temp']
        temp_ls.append(temp)
        description=day['weather'][0]['description']
        temp_max=day['main']['temp_max']
        pressure=day['main']['pressure']
        print('{}, 时间:{},  温度:{},  天气:{},  最高温度:{},  气压:{}'.format('leshan',time,temp,description,temp_max,pressure))
        print('-'*50) 

if menno=='2':
    print('2.查看其他城市天气')
    import urllib.request as r

    city=input('请输入城市拼音：')
    city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric ".format(city)
    info=r.urlopen(city_address).read().decode('utf-8','ignore')
    city_1.append(city)
            
    import json
    data=json.loads(info)
    index=int(len(data['list']))
    for i in range(0,index):
        day=data['list'][i]
        time=day['dt_txt']
        time_ls.append(time)
        temp=day['main']['temp']
        temp_ls.append(temp)
        description=day['weather'][0]['description']
        temp_max=day['main']['temp_max']
        pressure=day['main']['pressure']
        print('{}, 时间:{},  温度:{},  天气:{},  最高温度:{},  气压:{}'.format(city,time,temp,description,temp_max,pressure))
        print('-'*50)
  
if menno=='3':
    print('3.保存当前城市')
    
    print('保存成功！')

import matplotlib.pyplot as plt
from pylab import *                           #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
names=time_ls
time_ls1=[]
x = range(len(names))
y=temp_ls
plt.plot(x, y, marker='o', mec='r', mfc='w',label=u'温度变化曲线')
plt.legend()  # 让图例生效
plt.xticks(x, names, rotation=80)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"time(s)时间") #X轴标签
plt.ylabel("温度") #Y轴标签
plt.title("Temperature:"+"  "+str(city_1)) #标题
plt.show()

