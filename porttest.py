# @Author: sunshine
# @Date:   2017-12-04T21:15:06+08:00
# @Email:  guang334419520@126.com
# @Filename: porttest.py
# @Last modified by:   sunshine
# @Last modified time: 2017-12-06T21:10:38+08:00

import socket
import threading

scrennLock = threading.Lock()
#用来判断端口是否开放
def connScan(tgtHost, tgtPort):
    try:
        connfd = socket.socket(socket.AF_INET,
        socket.SOCK_STREAM)
        connfd.connect((tgtHost, tgtPort))
        connfd.send(b'ViolentPython\r\n')
        results = connfd.recv(100)

        scrennLock.acquire()
        print('[+]%d/tcp open' % tgtPort)
        print('[+]' + str(results))

    except:
        scrennLock.acquire()
        print('[-]%d/tcp closed' % tgtPort)
    finally:
        scrennLock.release()
        connfd.close()



def portScan(tgtHost, tgtPorts):

    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-]Cannot resolve '%s': Unknown host"
        %(tgtHost))
        return
    try:
        trgName = socket.gethostbyaddr(tgtHost)
        print("[+]Scan Results for:" + tgtName)
    except:
        print("[+]Scan Results for:" + tgtIP)

    socket.setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print("Scanning port " + str(tgtPort))
        t = threading.Thread(target = connScan,
        args=(tgtHost, int(tgtPort)))
        t.start()
        #connScan(tgtHost, int(tgtPort))
