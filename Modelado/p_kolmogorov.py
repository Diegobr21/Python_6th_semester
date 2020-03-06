#dictionaries for alpha =10%, 5% & 1% {n: d}
d_alpha10={1:0.950, 2:0.776, 3:0.642, 4:0.564, 5:0.510, 6:0.470, 7:0.438, 8:0.411, 9:0.388, 10:0.368, 11:0.352, 12:0.338,
 13:0.352, 14:0.314, 15:0.304, 16:0.295, 17:286, 18:0.278, 19:0.272, 20:0.264, 25:0.240, 30:0.220, 35:0.210}

d_alpha5={1:0.975, 2:0.842, 3:0.708, 4:0.624, 5:0.563, 6:0.521, 7:0.486, 8:0.457, 9:0.432, 10:0.409, 11:0.391, 12:0.375,
 13:0.361, 14:0.349, 15:0.338, 16:0.328, 17:318, 18:0.309, 19:0.301, 20:0.294, 25:0.264, 30:0.242, 35:0.230, 40:0.210,
 50:0.188, 60:0.172, 70:0.160, 80:0.150, 90:0.141, 100:0.134 }

d_alpha1={1:0.995, 2:0.929, 3:0.829, 4:0.734, 5:0.669, 6:0.618, 7:0.577, 8:0.543, 9:0.514, 10:0.486, 11:0.468, 12:0.450,
 13:0.433, 14:0.418, 15:0.404, 16:0.392, 17:381, 18:0.371, 19:0.363, 20:0.352, 25:0.317, 30:0.290, 35:0.270, 40:0.252,
 50:0.226, 60:0.207, 70:0.192, 80:0.180}

#Datos n numeros rect, alpha
num_rect=[.19152, .36024, .94458, .54158, .75051, .60365, .83799, .32960, .19322, .11220]
n=len(num_rect)

num_rect.sort()

alpha=int(input("Ingrese alpha: %"))

fxi=[]
for i in range(len(num_rect)):
    fxi.append((i+1)/n)

dn=[]
for i in range(len(num_rect)):
    dn.append(abs(fxi[i] - num_rect[i]))
Dn=max(dn)

print("i     xi    F(xi)  |F(xi) - xi|")
print("________________________________")
for i in range(len(num_rect)):
    print(f"{i+1} | {round(num_rect[i], 5)} | {fxi[i]} | {round(dn[i], 5)} \n")

dtablas=0
if alpha == 5:
    dtablas=d_alpha5[n]
elif alpha == 1:
    dtablas = d_alpha1[n]
elif alpha == 10:
    dtablas = d_alpha10[n]
#dtablas= float(input(f"Ingrese el estadístico de tablas para alpha: 5% y n: {n} "))

if Dn < dtablas:
    print("Estadístico de prueba menor a estadístico de tablas:")
    print(f"{Dn} < {dtablas} ")
    print("Los números son aceptados")
else:
    print("Los números no son aceptados")
