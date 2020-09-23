# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:21:55 2020

@author: Brent Kotzee
"""
import pandas as pd
import numpy as np
import re
from pandas.core.common import flatten
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from fucs import GETPMI,GetData, GetJobs, GetCum, GetPAI

def JustPMI(df,orginIN,destinationIN,timeIN,i,name):
    stop = 1
    
    while stop < 3:
        pmi = []
        Accs = []
        OriginToAll = []
        if stop == 1:        
            print(df)                
        timeIN=[timeIN[i]]   
        for j in range(len(timeIN)):
#            data= df.loc[(df["Name"].isin( [str(orginIN) + " - "+ str(destinationIN)] ))   & (df["Time"].isin([str(timeIN[j] ) ] ) )]
            data= df.loc[(df["Origin"].isin( [str(orginIN)])) & (df["Dest"].isin( [str(destinationIN)] ))   & (df["Time"].isin([str(timeIN[j] ) ] ) )]
            pmi.append(GETPMI(data["Shape_Leng"].values[0], data["Total_Trav"].values[0]))              
        Accs = Accs + GetData(orginIN, timeIN, destinationIN, df,name)
        Hour=[]
        for i in range(len(timeIN)):
            (h,m,s) = timeIN[i].split(':')
            Hour.append(int(h))
        stop = 3
        return Hour,pmi,Accs