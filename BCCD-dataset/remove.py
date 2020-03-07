
xml1
img1



import os



os.chdir("../JPEGImages/")


for i in xml1:
    if i<99 and i>9:
        print("i<90",i)
        try: 
            filename1="BloodImage_000"+str(i)+".jpg"
            os.remove(filename1)
        except: pass

    elif i>99:  
        try: 
            filename1="BloodImage_00"+str(i)+".jpg"
            os.remove(filename1)
        except: pass
        print("i>90",i)
       
        
os.chdir("../Annotations/")


for i in img1:
    if i<99 and i>9:
        print("i<90",i)
        try: 
            filename1="BloodImage_000"+str(i)+".txt"
            os.remove(filename1)
        except: pass

    elif i>99:  
        try: 
            filename1="BloodImage_00"+str(i)+".txt"
            os.remove(filename1)
        except: pass
        print("i>90",i)
     
        
        
         
        
  