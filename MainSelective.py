# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:38:21 2020

@author: Brent Kotzee
"""

import pandas as pd
import numpy as np
from PMI import PMI
from JUSTPMI import JustPMI
from JUSTPAI import JustPai
from BOTH import both
from fucs import GETPMI,GetData, GetJobs, GetCum, GetPAI,GetAVA,Histo
#will be used with the loops 
outter= 1
#going to be the constant data outside of the loop segment
#now plot parameter with time,availablity and accessibilty as the axis
from mpl_toolkits import mplot3d
#import numpy as np
import matplotlib.pyplot as plt
"""
times = input("The hours you want to anal:\n")
if ("," in times):
    times =times.split(",")
print("Please type in the Transport(BUS;Metro;MyCiti;Taxi):\n")
Transport = input( )
print("Please type in the day(Tuesday;Wednesday;Thursday):\n")
Day = input( )

df = pd.DataFrame()
for i in range(len(times)):
    dfinter = pd.ExcelFile( Transport+"_"+Day+"_"+str(times[i])[0]+'.xlsx').parse( 'Sheet1' )
    if i==0:
        df = dfinter
    else:
        df.append(dfinter)
#dataJob = pd.read_csv('Jobs.csv', header ='infer')
#date =input("Pleaseinput the date for the day(dd/mm/yyyy like so 1/4/1900) \n")
"""
"""
OandD= df["Name"].str.split(" - ", n = 1, expand = True)
df["Origin"]=OandD[0]
df["Dest"]=OandD[1] 

time = df["TimeOfDay"].str.split(" ", n = 1, expand = True)
df["Time"] =time[1]
"""
Hour = []
OriginToAll = []
asscum = []
Accs = []
AV =[]
pai = []
pmi = []
AccC=[]
#timeIN = [0:00:00,1:00:00,2:00:00,3:00:00,4:00:00,5:00:00,6:00:00,7:00:00,8:00:00,9:00:00,10:00:00,11:00:00,12:00:00,13:00:00,14:00:00,15:00:00,16:00:00,17:00:00,18:00:00,19:00:00,20:00:00,21:00:00,22:00:00,23:00:00]
timeIN=""
orginIN=""
destinationIN=""
while outter < 3:
    timeIN = input("The hours you want to anal:\n")
    if ("," in timeIN):
        timeIN =timeIN.split(",")
    else:
        timeIN =[timeIN]
    print("Please type in the Transport(BUS;Metro;MyCiti;Taxi):\n")
    Transport = input( )
    print("Please type in the day(Tuesday;Wednesday;Thursday):\n")
    Day = input( )
    opt = eval(input("You want to do a full anal(1), PMI(2), PAI(3) or PMI and PAI(No cum)(4)""\n"))
    
    for i in range(len(timeIN)):

        (h,m,s) = timeIN[i].split(':')
        Hour.append(int(h))
            
        df = pd.read_csv( Transport+"_"+Day+"_"+str(Hour[i])+'.txt',sep=";")
        if i ==0:
            print("Please select the type of Opportunity in the TAZ Destination:\n")
            GetJobs()
            name = input()
            print("Please type in the TAZ Origin:\n")
            print( sorted( list( dict.fromkeys( df["Origin"].tolist() ) ) ) )
            orginIN = input()
            Histo(orginIN)
    
            print("Please type in the TAZ Destination:\n")
            print( sorted( list( dict.fromkeys( df["Dest"].tolist() ) ) ) )
            destinationIN = input()
            while  sorted( list( dict.fromkeys( df["Dest"].tolist() ) ) ).count(eval(destinationIN)) == 0 :
                print("TAZ Destination was not in the list:\n")
                print("Please type in the TAZ Destination:\n")
                destinationIN = input()
                
        if opt ==2:
            print("Please select the type of Opportunity in the TAZ Destination:\n")
            GetJobs()
            name = input()
            Histo(orginIN)
        if opt == 1:            
            Hour1,OriginToAll1,asscum1,Accs1, pai1, pmi1,AccC1,AV1=PMI(df,orginIN,destinationIN,timeIN,i,name)
        elif opt ==2:
            Hour1,pmi1,Accs1 = JustPMI(df,orginIN,destinationIN,timeIN,i,name)
        elif opt==3:
             pai1,Accs1,Hour1 =JustPai(df,orginIN,destinationIN,timeIN,i,name)
        elif opt ==4:
            Hour1,pai1,Accs1,pmi1= both(df,orginIN,destinationIN,timeIN,i,name)
        
        
        OriginToAll = OriginToAll+OriginToAll1
        asscum = asscum + asscum1
        Accs = Accs + Accs1
        AccC = AccC + AccC1
        AV= AV + AV1
        pai = pai + pai1
        pmi = pmi + pmi1
    
    if opt == 1:
        print ("PAI vs PMI\n")
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.set_xlim3d(0, max(pmi))
        ax.set_ylim3d(0, max(Accs))
        ax.set_zlim3d(0, max(Hour))
        #ax.view_init(30, 360)
        ax.set_xlabel('Potential Mobiltiy Index ')
        ax.set_ylabel('Accessibility')
        ax.set_zlabel('Time(h)')
        
        
        z_points = Hour
        x_points = pmi
        y_points = Accs
        ax.scatter3D(x_points, y_points, z_points, c="black", cmap='hsv');
        ax.plot3D(x_points, y_points, z_points, c="black");
        
        plt.show()
        
        print(np.array([[round(num, 2) for num in pmi],[round(num) for num in pai],timeIN]).T)
        
        
        print ("PAI vs Availability\n")
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.set_xlim3d(0, max(pai))
        ax.set_ylim3d(0, max(AV))
        ax.set_zlim3d(0, max(Hour))
        #ax.view_init(30, 360)
        ax.set_xlabel('Potential Accessibility Index ')
        ax.set_ylabel('Availabilty(min)')
        ax.set_zlabel('Time(h)')
        
        
        z_points = Hour
        x_points = pai
        y_points = AV
        ax.scatter3D(x_points, y_points, z_points, c="black", cmap='hsv');
        ax.plot3D(x_points, y_points, z_points, c="black");
        
        plt.show()

        print(np.array([pai,AV,timeIN]).T)


        print ("Cumulative PAI vs PMI\n")
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.set_xlim3d(0, max(pmi))
        ax.set_ylim3d(0, max(AccC))
        ax.set_zlim3d(0, max(Hour))
        #ax.view_init(30, 360)
        ax.set_xlabel('Potential Mobiltiy Index')
        ax.set_ylabel('Accessibility Cumulitive')
        ax.set_zlabel('Time(h)')
        
        
        z_points = Hour
        x_points = OriginToAll
        y_points = AccC
        ax.scatter3D(x_points, y_points, z_points, c="black", cmap='hsv');
        ax.plot3D(x_points, y_points, z_points, c="black");
        
        plt.show()

        print(np.array([pmi,AccC,timeIN]).T)

        print("DONE")
    elif opt ==2:
        print ("pmi\n")
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.set_xlim3d(0, max(pmi))
        ax.set_ylim3d(0, max(Accs))
        ax.set_zlim3d(0, max(Hour))
        #ax.view_init(30, 360)
        ax.set_xlabel('Potential Mobiltiy Index ')
        ax.set_ylabel('Availabilty')
        ax.set_zlabel('Time(h)')
        
        
        z_points = Hour
        x_points = pmi
        y_points = Accs
        ax.scatter3D(x_points, y_points, z_points, c="black", cmap='hsv');
        ax.plot3D(x_points, y_points, z_points, c="black");
        
        plt.show()
    elif opt==3:
        print ("pai\n")
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.set_xlim3d(0, max(pai))
        ax.set_ylim3d(0, max(Accs))
        ax.set_zlim3d(0, max(Hour))
        #ax.view_init(30, 360)
        ax.set_xlabel('Potential Mobiltiy Index ')
        ax.set_ylabel('Availabilty')
        ax.set_zlabel('Time(h)')
        
        
        z_points = Hour
        x_points = pai
        y_points = Accs
        ax.scatter3D(x_points, y_points, z_points, c="black", cmap='hsv');
        ax.plot3D(x_points, y_points, z_points, c="black");
        
        plt.show()
    elif opt ==4:
        print ("pmi\n")
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.set_xlim3d(0, max(pmi))
        ax.set_ylim3d(0, max(Accs))
        ax.set_zlim3d(0, max(Hour))
        #ax.view_init(30, 360)
        ax.set_xlabel('Potential Mobiltiy Index ')
        ax.set_ylabel('Availabilty')
        ax.set_zlabel('Time(h)')
        
        
        z_points = Hour
        x_points = pmi
        y_points = Accs
        ax.scatter3D(x_points, y_points, z_points, c="black", cmap='hsv');
        ax.plot3D(x_points, y_points, z_points, c="black");
        
        plt.show()
        print ("pai\n")
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.set_xlim3d(0, max(pai))
        ax.set_ylim3d(0, max(Accs))
        ax.set_zlim3d(0, max(Hour))
        #ax.view_init(30, 360)
        ax.set_xlabel('Potential Mobiltiy Index ')
        ax.set_ylabel('Availabilty')
        ax.set_zlabel('Time(h)')
        
        
        z_points = Hour
        x_points = pai
        y_points = Accs
        ax.scatter3D(x_points, y_points, z_points, c="black", cmap='hsv');
        ax.plot3D(x_points, y_points, z_points, c="black");
        
        plt.show()
        Histo(destinationIN)
   
    outter = eval(input("You want to redo (1) or you want to stop(3), different ervice(2)""\n"))
