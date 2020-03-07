import pandas as pd

import os

os.chdir("JPEGImages/")

img1=[]

for i in range(0,411):
    if i<9:
        filename1="BloodImage_0000"+str(i)+".jpg"
        if filename1 in os.listdir(os.getcwd()):
            pass
        else:
            img1.append(i)
            print(i)
    elif i>9 and i<99:
       
        filename1="BloodImage_000"+str(i)+".jpg"
        if filename1 in os.listdir(os.getcwd()):
            pass
        else:
            print(i)
            img1.append(i)
            
    elif i>99 and i<410:
       
        filename1="BloodImage_00"+str(i)+".jpg"
        if filename1 in os.listdir(os.getcwd()):
            pass
        else:
            print(i)
            img1.append(i)
            
    
    












        
            
         