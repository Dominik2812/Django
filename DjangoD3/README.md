# Visualize Relationships in Django


![screen](pics/screen.png?raw=true "screen")

## Summary
A Django app that realizes "Drag and Drop" feature in combination with d3 visualization (https://d3js.org/). 
The app visualizes OneToMany and ManyToMany relationships of Data Base objects via d3 (Data Driven Documents). Via Drag and Drop objects can be deleted or viewed in detail. The objects are called "Bubbles" and consist of a core that can be considered as a category (such as "Sports") and a shell which consists of other "Bubbles" derive from the core (such as "running" or "juggling"). The "Bubbles" in the shell also have further relationships to other "Bubbles" and so on. 

The Relationship are either of type ManyToMany ("related") or of OneToMany ("children"). To define those relationships drag a bubble of your choice into the detail field (e.g.  "mousedown" on the field "Jakob" and "mouseup " on the detail field.

## Code Details 
In the following I will explain how the d3 visualization works and how drag and drop mechanisms can be applied. Django architecture and queries is kept as simple as possible and this will not be discussed. 


### Visualization of OneToMany and ManyToMany relatinoships via d3
To list all "Bubbles" in the "views.py" file the function "bubbles()" is called . The function "buildTree()" then retrieves all "Bubbles" from the Database and transforms all those objects, their children and related "Bubbles" into JSON format via the "listRecursive()" function. 
![views](pics/views.png?raw=true "views")

The JSON is then passed in the variable "family" to the "reservoir_link.html". This template has a three fold structure. The JSON is packed into "var myArr" via Javascript (part 1 in the image below). A <div> element with the id ="chart" (step 2) is needed to display the d3 visualisation, which still has to be created. The creation of the graphics is managed by part 3. There the first link enables your code to handle d3 elements in general. The second link is a link to the local "reservoir.js" that receives the JSON and converts it into graphics, which will be discussed in the next paragraph. The third link script part serves to change the "id=chart" to "id=full" after the graphics has been created and displayed. In this way several independant d3-graphics can be displaed on the same page, as it is necessary for the detail view, where besides the reservoir also a the "Bubble" of interest is displayed both with related "Bubbles" and children.
![template](pics/template.png?raw=true "template")
  
![script](pics/script.png?raw=true "script")


![dataflowDragDrop](pics/dataflowDragDrop.png?raw=true "dataflowDragDrop")



