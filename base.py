#!/usr/bin/env python

import sys


videos = []
caches = []
requests = []
endpoints = []


def start():

    global videos, requests, caches, endpoints

    # Check arguments 
    if (len(sys.argv) < 2):
        print "usage: {} <input file>".format(sys.argv[0])
        sys.exit(1)

    # Open input file
    with open(sys.argv[1], "r") as myfile:
        nvideos, nendpoints, nreqdesc, ncaches, capcaches = [int(n) for n in myfile.readline().split()]
        videos = [int(n) for n in myfile.readline().split()]

        # Init caches
        caches = ncaches*[{'videos':[], 'freespace': capcaches}]

        # Read endpoints
        for i in range(0,nendpoints):
            latdc, ncachep = [int(n) for n in myfile.readline().split()]
            endpoint = {'caches':[],'latdc': latdc}
            # Read endpoint caches
            for j in range(0,ncachep):
                idcache, latcache = [int(n) for n in myfile.readline().split()]
                endpoint['caches'].append((idcache, latcache))

        # Read requests
        for i in range(0,nreqdesc):
            idvideo, idendpoint, nbrequests = [int(n) for n in myfile.readline().split()]
            requests.append((idvideo, idendpoint, nbrequests))

    

  
start()
