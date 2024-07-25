webSocket = new WebSocket(url, protocols);


webSocket.onmessage = (event) => {
   var url = event.data;
  const img = document.getElementById("image");
  f.href = url;
  
  console.log(event.data);
};
