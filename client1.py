import socket

client1_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1_Socket.connect(("192.168.43.131", 12345))

def main():
    while True:

        print("want to send a messege:(s: send/ r:recieve or END : end)")
        choice = input()

        if(choice == 's'):
            client1_Socket.send(choice.encode('utf-8'))
            status = client1_Socket.recv(1024).decode('utf-8')
            if status == '0':                                           # server wants to send data from another client
                data = input('enter your messege: ')
                client1_Socket.sendall(data.encode('utf-8'))
            elif status == '2':                                         # server ready to accept data
                print('client 2 also want to send but prefering client 1 first:\n')
                client1_data = input('enter your msg:\n')
                client1_Socket.send(client1_data.encode('utf-8'))
                print('client 1 is sending:\n')
                data =client1_Socket.recv(1024).decode('utf-8')
                print(data)
            elif status == 'END':
                info = client1_Socket.recv(1024).decode('utf-8')
                print(info)
            else:
                print('There is some issue')
    
        elif choice == 'r':
            client1_Socket.send(choice.encode('utf-8'))
            status = client1_Socket.recv(1024).decode('utf-8')
            if status == '0':                                           # server is sending msg
                data = client1_Socket.recv(1024).decode('utf-8')
                print(data)
            elif status == '1':
                print('client 2 also wants to recieve, so send first:\n')
                client1_data = input()
                client1_Socket.send(client1_data.encode('utf-8'))

                print('client 2 is sending..\n')
                data = client1_Socket.recv(1024).decode('utf-8')
                print(data)
            elif status == 'END':
                info = client1_Socket.recv(1024).decode('utf-8')
                print(info)
            else:
                print('-1')

        elif choice == 'END':
            client1_Socket.send(choice.encode('utf-8'))
            print('socket is closing..')
            client1_Socket.close()

        else:
            print('Entered wrong choice:')

if __name__ == '__main__':
    main()