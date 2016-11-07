function func(tagname){
 var obj = document.getElementById(tagname);
 if(obj.style.display==""){
  obj.style.display = "none";
 }else{
  obj.style.display = "";
 }
}
