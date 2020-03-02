#coco dataset the bounding box are [top_left_x,top_y,w,h]

#convert coco dataset into yolo dataset

#make a folder img and put image inside it and also Label folder in img 

#run json_to_text.py in img folder it convert all json data into text in Label foler

#again run yolo_format.py it convert anotation into yolo format

#yolo always takes [label,center_x,center_y,w,h]
where label=0,1,2,3..... according class
