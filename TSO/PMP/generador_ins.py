import random as random
import numpy as np

p=int(input('Enter the number of facilities to be opened: '))
m=int(input('Enter the number of facilities available: '))
n=int(input('Enter the number of users to be considered: '))
dmin=int(input('Smallest distance possible from customer(i) to facility(j): '))
dmax=int(input('Greatest distance possible from customer(i) to facility(j): '))
if dmin < dmax and dmin > 0 and dmax > 0 and p <= m and m > 0:
    print('input successful')
    mu = (dmin + dmax) / 2     
    data = mu + 2.5*np.random.randn(m, n)
    #print(data)
    
               
    filename=input('Enter a filename or press Enter to leave it as instancia: ')
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
    else:
        with open('instancia.txt', 'w') as f:    
            f.write('%r %r %r %r' % (m, n, p, int(mu)))
            f.write('\n')

            for i in range(m):
                f.write('%r' % (i)+ " ")
                for j in range(n):
                    f.write('%r' % (random.randint(dmin, dmax))+ " ")
                f.write('\n')
            f.close()
            
        
else:
    print('input failed')

