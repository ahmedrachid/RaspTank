import keyboard
import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect(("192.168.1.1", 9000))
serv.send("connect Ahmed".encode())

stop = False
speed = 100

def onkeypress(event):
    global stop
    global speed
    if event.name == 'x':
        stop = True
    if event.name == 'w':
        print('You have pressed UP => Move FORWARD')
        serv.send("forward".encode())
    if event.name == 's':
        print('You have pressed BACKWARD => Move BACKWARD')
        serv.send("backward".encode())
    if event.name == 'd':
        print('You have pressed RIGHT => Move RIGHT')
        serv.send("right".encode())
    if event.name == 'a':
        print('You have pressed LEFT  => Move LEFT')
        serv.send("left".encode())
    if event.name == 'c':
        serv.send("stop".encode())
    if event.name == 'down':
        if speed <= 0:
            speed = 0
        else:
            speed = speed - 10
        msg = 'speed '+str(speed)
        serv.send(msg.encode())
    if event.name == 'up':
        if speed >= 100:
            speed = 100
        else:
            speed = speed + 10
        msg = 'speed ' + str(speed)
        serv.send(msg.encode())
    if event.name == 'l':
        msg = 'police'
        serv.send(msg.encode())
    if event.name == 'm':
        msg = 'malus'
        serv.send(msg.encode())
keyboard.on_press(onkeypress)

while True:
    try:
        if stop:
            print('EXIT !')
            break
    except:
        pass


#while True:
#    try:
#        if keyboard.is_pressed("z"):
#            print('You have pressed UP => Move FORWARD')
#            serv.send("forward".encode())
#        elif keyboard.is_pressed("s"):
#            print('You have pressed DOWN => Move BACKWARD')
#            serv.send("backward".encode())
#        elif keyboard.is_pressed("d"):
#            print('You have pressed RIGHT => Move RIGHT')
#            serv.send("right".encode())
#        elif keyboard.is_pressed("q"):
#            print('You have pressed LEFT => Move LEFT')
#            serv.send("left".encode())
#    except:
#        pass
