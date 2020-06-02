const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
  document.getElementById("message").style.display = "none";
},6000);
