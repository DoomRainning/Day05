# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 09:00:59 2018

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
if menno=='1':
    import urllib.request as r
    city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric ".format('leshan')
    info=r.urlopen(city_address).read().decode('utf-8','ignore')            
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
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm 
from matplotlib import axes
def draw_heatmap(data,xlabels,ylabels):

    cmap = cm.Reds    

    figure=plt.figure(facecolor='w')

    ax=figure.add_subplot(2,1,1,position=[0.1,0.15,0.8,0.8])

    ax.set_yticks(range(len(ylabels)))

    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))

    ax.set_xticklabels(xlabels)
    vmax=data[0][0]
    vmin=data[0][0]
    for i in data:
        for j in i:
            if j>vmax:
                vmax=j
            if j<vmin:
                vmin=j
    map=ax.imshow(data,interpolation='nearest',cmap=cmap,aspect='auto',vmin=vmin,vmax=vmax)
    cb=plt.colorbar(mappable=map,cax=None,ax=None,shrink=0.5)
    plt.title("Temperature:"+"  "+city) #标题
    plt.show()
#a=[[22.62,26.62,27.94,20.24,19.09,18.88,18.89,18.35],[19.1,21.98,23.28,22.19,20.33,17.5,15.89,14.99],[20.29,24.12,26.59,26.33,22.62,19.19,17.14,15.92]]
(temp_ls).append(22)
a=np.array(temp_ls).reshape(5,8)
xlabels=['3:00','6:00','9:00','12:00','15:00','18:00','21:00','24:00']
ylabels=['6-8','6-9','6-10','6-11','6-12']
draw_heatmap(a,xlabels,ylabels)
