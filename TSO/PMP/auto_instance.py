import sys
import random as random
import numpy as np
import matplotlib.pyplot as plt

#*-------------------Initial parameters-----------
"""
p=  int(input('Enter the number of facilities to be opened: '))
m=  int(input('Enter the number of facilities available: '))
n=  int(input('Enter the number of users to be considered: '))
dmin=int(input('Smallest distance possible for x/y: '))
dmax=int(input('Greatest distance possible for x/y: '))

"""
print('Ingrese el numero del grupo de 20 instancias a generar')
grupo = int(input('1- bajos 1er grupo\n2- bajos 2do grupo\n3-medios 1er grupo\n4- medios 2do grupo\n5- altos\n: '))
if grupo ==1:    #bajos 1
    print('grupo: ', grupo)
    n=1000
    m=100
    p=8    
    cont_name = 1
    file_l = "b"
    seed =47632
elif grupo ==2:  #bajos 2
    print('grupo: ', grupo)
    n=5000
    m=200
    p=10    
    cont_name = 21
    file_l = "b"
    seed =23674
elif grupo == 3: #meds 1
    print('grupo: ', grupo)
    n=10000
    m=400
    p=15    
    cont_name = 1
    file_l = "m"
    seed =257296
elif grupo == 4: #meds 2
    print('grupo: ', grupo)
    n=20000
    m=500
    p=25    
    cont_name = 21
    file_l = "m"
    seed =692752
elif grupo == 5: #altos
    print('grupo: ', grupo)
    n=30000
    m=600
    p=30    
    cont_name = 1
    file_l = "a"
    seed =41232
elif grupo == 6:
    print('XL size - Memory Error')
    n=40000
    m=700
    p=20    
    cont_name = 1
    file_l = "x"
    seed =23214


else:
    print('No existe el grupo')

#seed = 1 #ba10(hex) en decimal = 47632//23674 // 3ed10(medio) = 257296//692752 // a110(alto) = 41232//23214

#print(seed)
rango = 10000 #! NO MOVER
cant = 1  #! NO MOVER
for j in range(cant):
    np.random.seed(seed + cont_name)
    dmin = int(np.random.randint(4,399))
    dmax = dmin + rango

    

    if dmin > 0 and p < m and m > 0:
        #print('input successful')

        mu = (dmin + dmax) / 2   
        np.random.seed(seed + cont_name)  
        data = np.random.uniform(dmin,dmax,[m,n])
        #plt.scatter(data[:,0], data[:,1])
        #plt.show()
    
        #print(data)
        
        cont_name = str(cont_name)
        filename = file_l + cont_name
        if len(filename) != 0:
            filename+='.txt'
        else:
            filename=' '
        if filename!=' ':
            with open(filename,'w') as f:
                f.write('%r %r %r %r' % (m, n, p, int(mu)))
                f.write('\n')

                for i in range(m):
                    f.write('%r' % (i)+ " ")
                    
                    for j in range(n):
                        f.write('%r' % (data[i][j])+ " ")
                    f.write('\n')
                    
                f.close()
        

        print("input successful " + filename)

        cont_name = int(cont_name)
        cont_name += 1     
        #seed += 1  
        #np.random.seed = seed  
        #print(seed)  
    else:
        print('input failed')

