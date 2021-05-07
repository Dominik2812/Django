
//delete a bubble
const del_handler = e => {
    // by default elemtents cannot be dropped into other elements
    e.preventDefault(); 
    // get the current url and strip it to http://127.0.0.1:8000/
    completeUrl=String(window.location.href).substring(0,22)
    //then create the url that leads to DeleteView
    // g_Id stems from reservoir.js and is already waiting in the 
    //svg-element that represents the bubble
    new_path= completeUrl+'app/delete/bubble/'+String(g_Id);
    window.location.href=new_path
  }
del=document.querySelector("#delmeBubble")
del.addEventListener("mouseup", del_handler);


//see the single bubble details
const singleBubble_handler = e => {
    // by default elemtents cannot be dropped into other elements
    e.preventDefault(); 
    // create new url such as in the del_handler
    completeUrl=String(window.location.href).substring(0,22)
    new_path= completeUrl+'app/singleBubble/' + String(g_Id) ;
    window.location.href=new_path      
  }
  singleBubble=document.querySelector("#detail")
  singleBubble.addEventListener("mouseup", singleBubble_handler);
