l = [ 9,5,9,4,3,6,7,1,2,3,9,1,2]                                                     
                                                                                         
print l 

# mediana                                                                                
l.sort()                                                                                 
print l                                                                                  
                                                                                         
if len(l) % 2 == 0:                                                                      
    n = len(l)                                                                           
    mediana = (l[n/2-1]+ l[n/2] )/2                                                      
else:                                                                                    
    mediana =l[len(l)/2]                                                                 
                                                                                         
print 'mediana:',mediana 