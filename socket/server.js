chrome.experimental.socket.create('tcp', '127.0.0.1', 8080, function(socketInfo) {
  chrome.experimental.socket.connect(socketInfo.socketId, function (result) {
        chrome.experimental.socket.write(socketInfo.socketId, "Hello, world!");         
    });
});

chrome.sockets.tcp.create({}, function(createInfo) {
  chrome.sockets.tcp.connect(createInfo.socketId,
    IP, PORT, onConnectedCallback);
});
chrome.sockets.tcp.send(socketId, arrayBuffer, onSentCallback);
