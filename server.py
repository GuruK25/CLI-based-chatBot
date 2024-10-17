import socket

def createSocket(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(2)
    return s


def main():
    ip = "192.168.43.131"
    port1 = 12345
    port2 = 12346

    serverSocket1 = createSocket(ip, port1);
    serverSocket2 = createSocket(ip, port2);
    print("server is ready to connect:")

    client1_socket, addr1 = serverSocket1.accept();
    print(f"client 1 is connected from {addr1}")

    client2_socket, addr2 = serverSocket2.accept();
    print(f"client 2 is connected fron {addr2}")

    while True:
       
        client1_choice = client1_socket.recv(1024).decode('utf-8')
        client2_choice = client2_socket.recv(1024).decode('utf-8')

        if client1_choice == 's' and client2_choice == 'r':                      # client 1 send, client 2 recv
            n = '0'
            client1_socket.send(n.encode('utf-8'))
            client2_socket.send(n.encode('utf-8'))
            client1_data = client1_socket.recv(1024).decode('utf-8')           #recieving dmsg frm client 1
            print('data recieved from client 1.')
            client2_socket.send(client1_data.encode('utf-8'))                  # sending to client 2
            print('data sent to client 2.')


        elif client1_choice == 'r' and client2_choice == 's':                   # client1 rcv , client 2 send
            n = '0';
            client1_socket.send(n.encode('utf-8'))
            client2_socket.send(n.encode('utf-8'))
            client2_data = client2_socket.recv(1024).decode('utf-8')
            print('data recieved from client 2.')
            client1_socket.send(client2_data.encode('utf-8'))      
            print('data sent to client 1.')

        elif client1_choice == 'r' and client2_choice == 'r':                   #client 1 rvcv, client 2 also rcv
            n='1'
            client1_socket.send(n.encode('utf-8'))
            client2_socket.send(n.encode('utf-8'))
            client1_data = client1_socket.recv(1024).decode('utf-8')
            print('data recieved from client 1.')
            client2_socket.send(client1_data.encode('utf-8'))
            print('data sent to client 2.')
            client2_data = client2_socket.recv(1024).decode('utf-8')
            print('data recieved from client 2.')
            client1_socket.send(client2_data.encode('utf-8'))
            print('data sent to client 1.')

        elif client1_choice == 's' and client2_choice == 's':                   # client 1 and client 2 both want send
            n = '2'
            client1_socket.send(n.encode('utf-8'))
            client2_socket.send(n.encode('utf-8'))
            client1_data = client1_socket.recv(1024).decode('utf-8')
            print('data recieved from client 1.')
            client2_socket.send(client1_data.encode('utf-8'))
            print('data sent to client 2.')
            client2_data = client2_socket.recv(1024).decode('utf-8')
            print('data recieved from client 2.')
            client1_socket.send(client2_data.encode('utf-8'))
            print('data sent to client 1.')

        elif client1_choice == 'END':
            client2_socket.send(client1_choice.encode('utf-8'))
            info = 'client 1 wants to close: closing.. closed!'
            client2_socket.send(info.encode('utf-8'))
            client1_socket.close()
            serverSocket1.close()
            print('client 1 closed.')

        elif client2_choice == 'END':
            client1_socket.send(client2_choice.encode('utf-8'))          #sent end status in the form of 'status'
            info = 'client 2 wants to close: closing..'
            client1_socket.send(info.encode('utf-8'))
            client2_socket.close()
            serverSocket2.close()
            print('client 2 closed.')
            exit

        else:
            print('wrong choice from clients:')
    

if __name__ == '__main__':
    main()

