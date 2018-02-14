l = [ 9,5,9,4,3,6,7,1,2,3,9,1,2]                                                     
                                                                                         
print l 


# moda                                                                                   
repeticiones = 0                                                                         
for i in l:                                                                              
    apariciones = l.count(i)                                                             
    if apariciones > repeticiones:                                                       
        repeticiones = apariciones                                                       
                                                                                         
modas = []                                                                               
for i in l:                                                                              
    apariciones = l.count(i)                                                             
    if apariciones == repeticiones and i not in modas:                                   
        modas.append(i)                                                                  
                                                                                         
print "moda:", modas      