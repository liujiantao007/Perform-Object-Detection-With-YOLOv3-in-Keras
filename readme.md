
* The structure of the `BCCD_dataset`

  ```
  ├── BCCD
  │   ├── Annotations
  │   │       └── BloodImage_00XYZ.xml (364 items)
  │   ├── ImageSets       # Contain four Main/*.txt which split the dataset
  │   └── JPEGImages
  │   |   └── BloodImage_00XYZ.jpg (364 items)
      |
      |__xml_to_yolo_format.py
      
  ```````````````````````````
  * The structure of the `BCCD_dataset`
  
  ````````````````````````````````````````
  Json_to_yolo_format_data
  |
  |
  ├── img
  │   └── 1.jpg           # Some preprocess scripts for mxnet
      |
      |___Label
      |
      |___Json_to_text.py #A script to generate  .txt in Label folder
      |
      |___yolo_format.py  #create anotation file
 
  
  ```

* The  `JPEGImages`:

  * **Image Type** : *jpeg(JPEG)*
  * **Width** x **Height** : *640 x 480*

* The `Annotations` : The VOC format `.xml` for Object Detection, automatically generate by the label tools. Below is an example of `.xml` file.

  ```xml
  <annotation>
  	<folder>JPEGImages</folder>
  	<filename>BloodImage_00000.jpg</filename>
  	<path>/home/pi/detection_dataset/JPEGImages/BloodImage_00000.jpg</path>
  	<source>
  		<database>Unknown</database>
  	</source>
  	<size>
  		<width>640</width>
  		<height>480</height>
  		<depth>3</depth>
  	</size>
  	<segmented>0</segmented>
  	<object>
  		<name>WBC</name>
  		<pose>Unspecified</pose>
  		<truncated>0</truncated>
  		<difficult>0</difficult>
  		<bndbox>
  			<xmin>260</xmin>
  			<ymin>177</ymin>
  			<xmax>491</xmax>
  			<ymax>376</ymax>
  		</bndbox>
  	</object>
      ...
  	<object>
  		...
  	</object>
  </annotation>
  ```


