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
        caches = [{'videos':[], 'freespace': capcaches} for i in range(0,capcaches)]

        # Read endpoints
        for i in range(0,nendpoints):
            latdc, ncachep = [int(n) for n in myfile.readline().split()]
            endpoint = {'caches':[],'latdc': latdc}
            # Read endpoint caches
            for j in range(0,ncachep):
                idcache, latcache = [int(n) for n in myfile.readline().split()]
                endpoint['caches'].append((idcache, latcache))

            endpoints.append(endpoint)

        # Read requests
        for i in range(0,nreqdesc):
            idvideo, idendpoint, nbrequests = [int(n) for n in myfile.readline().split()]
            requests.append((idvideo, idendpoint, nbrequests))

    # Launch
    fonction()
    output()

    

def fonction ():
    global videos,caches, requests, endpoints 

    # Optimizations 
    requests.sort(key = lambda tup : tup[2])
    opt_latence_endpoint() # optimise par les latences

    for req in range(0,len(requests)):
        taille_vid = videos[requests[req][0]] 
        idendpoint = requests[req][1]
        endpoint = endpoints[idendpoint]
         

        ispresent = False
        for idcache, latcache in endpoint['caches']:
            if requests[req][0] in caches[idcache]['videos']:
                ispresent = True
                break
        
        if ispresent:
            continue
        
        for idcache, latcache in endpoint['caches']:
            cache = caches[idcache]
            if (cache['freespace'] >= taille_vid):
                caches[idcache]['videos'].append(requests[req][0])
                caches[idcache]['freespace'] -= taille_vid
                break
        



def opt_latence_endpoint():
    global endpoints
    for idendpoint in range(0,len(endpoints)):
        endpoints[idendpoint]['caches'].sort( key = lambda tup : tup[1] ) 
    
    
    
        
def output():
    global caches
    nb_caches = 0
    for cache in caches :
        if cache['videos']:
            nb_caches += 1

    print nb_caches

    for idcache in range(0,len(caches)) :
        if caches[idcache]['videos']:
            print idcache,
            for video in caches[idcache]['videos']:
                print video,
            print ''
            
        
        
  
start()
