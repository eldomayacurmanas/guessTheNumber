import random
import os

juego= True
while juego==True:
    os.system("cls")
    vidas = 5
    print("adivine un numero random entre 0 y 100: ")
    numero= random.randint(0,100)
    win=False
    while vidas != 0 and win== False :
        intento= int(input())
        
        if intento < numero:
            vidas-=1
            print("el numero es mayor que {} le quedan {} vidas".format(intento, vidas))
        if intento > numero:
            vidas-=1
            print("el numero es menor que {} le quedan {} vidas".format(intento, vidas))
        if intento == numero:
            print("ha acertado al numero {}!".format(numero))
            win = True
    if vidas==0:
        print("usted ha perdido, el numero era {}".format(numero))
    print("digite 1 para jugar de nuevo ")
    if int(input()) != 1:
        juego=False
