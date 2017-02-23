

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
        

        
# opt 1 : trier par rapport au nombre de request
# opt 2 : trier par rapport à la taille
# opt 3 : trier par rapport à la latence
# opt 4 : remplir les caches les moins remplit
