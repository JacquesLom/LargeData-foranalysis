# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:40:07 2020

@author: Jacques
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataJob = pd.read_csv('Jobs.csv', header ='infer')
dataJobHour = pd.read_csv('Jobs_Hours.csv', header ='infer')
Income = pd.read_csv('Income.csv', header ='infer')
popPerct = pd.read_csv('TAZ_Population_Percentage.csv', header ='infer')

#get the data stored using the orgin-destinationtime key to gettrav time and length to calculate the accesibilty value
#the function is given orgin value, time[list],destiniation value, dictionary created in the main, user inputed name
def GetData(origin, time, destination, df, name):
        acc = []    
        
        jobNum = dataJob.loc[(dataJob["TZ_2013"] == eval(destination)), name].values[0]
       
        for i in range(len(list(dict.fromkeys(time)))):

            #            data= df.loc[(df["Name"].isin( [str(origin) + " - "+ str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
            data= df.loc[(df["Origin"].isin( [str(origin)])) & (df["Dest"].isin( [str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
            jobHour = dataJobHour.loc[(dataJobHour["Operating_Time"].isin([str(time[i])]))]
            
            acc.append((jobHour[name].values[0])*jobNum * (data["Total_Trav"].values[0]))
        return acc
 
def GetaccC(origin, time, destination, df, name):#can prolly remove name
        accC = []         
        #jobHour = dataJobHour.loc[(dataJobHour["Operating_Time"].isin([str(time)]))]
        for i in range(len(list(dict.fromkeys(time)))):
            a = []
            for j in list(dict.fromkeys(list(dataJob["TZ_2013"]))):
                #data= df.loc[(df["Name"].isin( [str(origin) + " - "+ str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
                data= df.loc[(df["Origin"].isin( [str(origin)])) & (df["Dest"].isin( [str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
                datasub = data[ "Total_Trav" ].sum()
                jobHour = dataJobHour.loc[(dataJobHour["Operating_Time"].isin([str(time[i])]))]
                jobTotal = dataJob.loc[(dataJob["TZ_2013"].isin( [eval(destination)]))]
                jobNum = (jobHour[j].values[0]) * ((jobTotal[j].sum())) 
                jobNum = jobNum + jobNum * datasub
                a.append(jobNum)
            accC.append(sum(a))
            
        return accC        

#you dont just give the input you give the entire destination  and time  
def GetCum(time, destination, df, name, origin):
    cum = []    
    for i in range(len(time)):
#        data= df.loc[(df["Name"].isin( [str(origin) + " - "+ str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
        data= df.loc[(df["Origin"].isin( [str(origin)])) & (df["Dest"].isin( [str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
        datasub = data[ "Total_Trav" ].sum()
        jobHour = dataJobHour.loc[(dataJobHour["Operating_Time"].isin([str(time[i])]))]
        sub = dataJob.loc[(dataJob["TZ_2013"] != eval(origin))]
        jobNum =(sub[str(name)].sum())*(jobHour[name].values[0])
        jobNum= jobNum + jobNum * datasub
        cum.append(jobNum)
    return cum 


def GetAVA(origin, time, destination, df):
        AVA =[]
        for i in range(len(list(dict.fromkeys(time)))):
#            data= df.loc[(df["Name"].isin( [str(origin) + " - "+ str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
            data= df.loc[(df["Origin"].isin( [str(origin)])) & (df["Dest"].isin( [str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
            AVA.append((data[ "Total_Trav" ].values[0]))
        return AVA

def GetPAI(origin, time, destination, df, name):
        pai =[]
        jobNum = dataJob.loc[(dataJob["TZ_2013"] == eval(destination)), name].values[0]
        for i in range(len(list(dict.fromkeys(time)))):
#            data= df.loc[(df["Name"].isin( [str(origin) + " - "+ str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
            data= df.loc[(df["Origin"].isin( [str(origin)])) & (df["Dest"].isin( [str(destination)] ))   & (df["Time"].isin([str(time[i] ) ] ) )]
            jobHour = dataJobHour.loc[(dataJobHour["Operating_Time"].isin([str(time[i])]))]
            pai.append((jobHour[name].values[0])*jobNum * (data[ "Total_Trav" ].values[0]))
        return pai
    
def GETPMI(time, dist):
    
    return float(np.divide(dist/1000,(time/60)))    
    
def GetJobs():
    for col in dataJob.columns:
        print(col)
def Histo(origin):
    Income = pd.read_csv('income.csv', header ='infer')
    popPerct = pd.read_csv('TAZ_Population_Percentage.csv', header ='infer')
    inrow = Income.loc[Income["TZ_2013"].isin([origin])]
    poprow = popPerct.loc[popPerct["TZ2013"].isin([origin])]
    names = ["1st",'2nd',"3rd","4th"]
    inlist =[inrow["1st"].values[0], inrow["2nd"].values[0], inrow["3rd"].values[0], inrow["4th"].values[0]]
    plt.bar(x=names, height =inlist,color=['orange', 'green','blue','black'])
    plt.xlabel("Runs/Delivery")
    plt.ylabel("Frequency")
    plt.title('Champions Trophy 2017 Final\n Runs scored in 3 overs')
    plt.show()

    names = ["Black_African_%",'White_%','Coloured_%',"Indian_or_Asian_%","Other_%"]
    inlist =[poprow["Black_African_%"].values[0], poprow["White_%"].values[0], poprow["Indian_or_Asian_%"].values[0], poprow["Other_%"].values[0],poprow["Coloured_%"].values[0]]
    plt.bar(x=names, height =inlist,color=['orange', 'green','blue','black'])
    plt.xlabel("Runs/Delivery")
    plt.ylabel("Frequency")
    plt.title('Champions Trophy 2017 Final\n Runs scored in 3 overs')
    plt.show()
