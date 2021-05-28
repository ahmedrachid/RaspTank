import socket
import move
import os
import info
import RPIservo

import functions
import robotLight
import switch
import socket
import robotLight
#websocket
import asyncio
import websockets
direction_command = 'no'
turn_command = 'no'

RL = robotLight.RobotLight()
RL.start()
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect(("192.168.1.1", 9000))
serv.send("register Ahmed".encode())

while True:
	data = serv.recv(2048)
	data = data.decode()
	print('Received:',data)
	if not data:
		break
	if 'register' not in data  and data != "already used":
		#currentSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#currentSocket.connect(("",10223))
		#print("Sending message {} to execute".format(data))
		#currentSocket.send(str(data).encode())
		#currentSocket.close()		
		if data == 'forward':			
			direction_command = 'forward'
			move.move(100, direction_command, 'no',  0.5)
		elif data == 'backward':
			direction_command = 'backward'
			move.move(100, direction_command, 'no', 0.5)
		elif data == 'right':
			turn_command = 'right'
			move.move(100, 'no', turn_command, 0.5)
		elif data == 'left':
			turn_command = 'left'
			move.move(100, 'no', turn_command, 0.5)
		elif data == 'stop':
			turn_command = 'no'
			direction_command = 'no'
			move.move(100, direction_command, turn_command, 0.5)
		elif 'speed' in data:
			move.move(int(data.split()[1]), direction_command, turn_command, 0.5)


		elif 'police' in data:
			RL.police()
			#tmp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			#tmp_socket.connect(('', 10223))
			#tmp_socket.send('police'.encode())
