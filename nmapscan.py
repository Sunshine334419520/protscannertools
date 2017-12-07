# @Author: sunshine
# @Date:   2017-12-06T21:16:49+08:00
# @Email:  guang334419520@126.com
# @Filename: nmapscan.py
# @Last modified by:   sunshine
# @Last modified time: 2017-12-07T11:37:38+08:00


# coding = UTF-8

import nmap
import socket
import argv_argparse

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    results = nmScan.scan(tgtHost, str(tgtPort))
    state = results['scan'][tgtHost]['tcp'][tgtPort]['state']
    print("[+] {} tcp/{} {}".format(tgtHost, tgtPort, state))
def main():
    args = argv_argparse.parser()
    if (args.host == None) | (args.port == None):
        exit(0)
    else:
        print("hostname = %s \t port = %s" %(args.host, args.port))

    try:
        tgtIP = socket.gethostbyname(args.host)
    except:
        print("[-]Cannot resolve '%s': Unknown host"
        %(tgtHost))

    for tgtPort in args.port:
        nmapScan(tgtIP, tgtPort)

if __name__ == '__main__':
    main()
