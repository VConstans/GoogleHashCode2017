

def fonction ():
    global videos,caches, requests, endpoints 
    for req in range(0,len(request)):
        taille_vid = videos[req[0]] 
        idendpoint = req[1]
        endpoint = endpoints[idendpoint]
        
        for idcache in endpoint['caches'][0] :
            cache = caches[idcache]
            if (cache['freespace'] > taille_vid) :
                caches[idcache]['videos'].append(req[0])
                caches[idcache]['freespace'] -= taille_vid
                break
        


def optimisation1 ():
    global videos,caches, requests, endpoints 
    request.sort(key = lambda tup : tup[2]) #
    for req in range(0,len(request)):
        taille_vid = videos[req[0]] 
        idendpoint = req[1]
        endpoint = endpoints[idendpoint]
        
        for idcache in endpoint['caches'][0] :
            cache = caches[idcache]
            if (cache['freespace'] > taille_vid) :
                caches[idcache]['videos'].append(req[0])
                caches[idcache]['freespace'] -= taille_vid
                break

def opt_latence_endpoint():
    global endpoints
    for idendpoint in range(0,len(endpoints)):
        endpoints[idendpoint]['caches'].sort( key = lambda tup : tup[1] ) 
    
    
    
def optimisation2 ():
    global videos,caches, requests, endpoints 
    request.sort(key = lambda tup : tup[2]) #
    
    opt_latence_endpoint() # optimise par les latences
    
    for req in range(0,len(request)):
        taille_vid = videos[req[0]] 
        idendpoint = req[1]
        endpoint = endpoints[idendpoint]
        
        for idcache in endpoint['caches'][0] :
            cache = caches[idcache]
            if (cache['freespace'] > taille_vid) :
                caches[idcache]['videos'].append(req[0])
                caches[idcache]['freespace'] -= taille_vid
                break
        
# opt 1 : trier par rapport au nombre de request
# opt 2 : trier par rapport à la taille
# opt 3 : trier par rapport à la latence
# opt 4 : remplir les caches les moins remplit

def output():
    global caches
    nb_caches = 0
    for cache in caches :
        if cache['videos']:
            nb_caches ++;
    print str(nb_caches)
    for idcache in range(0,len(caches)) :
        if caches[idcache]['videos']:
            print "\n"+ str(idcache)
            for video in caches[idcache]['videos']:
                print " "+ str(video)
            
        
        
