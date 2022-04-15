let socket = new WebSocket("wss://" + window.location.hostname + ":1234/");
let ImageType = 'png'

socket.onopen = function(e) {
  document.onkeypress = function(e) {
     get = window.event?event:e;
     key = get.keyCode?get.keyCode:get.charCode;
     key = String.fromCharCode(key);
 
   socket.send("Key: " +key)
;}
  document.onmousemove = function(event) { 
    pointerX = event.pageX;
    pointerY = event.pageY;
    socket.send("X: " + pointerX);
    socket.send("Y: " + pointerY);
  };
};
  


socket.onmessage = function(event) {
  imageAsBase64 = event.data;
};


socket.onerror = function(error) {
  alert(`[error] ${error.message}`);
};

document.getElementById("ItemPreview").src = "data:image/" +ImageType+ ";base64," + imageAsBase64;

