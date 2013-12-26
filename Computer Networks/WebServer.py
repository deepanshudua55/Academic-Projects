# Imports all the Python libraries used in the below program!
import sys
import socket
import httplib
import threading

# handle_requests deals with checking the file cache, creating new cache file and sending the response back to client! 
def handle_request(clientSocket, threadName):
	message = clientSocket.recv(12000) #Receives data from the socket!
	messageParts = message.split()
	if len(messageParts) < 1:
		print "The message from one of the request is empty"
		print 'Server Is Ready and waiting for a new request'
		clientSocket.send("HTTP/1.0 404 NOT_FOUND\r\n") 
		clientSocket.close()
		return
	# Extracts the domain name from the message received!
	filename = message.split()[1].partition("/")[2] 
	filename = "/" + filename
	
	#Checks, reads and sends the file if present in cache!
	try:
		fileToOpen = filename[1:].replace("/", "_"); # Tries to open the cache file if already present!
		fo = open(fileToOpen, "rb") # Tries to read the file in binary mode as file may contain images which can only be read in binary mode!
		data = fo.read()
		print "Send from cache"
		clientSocket.send("HTTP/1.0 200 OK\r\n") # Proxy server sends a standard response for successful HTTP requests!
		clientSocket.send("Content-Type:text/html\r\n") # The content send by the proxy server is an Internet Media Type content which is readable by browser! 
		clientSocket.send("Connection: close\r\n") # Signals the client that the connection will be closed after the completion of response!
		clientSocket.send("\r\n") #Gives a line break between the response message and the actual data to be send to the client!
		clientSocket.send(str(data)) # Typecast the data into sting format.
		fo.close() # Closes the cache file!
		
	#The file is not present in cache. Reads from remote server and creates a new cache file!
	except IOError:
		
		print "File not found in cache"
		try:
			print "Getting from remote host"
			httpRequestType = messageParts[0] # Extracts the type of Request. GET OR POST!
			httpRequestPath = messageParts[1] # Extracts the path of the request. Like /google.com!
			httpRequestPath = httpRequestPath[1:] # Removes leading / from the httpRequestPath
			
			httpRequestServer = httpRequestPath.partition("/")[0]
			httpRequestParameters = "/"+httpRequestPath.partition("/")[2]
	
			conn = httplib.HTTPConnection(httpRequestServer); # Creates a single transaction connection with the HTTP Server!
			
			# Checks if request type is POST OR GET!
			if httpRequestType.lower() == "post":
				messageData = message.split("\r\n\r\n")[1]
				conn.request(httpRequestType, httpRequestParameters, messageData)
			else :
				conn.request(httpRequestType, httpRequestParameters)
				
			# Gets the response from the remote server and stores it in a variable named "response"!
			response = conn.getresponse()

			# Check for a successful response from the server. If such a response not found i.e 3XX, 4XX or 5XX is found then return that particular
			# response message!
			if response.status != 200:
				clientSocket.send("HTTP/1.0 200 OK\r\n") 
				clientSocket.send("Content-Type:text/html\r\n")
				clientSocket.send("Connection: close\r\n")
				clientSocket.send("\r\n")
				clientSocket.send("<html><body>Status Code was not 200. Redirects and Errors are currently not supported</body></html>")
				clientSocket.close()
				return 
				
			data = response.read()
			
			# converting relative paths to absolute paths
			data = data.replace("href=\"/", "href=\""+httpRequestServer+"/")
			data = data.replace("src=\"/", "src=\""+httpRequestServer+"/")
			data = data.replace("url(/", "url("+httpRequestServer+"/")
			
			# Creates a new cache file and starts writing into it!
			f = open(filename[1:].replace("/","_"), "w") # Opens the file in write only mode!
			f.write(data) # Writes the data!
			f.close() # Closes the file! 
			clientSocket.send("HTTP/1.0 200 OK\r\n") #Proxy server sends a standard response for successful HTTP requests!
			clientSocket.send("Content-Type:text/html\r\n") #The content send by the proxy server is an Internet Media Type content which is readable by humans!
			clientSocket.send("Connection: close\r\n")#Signals the client that the connection will be closed after the completion of response!
			clientSocket.send("\r\n") #Gives a space between the response message and the actually data to be send to the client!
			clientSocket.send(data)
		#Handles error for any other kind of exception like
		except Exception as e:
			clientSocket.send("HTTP/1.0 404 NOT_FOUND\r\n") 
			clientSocket.send("Connection: close\r\n")
	clientSocket.close() # Closes the client socket!

# Checks while running the program if the an argument(port number) is passed or not. Exit if the there are no arguments passed!
if len(sys.argv) <= 1: 
    print 'Usage: "python S.py port"\n[port : It is the port of the Proxy Server]'
    sys.exit(2)

# Create a server socket, bind it to a port and start listening!
tcpSerPort = int(sys.argv[1]) # sys.argv[1] is the port number entered by the user!
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print "Server is getting started" # Prepare a server socket!
tcpSerSock.bind(('', tcpSerPort))
tcpSerSock.listen(5)

# For threading purpose(counter)!
threadCount = 1

while 1 :
	# Start receiving data from the client
	print 'Server Is Ready and waiting for a new request'
	tcpCliSock, addr = tcpSerSock.accept() # Accept a connection from client
	print "Got a request"
	threadName = "Thread Number:",threadCount
	print "Request handled by:", threadName
	#create new thread and pass the client socket to it
	t = threading.Thread(target=handle_request, args = (tcpCliSock, threadName)) # Creates a new thread for every new request!
	t.daemon = True
	t.start() # Starts the thread!
	threadCount = threadCount + 1