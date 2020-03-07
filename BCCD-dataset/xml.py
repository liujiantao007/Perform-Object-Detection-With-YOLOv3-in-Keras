import pandas as pd

import os



os.chdir("../Annotations/")


xml1=[]

for i in range(0,411):
    if i<9:
        filename1="BloodImage_0000"+str(i)+".xml"
        if filename1 in os.listdir(os.getcwd()):
            pass
        else:
            print(i)
            xml1.append(i)
    elif i>9 and i<99:
       
        filename1="BloodImage_000"+str(i)+".xml"
        if filename1 in os.listdir(os.getcwd()):
            pass
        else:
            print(i)
            xml1.append(i)
            
    elif i>99 and i<410:
       
        filename1="BloodImage_00"+str(i)+".xml"
        if filename1 in os.listdir(os.getcwd()):
            pass
        else:
            print(i)
            xml1.append(i)
            
    
           
            
            
            
            
            
            
            
            
            
         