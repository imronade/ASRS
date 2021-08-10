# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:56:06 2021

@author: Imron Ade
"""

# import data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

df = pd.read_excel('template.xlsx')
df['Local Date Time'] = pd.to_datetime(df['Local Date Time'])


# make hourly data
df2 = df.resample('1H', on = 'Local Date Time').mean()

colnames = list(df2.columns)
index_rm_colnames = [0,1,5,8,9,10,11,12,13]
rm = []
for i in index_rm_colnames:
    rm_colnames = colnames[i]
    rm.append(rm_colnames)

filtered_colnames = []
for i in colnames:
    if i not in rm:
        filtered_colnames.append(i)
warna = ['RdBu_r','vlag','YlOrBr','coolwarm','coolwarm']

for x in range(0,len(filtered_colnames)):
    i=filtered_colnames[x]
    # heatmap
    # df3 = df.set_index('Local Date Time')
    # df_m = df3[i].copy()
    # df_m = df_m.to_frame()
    # df_m['day'] = [i.day for i in df_m.index]
    # days = df_m.day.unique()
    # df_m['hour'] = [i.hour for i in df_m.index]
    # hour = df_m.hour.unique()
    # df_m = df_m.groupby(['day', 'hour']).mean()
    # df_m2 = df_m.unstack(level=0)
    # # df_m = df_m.round(decimals=2)
    # # color map
    # # cmap = sb.diverging_palette(0, 40, 83, 68, as_cmap=True)
    # fig, ax = plt.subplots(figsize=(14, 18))
    # sb.heatmap(df_m, annot=True, fmt =".2f",cmap="Blues",
    #                 annot_kws={"size": 7})
    # # xticks = []
    # # for a in range(1,(len(df_m.columns)+1)):
    # #     if a % 2 != 0:
    # #         xticks.append(a)
    # xticks = list(range(1,(len(df_m.columns)+1)))
    # plt.xticks(plt.xticks()[0], labels=xticks, rotation=1)
    
    # # title
    # title = str(i)+' \n'
    # plt.title(title, loc='center', fontsize=20)
    # plt.xlabel('days')
    # plt.savefig("contoh.png")

    # contour plot
    # preparing data
    df3 = df.set_index('Local Date Time')
    df_m = df3[i].copy()
    df_m = df_m.to_frame()
    df_m['day'] = [i.day for i in df_m.index]
    days = df_m.day.unique()
    df_m['hour'] = [i.hour for i in df_m.index]
    hour = df_m.hour.unique()
    df_m_siang = df_m[df_m['hour'] < 12]
    hour_siang = df_m_siang.hour.unique()
    df_m_malam = df_m[df_m['hour'] >= 12]
    hour_malam = df_m_malam.hour.unique()
    
    # making grup data
    df_m = df_m.groupby(['day', 'hour']).mean()
    df_m_siang = df_m_siang.groupby(['day', 'hour']).mean()
    df_m_malam = df_m_malam.groupby(['day', 'hour']).mean()    
    df_m = df_m.unstack(level=0)
    df_m_siang = df_m_siang.unstack(level=0)
    df_m_malam = df_m_malam.unstack(level=0)
    
    # Generate grid
    X, Y = np.meshgrid(days, hour)
    X_siang, Y_siang = np.meshgrid(days, hour_siang)
    X_malam, Y_malam = np.meshgrid(days, hour_malam)
    
    # Make a plot a day
    fig, ax = plt.subplots(figsize=(12, 8))
    CS = ax.contourf(X, Y, df_m, cmap=warna[x])
    clb = fig.colorbar(CS)
    # clb.ax.set_xlabel('Days') #Abit too wide
    # clb.ax.set_title(str(i)) #legend title 
    ax.set_xlabel('Days')
    ax.set_ylabel('Hour')
    # ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
    plt.title(str(i)+' \n')
    plt.xticks(days)
    plt.yticks(hour)
    plt.savefig(str(i)+'.png',dpi=500,bbox_inches='tight')
    #plt.show()
    
    # Make a plot daytime
    fig, ax = plt.subplots(figsize=(12, 8))
    CS = ax.contourf(X_siang, Y_siang, df_m_siang, cmap=warna[x])
    clb = fig.colorbar(CS)
    # clb.ax.set_xlabel('Days') #Abit too wide
    # clb.ax.set_title(str(i)) #legend title 
    ax.set_xlabel('Days')
    ax.set_ylabel('Hour')
    # ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
    plt.title(str(i)+' Daytime \n')
    plt.xticks(days)
    plt.yticks(hour_siang)
    plt.savefig(str(i)+'_Daytime.png',dpi=500,bbox_inches='tight')
    
    # Make a plot nighttime
    fig, ax = plt.subplots(figsize=(12, 8))
    CS = ax.contourf(X_malam, Y_malam, df_m_malam, cmap=warna[x])
    clb = fig.colorbar(CS)
    # clb.ax.set_xlabel('Days') #Abit too wide
    # clb.ax.set_title(str(i)) #legend title 
    ax.set_xlabel('Days')
    ax.set_ylabel('Hour')
    # ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
    plt.title(str(i)+' Nighttime \n')
    plt.xticks(days)
    plt.yticks(hour_malam)
    plt.savefig(str(i)+'_Nighttime.png',dpi=500,bbox_inches='tight')
    