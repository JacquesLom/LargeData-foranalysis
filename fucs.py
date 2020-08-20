# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:40:07 2020

@author: Jacques
"""

import pandas as pd
import numpy as np

dataJob = pd.read_csv('Jobs.csv', header ='infer')
#get the data stored using the orgin-destinationtime key to gettrav time and length to calculate the accesibilty value
#the function is given orgin value, time[list],destiniation value, dictionary created in the main, user inputed name
def GetData(origin, time, destination, df, name):
        acc = []    
        jobNum = dataJob.loc[(dataJob["TZ_2013"] == eval(destination)), name].values[0]
        for i in range(len(list(dict.fromkeys(time)))):
            data= df.loc[(df["Name"].isin( [str(origin) + " - "+ str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
            acc.append(jobNum * (1 / data["Total_Leng"].values[0]))
        return acc
    
#you dont just give the input you give the entire destination  and time  

def GetCum(time, destination, df, name, origin):
    cum = []
    
    for i in range(len(time)):
        data= df.loc[(df["Name"].isin( [str(origin) + " - "+ str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
        datasub = data[ "Total_Trav" ].sum()
        sub = dataJob.loc[(dataJob["TZ_2013"] != eval(origin))]
        jobNum =sub[str(name)].sum()
        jobNum= jobNum + jobNum * datasub
        cum.append(jobNum)
    return cum




def GetPAI(origin, time, destination, df, name):
        pai =[]
        jobNum = dataJob.loc[(dataJob["TZ_2013"] == eval(destination)), name].values[0]
        for i in range(len(list(dict.fromkeys(time)))):
            data= df.loc[(df["Name"].isin( [str(origin) + " - "+ str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
            pai.append(jobNum * (data[ "Total_Trav" ].values[0]))
        return pai
    
def GETPMI(time, dist):
    
    return float(np.divide(dist,time))    
    
def GetJobs():
    for col in dataJob.columns:
        print(col)