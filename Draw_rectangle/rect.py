# Python program to explain cv2.rectangle() method 

# importing cv2 
import cv2 
from matplotlib import pyplot as plt



path ='2.jpg'

# Reading an image in default mode 
image = cv2.imread(path) 

# Window name in which image is displayed 
window_name = 'Image'

# Start coordinate, here (5, 5) 
# represents the top left corner of rectangle

"""
<bndbox>
<xmin>216</xmin>
<ymin>359</ymin>
<xmax>316</xmax>
<ymax>464</ymax>
</bndbox>

<bndbox>
<xmin>77</xmin>
<ymin>326</ymin>
<xmax>177</xmax>
<ymax>431</ymax>
</bndbox>

<bndbox>
<xmin>540</xmin>
<ymin>353</ymin>
<xmax>640</xmax>
<ymax>458</ymax>
</bndbox>


<bndbox>
<xmin>405</xmin>
<ymin>350</ymin>
<xmax>513</xmax>
<ymax>457</ymax>
</bndbox>

"""



start_point = (216,359) 

# Ending coordinate, here (220, 220) 
# represents the bottom right corner of rectangle 
end_point = (316,464) 


start_point1 = (77,326) 
end_point1 = (177,431) 


start_point2 = (77,326) 
end_point2 = (177,431) 


start_point3 = (540,353) 
end_point3= (640,458) 

start_point4 = (405,350) 
end_point4= (513,457) 



# Blue color in BGR 
color = (255, 0, 0) 

# Line thickness of 2 px 
thickness = 2

# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness) 

image=cv2.rectangle(image, start_point1, end_point1, color, thickness)

image=cv2.rectangle(image, start_point2, end_point2, color, thickness)
image=cv2.rectangle(image, start_point3, end_point3, color, thickness)
image=cv2.rectangle(image, start_point4, end_point4, color, thickness)



cv2.imwrite('r.jpg',image)
# Displaying the image 
plt.imshow(image) 
