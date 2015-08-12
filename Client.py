# client.py
import socket, os, time

# create a socket object


def Connect():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        host = raw_input(" HOST: ")

        port = 7777
        tm = " Connecting... \n"
        print tm
        s.setblocking(1)
        s.connect((host, port))
        s.send("  Client")

        try:

                        print " Connected! \n"
                        print " Recv Data \n"
                        os.system("cls")
                        tm = s.recv(8196)
                        print tm
                        print " "
                        data = raw_input('MAIL:>')
                        if data == 'w':
                                s.send(data)
                                cmsg = s.recv(8192)
                                print cmsg
                                write = raw_input('Write:>')
                                s.send(write)
                                msgstat = s.recv(8196)
                                print msgstat
                                os.system("pause")
                                s.close()



                        s.send(data + ".txt")
                        mailrcvd = s.recv(8196)
                        print mailrcvd
                        s.close()
                        os.system("pause")
                        os.system("cls")
                        Connect()
        except:
                s.close()
                os.system("cls")
                Connect()
Connect()
