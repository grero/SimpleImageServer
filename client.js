webSocket = new WebSocket("ws://localhost:8765", "Protocol1");

webSocket.onmessage = (event) => {
   var url = event.data;
  const img = document.getElementById("image");
  f.src = url;
  
  console.log(event.data);
};
