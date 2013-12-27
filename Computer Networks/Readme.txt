

*******************************************************************************
* Instructions on how to compile and run program.                             *			                                                      *
* Name     : Sarvesh Sadhoo
                                                   *			                                      *
* Project  : Multithreaded Web Proxy Server  CSE5344 – Project 1 (Fall 2013)  *
 
* Date     : November 3,2013                                                  *  
*******************************************************************************

Project Specification:
----------------------

In this project,web proxy server is able to perform the following functionalities:

1. Receiving HTTP requests (GET and POST method) from a browser and forwarding them to
   the origin server.
2. Sending corresponding HTTP responses receiving from the origin server to the client.
3. Handle errors when a client requests an object which is not available.
4. Caching web pages each time the client makes a particular request for the first time and
   sending the cached web pages to the client when a cache hit occurs. 

Development Environment:
------------------------

Languages  	   : Python 2.7
Text Editor/IDE    : Note Pad ++ /PyCharm
Operating System   : Windows 7
Running Code	   : Command Prompt


Steps on how to compile and run program:
----------------------------------------

 1. Install or use Python 2.7 version.
 2. Open python file (sarvesh.py) in any text editor (Note Pad ++ or text Wrangler) to view the source code.
 3. To run the code open the command prompt and set the path where the python file is present.
 4. Give the command 'python sarvesh.py<space> <port number>. The program will start running in the cmd.
 5. Make sure Proxy server is ready to accept your request
 6. Open Chrome browser and enter the URL like localhost:<port number>/www.<website_name>.com.Eg: localhost:2000/www.google.com
 7. Website opens in the browser
 8. View the cmd to check the processing happening at the proxy server.


Project/Program Feaures:
------------------------

1. The program is able to succesfully Receiving HTTP requests (GET and POST method) from a browser and forwarding them to the origin server
2. The Program can handle errors
3. Multi threading has been implemented in the program. For each new reqiuest a new thread is created and that particular thread handles the request.
4. Cache has also been implemented in the program.


Specific Observations:
-----------------------

The following website where tested on the proxy web server. 

1. www.google.com
2. www.cnn.com
3. www.amazon.com
4. www.huffingtonpost.com
5. www.target.com
6. www.nytimes.com
7. www.foxnews.com
8. www.indeed.com
9. www.nbcnews.com
10. www.w3schools.com

Note: The above website were working fine with the server. The website were getting cached as well.

References:
-----------

1. Python BOOK: http://heather.cs.ucdavis.edu/~matloff/Python/PLN/FastLanePython.pdf: Introduction to Python
2. HTTP RESPONSE CODES: http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
3. PYTHON DoCS: http://docs.python.org/2/howto/sockets.html
4. Stackoverflow
5. TURORIAL POINTS WEBSITE: http://www.tutorialspoint.com/python/python_networking.htm


IMPORTANT NOTE:
---------------

While requesting certain websites you might not be able to view all the websites or you might see some error in the cmd. 
These error or issues arise due to the fact that we can not handle all the request while a website is accessed. Also these
issues don't crash the proxy server. You will be able to make new request for different websites. 