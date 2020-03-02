#convert xml to text
#https://towardsdatascience.com/getting-started-with-bounding-box-regression-in-tensorflow-743e22d0ccb3
import json 
import csv 
import pandas as pd
import os
import cv2
import numpy as np
from time import sleep

def convert(filename_str,coords):
    image = cv2.imread(filename_str)
    print(image.shape)
    #(480, 640, 3)
    #here already width and height are given
    x_diff = int(coords[2]/2) #mid x
    y_diff = int(coords[3]/2) #mid y
    coords[0] = coords[0]+x_diff #center c0
    coords[1] = coords[1]+y_diff #center c1
    print("x=",coords[0])
    print("y=",coords[1])
    coords[0] /= image.shape[1] 
    coords[1] /= image.shape[0]
    coords[2] /= image.shape[1]
    coords[3] /= image.shape[0]    
    return coords
   

label_path=os.getcwd()+'/Label/' #lable directory

DIRS = os.listdir(label_path)  #list of labels text

#now we take one by one text file and convert into anotation

for DIR in DIRS:
    dict1={}
    dict1['Damage']=[]
    dict1['x']=[]#center x
    dict1['y']=[]#center y
    dict1['width']=[]
    dict1['height']=[]
    #print("Currently in subdirectory:", DIR)
    df=pd.read_csv(label_path+DIR,sep=" ",header=None) #read text file in pandas
    for i in range(0,df.shape[0]):# iterate df and convert data in np.array
        data_array=np.array(df.iloc[i,:],dtype=np.float64)
        #seprate label
        label=data_array[0]
        data_array=data_array[1:]
        print("data=",data_array) 
        #call function and return new cordinate 
        file_name=DIR.split('.')[0]+'.jpg'
        #convert image name according to extension
        cor=convert(file_name,data_array)
        print(cor)
        dict1['Damage'].append(0)
        dict1['x'].append(cor[0])
        dict1['y'].append(cor[1])
        dict1['width'].append(cor[2])
        dict1['height'].append(cor[3])
    df=pd.DataFrame(dict1)
    df.to_csv(DIR,sep=" ", encoding='utf-8', header=None,index=False)
        
    
        #here i am sending cordinate
    print("end")
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



























  

    