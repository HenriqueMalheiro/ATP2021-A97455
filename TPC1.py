# -*- coding: utf-8 -*-


def primeiro():
    a=input("Quem começa a jogar, CPU ou Jogador?")
    if a=="Jogador":
        Jogador()
    else:
        CPU()
    

def Jogador():
    total=21
    while total>1:
        b=input("Escolha o valor a tirar:")
        c=5-int(b)
        print("A CPU tira",c)
        total=total-5
        print("Ficam",total,"fósforos")
    print("A CPU ganhou o jogo")
        

def CPU():
    total=21
    while total>1:
        print("A CPU tira 1 fósforo")
        d=input("Escolha o valor a tirar:")
        total=total-1-int(d)
        print("Ficam",total,"fósforos")
        if int(d)+1!=5:
            print("A CPU tira",4-int(d))
            total=total-(4-int(d))
            while total>1:
                b=input("Escolha o valor a tirar:")
                c=5-int(b)
                print("A CPU tira",c)
                total=total-5
                print("Ficam",total,"fósforos")
            print("A CPU ganhou o jogo")
        elif total==1:
            print("Parabéns, ganhou o jogo!")
    
primeiro()