# @Author: sunshine
# @Date:   2017-12-03T21:23:05+08:00
# @Email:  guang334419520@126.com
# @Filename: argv_argparse.py
# @Last modified by:   sunshine
# @Last modified time: 2017-12-04T22:02:32+08:00

# conding = utf - 8

import sys
import argparse

def parser():
    args = argparse.ArgumentParser(description = "Personal Information",
    epilog = "Information end")
    #args.add_argument("-a", "--age",  type = int, dest = "age",    help = "Your age",         default = 0,      choices=range(150))
    args.add_argument("-H", "--host", type = str, dest = 'host',
    help = "host name", default = None)
    args.add_argument("-p", "--port",type = int,nargs = '+',dest = 'port',
    help = " other port", default = None)

    args = args.parse_args()
    #print("argparse.args = ", args, type(args))
    #print("host = %s port = %s " %(args.host, args.port))
    return args

if __name__ == "__main__":
     parser()
