
 
import socket, os
import sys
from thread import *
 
HOST = '0.0.0.0'   
PORT = 7777 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'

s.listen(1000)
print 'Socket now listening'
 
f = open('Menu.txt', 'r+')
mailsaved = f.read()
mailvar = mailsaved
def clientthread(conn):
			conn.recv(1024)
			conn.send("\n" + '\n' + " Connected To Bulletin Board Server " + '\n' +'\n   Please Enter The Number Of The Correseponding Mail To Read Below \n Or Type A Lowercase W To Write To The Bulletin Board A New Message \n ========================================================== \n' + '\n' + mailvar)
			mail = conn.recv(8196)
			print mail
			if mail == "w":
				t = open('2.txt', 'r')
				readed = t.read()
				t.close()
				print readed
				conn.send(readed)
				write = conn.recv(8196)
				t = open('2.txt', 'w')
				t.write(readed + "\n" + write)
				print write
				conn.send("Message Written!")
				t.close()
				conn.close()
			t = open( mail, 'r+')
			mailtosend = t.read()
			print mailtosend
			conn.send(mailtosend)
			conn.close()

while 1:
    conn, addr = s.accept()
    print 'Incoming Connection From ' + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread ,(conn,))
 
s.close()
