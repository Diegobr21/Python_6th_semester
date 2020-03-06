#Datos n numeros rect, alpha
num_rect=[.19152, .36024, .94458, .54158, .75051, .60365, .83799, .32960, .19322, .11220]
n=len(num_rect)
#Cantidad de sub-intervalos
m=2
FEi=(n-1)/(m**2)
parejas=[]
#Lista de listas y agregamos el siguiente elemento
t = list(map(lambda el:[el], num_rect)) 
for i in range(n-1):
    t[i].append(t[i+1][0])
parejas = t.copy()
parejas=parejas[:-1]
secciones=m**2
F0i=[]
for i in range(secciones):
    F0i.append(0)
for i in range(len(parejas)):
    if parejas[i][0] <= 0.5 and parejas[i][1] <= 0.5:
        F0i[0]+=1
    elif parejas[i][0] > 0.5 and parejas[i][1] <= 0.5:
        F0i[1]+=1
    elif parejas[i][0] <= 0.5 and parejas[i][1] > 0.5:
        F0i[2]+=1
    elif parejas[i][0] > 0.5 and parejas[i][1] > 0.5:
        F0i[3]+=1
sumF0i=0.0
for i in range(len(F0i)):
    sumF0i+=((F0i[i]-FEi)**2)
x02=round(((m**2)/(n-1)),2)
x02*=sumF0i

tablas= float(input(f"Ingrese el estadístico de tablas para alpha: 5% y m: {m},______ "))
if x02 < tablas:
    print("Estadístico de prueba menor a estadístico de tablas:")
    print(f"{x02} < {tablas} ")
    print("Los números son aceptados")
else:
    print("Los números no son aceptados")

print("Parejas: \n (X ,           Y)")
for p in parejas:
    print(p,"\n")
    

