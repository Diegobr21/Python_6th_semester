def mcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x ==0) and (greater % y ==0)):
            mcm = greater
            break
        greater += 1
    return mcm
try:
    a=int(input('Ingrese la constante multiplicativa(a):  '))
    x=int(input('Ingrese la semilla inicial(x0):  '))
    m=int(input('Ingrese el modulo divisor constante(m):  '))
    print(f"Los datos iniciales son:\na={a}, x0={x},  m={m}\n")
    if m & m-1 ==0:
        print('binario')
        pe=int(m/4)
        x0=[]
        xn=[]
        numrect=[]
        x0.append(x) 
        for i in range(pe):
            xn.append((a*x0[i])%m)
            numrect.append(xn[i]/m)
            x0.append(xn[i])
            if xn[i]==x:
                print('Generador congruencial multiplicativo no confiable')
                break
        print('Semilla inicial', x)
        print('Semillas generadas:', xn)
        if xn[-1]==x0[0] and len(xn)==pe:
            print('Generador congruencial multiplicativo confiable')
        else:
            print('Generador congruencial multiplicativo no confiable')

    elif str(m)[0]=='1':
        
        zeros=0       
        num=str(m)
        for l in num[1:]:
            if l!='0':
                print('no es decimal ni binario')
            elif l=='0':
                zeros+=1
        pot=zeros
        
        if pot>=5:
            d=(pot-2)
            pe=(5*(10**d))
            
        elif pot < 5:
            d=pot
            dos=(2**(d-2))
            cinco=(5**(d-1))*(4)
            mincm=mcm(dos,cinco)
            pe=mincm
        
        x0=[]
        xn=[]
        numrect=[]
        x0.append(x) 
        for i in range(pe):
            xn.append((a*x0[i])%m)
            numrect.append(xn[i]/m)
            x0.append(xn[i])
            if xn[i]==x:
                print('Generador congruencial multiplicativo no confiable')
                break
        print('Semilla inicial', x)
        print('Semillas generadas:', xn)
        if xn[-1]==x0[0] and len(xn)==pe:
            print('Generador congruencial multiplicativo confiable')
        else:
            print('Generador congruencial multiplicativo no confiable')          
        print('decimal')
        
    else:
        print('no es decimal ni binario')

except:
    print('nop')