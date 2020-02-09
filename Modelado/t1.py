try:
    a=int(input('Ingrese la constante multiplicativa(a):  '))
    x=int(input('Ingrese la semilla inicial(x0):  '))
    c=int(input('Ingrese la constante aditiva(c):  '))
    m=int(input('Ingrese el modulo divisor constante(m):  '))
    print(f"Los datos iniciales son:\na={a}, x0={x}, c={c}, m={m}\n")
    
    x0=[]
    xn=[]
    numrect=[]
    x0.append(x)   

    for i in range(m):
        xn.append(((a*x0[i])+c)%m)
        numrect.append(xn[i]/m)
        x0.append(xn[i])
        if xn[i]==x:
            print('Generador congruencial mixto no confiable')
            break
    print('Semilla inicial', x)
    print('Semillas generadas:', xn)
    if xn[-1]==x0[0] and len(xn)==m:
        print('Generador congruencial mixto confiable')
    else:
        print('Generador congruencial mixto no confiable')

except:
    print('Ingrese datos correctos')
    
