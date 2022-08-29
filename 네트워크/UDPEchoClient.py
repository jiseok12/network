from socket import *
from stat import S_IFPORT

s_ip = 'localhost'
s_port = 9999
s_addr = (s_ip, s_port)

c_sock = socket(AF_INET, SOCK_DGRAM)

indata = input('문자열 입력: ')
c_sock.sendto(indata.encode('utf-8'), s_addr)

while indata != 'q':
    data, addr = c_sock.recvfrom(1024)

    print('메아리 문자열 : ', data.decode('utf-8'))
    indata = input('문자열 입력 : ')
    c_sock.sendto(indata.encode('utf-8'), s_addr)

c_sock.close()