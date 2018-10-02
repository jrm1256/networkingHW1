# Justin Mosier
# Progrmming Assignment 1
# CSC 4350 
# Date: 9/28/18

# Set up server socket

from socket import *

serverPort = 7000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('',serverPort))
serverSocket.listen(5)


while True:

	print('Ready to serve...')
	
	# Set up connection socket
	connectionSocket, addr = serverSocket.accept()

	try:
		
		# Get file name and open file
		message = connectionSocket.recv(1024)
		filename = message.split()[1]

		f = open(filename[1:])
		
		#Read information and send data
		outputdata = f.read()
		sentence = 'HTTP/1.1 200 OK\r\n\r\n'
		
		connectionSocket.send(sentence.encode())
		connectionSocket.send(outputdata.encode())

		connectionSocket.close()

	except IOError:
		
		errorSentence = 'HTTP/1.1 404 Not Found\r\n\r\n'
		connectionSocket.send(errorSentence.encode())
		
		connectionSocket.close()
		
		
serverSocket.close()
