
function addCategory(e){
    if (e.type=='click' || e.keyCode === 13){
        document.getElementById('createCategoryForm').submit()
    } 
}

function addItem(e){
  if (e.type=='click' || e.keyCode === 13){
      document.getElementById('createItemForm').submit()
  } 
}


const dragstart_handler = e => {
    e.dataTransfer.setData("text/plain", e.target.id);
    console.log(e.target.id)
  }

const dragover_handler = e => {
  e.preventDefault();
}

const delCategory = e => {

  e.preventDefault();
  boxId=e.target.id
  CatId=boxId.substring(boxId.length-(boxId.length-7))
  completeUrl=String(window.location.href).substring(0,22)
  new_path= completeUrl+'bucket/delete/category/'+String(CatId);
  window.location.href=new_path

}

const delItem = e => {

  e.preventDefault();
  boxId = e.dataTransfer.getData("text/plain");

  ItemId=boxId.substring(boxId.length-(boxId.length-5))
  completeUrl=String(window.location.href).substring(0,22)
  new_path= completeUrl+'bucket/delete/item/'+String(ItemId);
  window.location.href=new_path

}

const uncouple = e => {

  e.preventDefault();
  x=e.target.id
  y=e.target.parentNode.id

  ItemId=x.substring(x.length-(x.length-5))
  CatId=y.substring(y.length-(y.length-7))

  console.log(ItemId, CatId)
  completeUrl=String(window.location.href).substring(0,22)
  new_path= completeUrl+'bucket/uncouple/item/'+String(ItemId)+ '/' + String(CatId);
  window.location.href=new_path

}
const linkCatItem = e => {
  e.preventDefault();
  boxId = e.dataTransfer.getData("text/plain");
  ItemId=boxId.substring(boxId.length-(boxId.length-5))
  CatId=e.target.id.substring(e.target.id.length-(e.target.id.length-7))
  console.log(boxId, ItemId, CatId, typeof boxId)
  completeUrl=String(window.location.href).substring(0,22)
  new_path= completeUrl+'bucket/link/'+String(CatId)+'/'+String(ItemId);
  window.location.href=new_path
}

window.addEventListener('DOMContentLoaded', () => {
  Array.from(document.querySelectorAll(".category")).forEach(
    category => {
      category.addEventListener("dragstart", dragstart_handler);
      category.addEventListener("dragover", dragover_handler);
      category.addEventListener("drop", linkCatItem);
      category.addEventListener("dblclick", delCategory)
    }
  );

  Array.from(document.querySelectorAll(".item")).forEach(
    item => {
      item.addEventListener("dragstart", dragstart_handler);
      item.addEventListener("dragover", dragover_handler);
      item.addEventListener("click", uncouple)

    }
  );
});

var textfieldCat = document.querySelector("#createCategoryText");
textfieldCat.addEventListener("keyup",addCategory);
textfieldCat.value=""; //Feld wieder leeren
textfieldCat.focus();

var textfieldItem = document.querySelector("#item");
textfieldItem.addEventListener("keyup",addItem);
textfieldItem.value=""; //Feld wieder leeren
textfieldItem.focus();


delEvent=document.querySelector("#trash")
delEvent.addEventListener("dragover", dragover_handler);
delEvent.addEventListener("drop", delItem);





