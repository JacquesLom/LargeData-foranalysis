# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 00:20:51 2020

@author: Jacques
"""
import pandas as pd

dataJob = pd.read_csv('Jobs.csv', header ='infer')
print("Please type in the Transport(BUS;Metro;MyCiti;Taxi):\n")
Transport = input( )
print("Please type in the day(Tuesday;Wednesday;Thursday):\n")
Day = input( )
#date =input("Pleaseinput the date for the day(dd/mm/yyyy like so 1/4/1900) \n")
df = pd.read_csv( Transport+"_"+Day+'.txt',sep=",")

OandD= df["Name"].str.split(" - ", n = 1, expand = True)
df["Origin"]=OandD[0]
df["Dest"]=OandD[1] 

time = df["TimeOfDay"].str.split(" ", n = 1, expand = True)
df["Time"] =time[1]


time = list( dict.fromkeys( df["Time"].tolist() ))
for i in range(len(time)):
    Newdf =  df.loc[ df["Time"].isin([str(time[i] ) ] ) ]
    Newdf.drop(columns=['OID', 'OID_','OriginID', 'Destinatio', 'Destinat_1', 'TimeOfDay'])
    del Newdf["OID"]
    del Newdf[ "OID_"]
    del Newdf['OriginID'] 
    del Newdf['Destinatio'] 
    del Newdf['Destinat_1'] 
    del Newdf["TimeOfDay"]
    Newdf.to_csv(Transport+"_"+Day+"_"+str(time[i])[0]+".txt", header=True, index=False, sep=';', mode='a') 
    
    