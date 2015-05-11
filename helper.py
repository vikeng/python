#!/usr/bin/python

import argparse
from time import strftime
from getpass import getuser
from sys import version
from os import getcwd, listdir

parser = argparse.ArgumentParser()

parser.add_argument('-t', '--time', action='store_true', help='Print current time')
parser.add_argument('-d', '--date', action='store_true', help='Print current date')
parser.add_argument('-u', '--uname', action='store_true', help='Print current user')
parser.add_argument('-v', '--version', action='store_true', help='Print python version')
parser.add_argument('--tree', action='store_true', help='Print list files')

args = parser.parse_args()

if args.time:
    print "Time: " + strftime("%H:%M:%S")
elif args.date:
    print "Date: " + strftime("%d.%m.%Y")
elif args.uname:
    print "User: " + getuser()
elif args.version:
    print "Python version: " + version
elif args.tree:
    print "List files"
    files = listdir(getcwd())
    for f in files:
        print f
else:
    print "No info"
