# @Author: sunshine
# @Date:   2017-12-03T21:56:43+08:00
# @Email:  guang334419520@126.com
# @Filename: scanner_port.py
# @Last modified by:   sunshine
# @Last modified time: 2017-12-06T21:04:09+08:00

import argv_argparse
import porttest



def main():
    args = argv_argparse.parser()
    if (args.host == None) | (args.port == None):
        exit(0)
    else:
        print("hostname = %s \t port = %s" %(args.host, args.port))

    porttest.portScan(args.host, args.port)

if __name__ == '__main__':
    main()
