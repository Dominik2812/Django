# Bucket: Brainstrom support app

## Summary
Brainstorm and rapidly prioritze or categorize your Thoughts by DjangoBucket. write your thought into the green field and press enter, create categories likewise in the violet field. Prioritize your unordered thought by dragging them into Category fields. Delete thoughts by dragging them into the "delete" field Delete categories by doubbleclick on the yellow field. 

![Categorize](pics/Categorize.png?raw=true "Categorize")

## Code Details

The project illustrates important interaction between the Django Database and Javascript events, that might be usefule for many other applications as well. We focuss here on the Javascript part; an example how data flows between Django Database, views and Javascript is illustrated in my DjangoD3 Project. 

### models.py 
Thoughts are represented by Item objects that can be linked to several Categories via ManyToMany relationships. 


![models](pics/models.png?raw=true "models")


### The Javascript CRUD2.js


![submit](pics/submit.png?raw=true "submit")

![DragDrop](pics/DragDrop.png?raw=true "DragDrop")

![delete](pics/delete.png?raw=true "delete")

![link](pics/link.png?raw=true "link")

![provide](pics/provide.png?raw=true "provide")






 




