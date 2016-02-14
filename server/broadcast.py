import sys, time
from socket import *
BC_PORT = 12345

while True:
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('', 0))
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.sendto("IAMASERVER", ('<broadcast>', BC_PORT))

    time.sleep(5)
