from socket import *

s_ip = 'localhost'
s_port = 9999
s_addr = (s_ip, s_port)

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind( s_addr )

s_sock.settimeout(5)

data, c_addr = s_sock.resvfrom(1024)

print('수신 주소는 : ', c_addr)
print('수신된 자료는 : ', data.decode('utf-8'))

s_sock.close()