#!/usr/bin/env python

import sys

def start():
    # Check arguments 
    if (len(sys.argv) < 2):
        print "usage: {} <input file>".format(sys.argv[0])
        sys.exit(1)

    # Open input file
    with open(sys.argv[1], "r") as myfile:
        # Read 10 lines 
        for i in range(0,9):
            myfile.readline().split()

  
start()
