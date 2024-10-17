import socket

client2_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2_Socket.connect(("192.168.43.131", 12346))

def main():
    while True:

        print("want to send a messege:(s: send/ r:recieve)")
        choice = input()

        if(choice == 's'):
            client2_Socket.send(choice.encode('utf-8'))
            status = client2_Socket.recv(1024).decode('utf-8')
            if status == '0':                                           # server wants to send data from another client
                data = input('enter your messege: ')
                client2_Socket.sendall(data.encode('utf-8'))
            elif status == '2':                                         # server ready to accept data
                print("client 1 also want to send. preference is given to client 1:\n")
                data = client2_Socket.recv(1024).decode('utf-8')
                print(data)
                print("now you can send msg:\n")
                client2_data = input()
                client2_Socket.send(client2_data.encode('utf-8'))
            elif status == 'END':
                info =client2_Socket.recv(1024).deco('utf-8')
                print(info)
            else:
                print('There is some issue')
    
        elif choice == 'r':
            client2_Socket.send(choice.encode('utf-8'))
            status = client2_Socket.recv(1024).decode('utf-8')
            if status == '0':                                           # server is sending msg
                data = client2_Socket.recv(1024).decode('utf-8')
                print(data)
            elif status == '1':
                print("client 1 also wanted to recieve, but forced to send:\n")
                data = client2_Socket.recv(1024).decode('utf-8')
                print(data)
                print('Now client 1 is ready to recieve: enter your msg:')
                client2_data = input()
                client2_Socket.send(client2_data.encode('utf-8'))
            elif status == 'END':
                info =client2_Socket.recv(1024).deco('utf-8')
                print(info)
                exit
            else:
                print('-1')

        elif choice == 'END':
            client2_Socket.send(choice.encode('utf-8'))

            client2_Socket.send(choice.encode('utf-8'))
            client2_Socket.close()
        else:
            print('Entered wrong choice:')

if __name__ == '__main__':
    main()