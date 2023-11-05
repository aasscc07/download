import serial
import time 
from socket import socket,AF_INET,SOCK_STREAM


#board = pyfirmata.Arduino('/dev/ttyACM0')
#servo_pin = board.digital[9]
#it = pyfirmata.util.Iterator(board)
#it.start()

server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('192.168.20.12',9999))
#while True:
#    server_socket.listen(1)

#    print("Watting..")

   
#    client_socket,addr = server_socket.accept()

#    print("accept..")

#    client_socket.send(str(board.get_pin('a:0:i').read()).encode())

#    command = client_socket.recv(1024).decode()

#    if command == '1':
#        servo_pin.write(90)
#    elif command == '0':
#        client_socket.close()

#    client_socket.close()



arduino = serial.Serial(port='/dev/ttyACM0',baudrate=9600,timeout=1)

def read_from_arduino():
    data = arduino.readline().decode().rstrip()
    return data

def write_to_arduino(command):
    arduino.write(str(command).encode())


while True:
    server_socket.listen(1)
    print("Watting")

    client_socket,addr = server_socket.accept()

    print("accept...")

    sensor_value = read_from_arduino()
    
    if sensor_value:
        print("R")
    client_socket.send(str(sensor_value).encode())


    command = client_socket.recv(1024).decode()
    write_to_arduino(command)

    time.sleep(1)
