import random

def tirar_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma1 = dado1 + dado2
    return dado1, dado2, suma1

def juego():
    numberl = [4,5,6,8,9,10]
    dados =tirar_dados()
    d1 = dados[0]
    d2 = dados[1]
    s = dados[2]
    gano = 0
    

    if s == 7 or s == 11:
        print('ganaste')
        gano = 1
        
    elif s in numberl:
        not_seven = True
        while not_seven:
            segundo_tiro = tirar_dados()
            d1n = segundo_tiro[0]
            d2n = segundo_tiro[1]
            sn = segundo_tiro[2]
            if sn == 7:
                print('perdiste, salio un 7 antes')
                
                not_seven = False
            elif sn == s:
                print('ganaste')
                gano = 1
                not_seven = False
            else:
                s = sn
    else:
        print('perdiste, 2, 3 o 12')
    return gano
     

def resultados(cantidad = 100):
    money = 20
    won = 0
    lost = 0
    meta = 0
    quiebra = 0
    for i in range(cantidad):
        if money == 50:
            print("Se acabo, dinero:", money)
            print('iteracion :', i)
            meta += 1
            money = 20
        elif money == 0:
            print('Quiebra :', money)
            quiebra += 1
            money = 20
        r =juego()
        if r == 1:
            won += 1
            money += 1
        else:
            lost += 1
            money -= 1

    print('Dinero: ', money)
    print('Meta :', meta)
    print('Quiebra: ', quiebra)
    return money, meta, quiebra

resultados()
    


