# SimplerImageServer

 This is just a proof-of-concept of how to have a server initiate a change in the image displayed on a web page
using WebSockets

## Usage

First start the server

```bash
python server.py
```

This will load any *.png or *.jpg images found in the current working directory and serve each one randomly every 1 second.

Then, in a web browser open the file `index.html`. You should see the image updated every 1 second.


