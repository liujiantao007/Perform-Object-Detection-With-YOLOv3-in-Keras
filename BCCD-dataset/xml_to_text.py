#rahul pandit
import xml.etree.ElementTree as ET
import cv2
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os



labels={'RBC':0,'WBC':1}

label_path=os.getcwd()+'/Annotations/' #lable directory

DIRS = os.listdir(label_path)  #list of labels text


#(480,640,3) all image shape
#width=x=640
#height=y=480



def convert(coords):
	
	shape=[480,640]
	coords[2] -= coords[0] #width
	coords[3] -= coords[1] #height
	x_diff = int(coords[2]/2) #mid x
	y_diff = int(coords[3]/2) #mid y
	coords[0] = coords[0]+x_diff
	coords[1] = coords[1]+y_diff
	coords[0] /= int(shape[1]) #center x
	coords[1] /= int(shape[0]) #center y
	coords[2] /= int(shape[1]) #width
	coords[3] /= int(shape[0]) #height
	return coords



for DIR in DIRS:
	dict1={}
	dict1['xmin']=[]
	dict1['ymin']=[]
	dict1['xmax']=[]
	dict1['ymax']=[]
	dict1['label']=[]
	os.chdir("Annotations/")
	tree = ET.parse(DIR)
	for elem in tree.iter():
		if 'object' in elem.tag or 'part' in elem.tag:
			for attr in list(elem):
				if 'name' in attr.tag:
					name = attr.text
					dict1['label'].append(name)
				if 'bndbox' in attr.tag:
					for dim in list(attr):
						if 'xmin' in dim.tag:
							xmin = int(round(float(dim.text)))
							dict1['xmin'].append(xmin)
						if 'ymin' in dim.tag:
							ymin = int(round(float(dim.text)))
							dict1['ymin'].append(ymin)
						if 'xmax' in dim.tag:
							xmax = int(round(float(dim.text)))
							dict1['xmax'].append(xmax)
						if 'ymax' in dim.tag:
							ymax = int(round(float(dim.text)))
							dict1['ymax'].append(ymax)
	
	
	df=pd.DataFrame(dict1)
	df['label']=df['label'].apply(lambda x: labels[x])
	#print(df)
	
	#now convert all data to yolo fomrat
	
	dict2={}
	dict2['cell_type']=[]
	dict2['x']=[]#center x
	dict2['y']=[]#center y
	dict2['width']=[]
	dict2['height']=[]
	for i in range(0,df.shape[0]):
		data=np.array(df.iloc[i,:],dtype=np.float32)
		new_data=convert(data[:-1])
		#print(new_data)
		dict2['cell_type'].append(int(data[-1]))
		dict2['x'].append(new_data[0])
		dict2['y'].append(new_data[1])
		dict2['width'].append(new_data[2])
		dict2['height'].append(new_data[3])
	
	df1=pd.DataFrame(dict2)
	file_name=DIR.split('.')[0]
	os.chdir("..")
	path=os.getcwd()+'/JPEGImages/{}.txt'.format(file_name)
	df1.to_csv(path,sep=" ", encoding='utf-8', header=None,index=False)
	
	print("*******************{}********************".format(file_name))
	print("*******************************************")









