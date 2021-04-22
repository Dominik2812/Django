# Bucket: Brainstrom support app


![screen](pics/screen.png?raw=true "screen")

## Summary
A Django 

## Code Details 
In the following I will explain how the d3 visualization works and how drag and drop mechanisms can be applied. Django architecture and queries is kept as simple as possible and this will not be discussed. 


### Visualization of OneToMany and ManyToMany relatinoships via d3
To list all "Bubbles" in the "views.py" file the function "bubbles()" is called . The function "buildTree()" then retrieves all "Bubbles" from the Database and transforms all those objects, their children and related "Bubbles" into JSON format via the "listRecursive()" function. 

![Categorize](pics/Categorize.png?raw=true "Categorize")

The JSON is then passed in the variable "family" to the "reservoir_link.html". This template has a three fold structure. The JSON is packed into "var myArr" via Javascript (part 1 in the image below). A "div" element with the id ="chart" (step 2) is needed to display the d3 visualisation, which still has to be created. The creation of the graphics is managed by part 3. There the first link enables your code to handle d3 elements in general. The second link is a link to the local "reservoir.js" that receives the JSON and converts it into graphics, which will be discussed in the next paragraph. The third link script part serves to change the "id=chart" to "id=full" after the graphics has been created and displayed. In this way several independant d3-graphics can be displaed on the same page, as it is necessary for the detail view, where besides the reservoir also a the "Bubble" of interest is displayed both with related "Bubbles" and children.
  
  
  
![Brainstorm_INtoBucket](pics/Brainstorm_INtoBucket.png?raw=true "Brainstorm_INtoBucket")



In the "reservoir.js" the JSON is read by teh function getData() and passed into a forloop that takes care of the visualization but also of the "events" that are attached to each "Bubble", that is represented as a "g" element in the html part. The event of interest is the drag and drop event. In the following image the 3rd section shows the "mousedown" event by which the drag and drop is initiated. 



### Drag and Drop of "Bubbles":
The mousedown event shown in the previous image transforms the id of a "g" element into an object id which is then packed into "g_Id". Thi in turn is then passeed to the "dump.js" where it is then integrated into a URL . The URL is then passed to the AppUrls.py which calls in this case a CBV (class Based View) in the views.py.
 




