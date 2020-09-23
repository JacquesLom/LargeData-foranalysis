# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:37:09 2020

@author: Brent Kotzee
"""

import pandas as pd
import numpy as np
import re
from pandas.core.common import flatten
import datetime
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from fucs import GETPMI,GetData, GetJobs, GetCum, GetPAI,GetAVA

def JustPai(df,orginIN,destinationIN,timeIN,i,name):
    stop = 1
    
    while stop < 3:
        pmi = []
        Accs = []
        OriginToAll = []
        AV=[]
        if stop == 1:        
            print(df)
        #--------------------------------------------------------------------------
        #Get input parameters to display
        if stop == 1:
            """
            print("Please type in the TAZ Origin:\n")
            print( sorted( list( dict.fromkeys( df["Origin"].tolist() ) ) ) )
            orginIN = input()
    
            print("Please type in the TAZ Destination:\n")
            print( sorted( list( dict.fromkeys( df["Dest"].tolist() ) ) ) )
            destinationIN = input()
            
            print("Please type in the TimeOfDay(hh:mm:ss):\n")
            print( sorted( list( dict.fromkeys( df["Time"].tolist() ) ) ) )
            timeIN = list(re.split('[,,\s]',(input("Enter a multiple value: "))))
            """

        """
        else:
            OrginQ = input("new orgin Type Y or N ?")
            destinationQ = input("new destination Type Y or N ?" )
            
            if (OrginQ == "Y") or (destinationQ == "Y") :
                        OriginToAll= []
                        print("Please type in the TAZ Origin:\n")
                        print( sorted( list( dict.fromkeys( df["Origin"].tolist() ) ) ) )
                        orginIN = input()
    
                        print("Please type in the TAZ Destination:\n")
                        print( sorted( list( dict.fromkeys( df["Dest"].tolist() ) ) ) )
                        destinationIN = input()
                        pmi = []#can prolly remove
                        Accs = []#can proly remove
                        timeIN = []
       
            print("Please type in the TimeOfDay(hh:mm:ss):\n")
            print( sorted( list( dict.fromkeys( df["Time"].tolist() ) ) ) )
            print("Do you want the entire day?")
            ans = input()
            if ans == "Y":
                #this can be replaced by the time list 
                timeIN = ['0:00:00','1:00:00','2:00:00','3:00:00','4:00:00','5:00:00','6:00:00','7:00:00','8:00:00','9:00:00','10:00:00','11:00:00','12:00:00','13:00:00','14:00:00','15:00:00','16:00:00','17:00:00','18:00:00','19:00:00','20:00:00','21:00:00','22:00:00','23:00:00']
            else:
                timeIN = timeIN + list(re.split('[,,\s]',(input("Enter a multiple value: "))))
                timeIN = list(dict.fromkeys(timeIN))
        """
        Accs = Accs + GetData(orginIN, timeIN[i], destinationIN, df,name)
        AV = AV + GetAVA(orginIN, timeIN[i], destinationIN, df)
        pai = GetPAI(orginIN, timeIN[i], destinationIN, df, name)
        Hour=[]
        (h,m,s) = timeIN[i].split(':')
        Hour.append(int(h))
        
        """
        fig = plt.figure()
        ax = mplot3d.Axes3D(fig)
        ax.set_xlim3d(0, max(pai))
        ax.set_ylim3d(0, max(Accs))
        ax.set_zlim3d(0, max(Hour))
        #ax.view_init(30, 360)
        ax.set_xlabel('Potential Mobiltiy Index ')
        ax.set_ylabel('Availabilty')
        ax.set_zlabel('Time')
        
        
        z_points = Hour
        x_points = pai
        y_points = Accs
        ax.scatter3D(x_points, y_points, z_points, c="black", cmap='hsv');
        ax.plot3D(x_points, y_points, z_points, c="black");
        
        plt.show()
        """
        print("DONE")
        
        stop = 3
        return pai,Accs,Hour,AV