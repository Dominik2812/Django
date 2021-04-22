# Visualize Relationships in Django


![screen](pics/screen.png?raw=true "screen")

## Summary
A Django app that realizes "Drag and Drop" feature in combination with d3 visualization (https://d3js.org/). 
The app visualizes OneToMany and ManyToMany relationships of Data Base objects via d3 (Data Driven Documents). Via Drag and Drop objects can be deleted or viewed in detail. The objects are called "Bubbles" and consist of a core that can be considered as a category (such as "Sports") and a shell which consists of other "Bubbles" derive from the core (such as "running" or "juggling"). The "Bubbles" in the shell also have further relationships to other "Bubbles" and so on. 

The Relationship are either of type ManyToMany ("related") or of OneToMany ("children"). To define those relationships drag a bubble of your choice into the detail field (e.g.  "mousedown" on the field "Jakob" and "mouseup " on the detail field.

## Code Details 
In the following I will explain how the d3 visualization works and how drag and drop mechanisms can be applied. 


### Visualization via d3

![views](pics/views.png?raw=true "views")
![script](pics/script.png?raw=true "script")
![template](pics/template.png?raw=true "template")


![dataflowDragDrop](pics/dataflowDragDrop.png?raw=true "dataflowDragDrop")



