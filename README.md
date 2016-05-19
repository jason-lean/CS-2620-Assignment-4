## CS:2620 Assignment 4

>The goal of this assignment is to develop a proxy server with simple caching. Client can request web pages via the proxy
server. A request from a client includes a hostname (e.g. www.uiowa.edu) and a port number (typically 80). Once a
request is received by the server, it first checks if the response is already present in the cache. A cache entry has a lifetime
of 1 minute and the entry is considered to be stale once the lifetime is exceeded. If server finds the response in cache that
is not stale, server simply responds client with the entry from cache. The server, otherwise, sends a HTTP GET request to
the host specified and stores/updates the response in cache, the server then replies the client with the response.

#### Requirements

> In this assignment, you will write both client and proxy. The client will send HTTP GET requests to multiple web servers
via the proxy server. The client program connects to the proxy and sends HTTP GET requests for the following 3 websites
with an interval of 30 seconds. 

> At the client, once the response is received from the proxy server, send the exact same HTTP GET request directly to the
web server. Check whether the content (excluding header) received from the proxy server matches with the content
received from direct request. Output the hostnames for which the contents match and do not match. 

> In short, things to do:

> 1. Proxy server, which receives HTTP GET requests and responds with content from cache (with 1 minute stale
interval) or fetches it from web server
2. Client, which requests www.uiowa.edu, www.google.com, and www.yahoo.com with 30 seconds gap -- and
verifies the response from proxy server. 

#### What's included:

- `server.py`: server code that processes GET requests and sends response for verification
- `client.py`: client code that sends GET requests and verifies server response

