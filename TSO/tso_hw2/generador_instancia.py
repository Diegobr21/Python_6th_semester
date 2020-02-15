import random 

try:
    n=int(input('Enter the number of elements: '))
    vmin=int(input('Smallest value possible for values of elements: '))
    vmax=int(input('Greatest value possible for values of elements: '))
    wmin=int(input('Smallest weight possible for weight of elements: '))
    wmax=int(input('Greatest weight possible for weight of elements: '))
    if wmax > wmin and vmax > vmin and vmin >0 and vmax >0 and wmin >0 and wmax >0:
        print('input successful')
        w=n*((wmin + wmax)/2)*0.4
        with open('instancia.txt', 'w') as f:    
            f.write('%r %r' % (n, w))
            f.write('\n')
            for i in range(n):
                f.write('%r %r %r' % (i, random.randint(vmin, vmax), random.randint(wmin, wmax)))
                f.write('\n')
            
    else:
        print('input failed')
except:
    print('All data must take integer values')
    







        
    
    









