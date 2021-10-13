import socket
from threading import Thread
def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      print ('port is open')
   except:
      print ('port is closed/ connection refused')


def Main():
    ip_add = input('Enter IP : ') 
    port_no = input('Enter Port : ')
    c = int(input('How many time do you want to test ping :'))

    for i in range(c):
        myThread = Thread(target=isOpen, args=(ip_add,port_no))
        myThread.start()
        print(myThread)
    
    
if __name__ == "__main__":
  Main()
