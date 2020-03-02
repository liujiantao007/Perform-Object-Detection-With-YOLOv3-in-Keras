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
"""    



start_point = (216,359) 

# Ending coordinate, here (220, 220) 
# represents the bottom right corner of rectangle 
end_point = (316,464) 

# Blue color in BGR 
color = (255, 0, 0) 

# Line thickness of 2 px 
thickness = 2

# Using cv2.rectangle() method 
# Draw a rectangle with blue line borders of thickness of 2 px 
image = cv2.rectangle(image, start_point, end_point, color, thickness) 


cv2.imwrite('r.jpg',image)
# Displaying the image 
plt.imshow(image) 
