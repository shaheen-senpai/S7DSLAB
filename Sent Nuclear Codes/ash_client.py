import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketAddress = ('172.18.109.20', 12345)



def listen():
    while True:
        message, address = s.recvfrom(1024)
        l = message.decode().split('^')
        if len(l) == 1:
            printToConsole(message.decode())
        else:
            printToConsole(l[1] + " : " + l[0])
            

def printToConsole(message):
    print("\n", message)

def handleInput():
    name = input("Enter you name:")
    s.sendto(name.encode(), socketAddress)

    while True:
        snd = input("Message: ")
        s.sendto(snd.encode(), socketAddress)

t1 = threading.Thread(target=listen)
t2 = threading.Thread(target=handleInput)


t1.start()
t2.start()

t1.join()
t2.join()

