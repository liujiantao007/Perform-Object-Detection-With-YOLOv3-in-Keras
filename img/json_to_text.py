#convert xml to text
#https://towardsdatascience.com/getting-started-with-bounding-box-regression-in-tensorflow-743e22d0ccb3
import json 
import csv 
import pandas as pd
import os

# Opening JSON file and loading the data 
# into the variable data 
with open('data.json') as json_file: 
	data = json.load(json_file) 

# *data keys all keys by iterable
keys=[*data]


for key in keys:
    dict1={}
    dict1['Damage']=[]
    dict1['x']=[]
    dict1['y']=[]
    dict1['width']=[]
    dict1['height']=[]
    
    #print(data[key])
    file_name=data[key]['filename']
    region_key=[*data[key]['regions']]
    for i in region_key:
        x=data[key]['regions'][i]['shape_attributes']['x']
        y=data[key]['regions'][i]['shape_attributes']['y']
        width=data[key]['regions'][i]['shape_attributes']['width']
        height=data[key]['regions'][i]['shape_attributes']['height']
        dict1['x'].append(x)
        dict1['y'].append(y)
        dict1['width'].append(width)
        dict1['height'].append(height)  
        dict1['Damage'].append(0)
    file_name=file_name.split('.')[0]
    df=pd.DataFrame(dict1)
    path=os.getcwd()+'/Label/{}.txt'.format(file_name)
    df.to_csv(path,sep=" ", encoding='utf-8', header=None,index=False)
        
    




















  

    