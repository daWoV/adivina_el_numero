import random

def cls():
    print("\n"*100)

def letrero():
    print("""
     _       _ _       _                    _           __                           
    / \   __| (_)_   _(_)_ __   __ _    ___| |  _ __  _/_/_ _ __ ___   ___ _ __ ___  
   / _ \ / _` | \ \ / / | '_ \ / _` |  / _ \ | | '_ \| | | | '_ ` _ \ / _ \ '__/ _ \ 
  / ___ \ (_| | |\ V /| | | | | (_| | |  __/ | | | | | |_| | | | | | |  __/ | | (_) |
 /_/   \_\__,_|_| \_/ |_|_| |_|\__,_|  \___|_| |_| |_|\__,_|_| |_| |_|\___|_|  \___/ 
                                                                                                                                                                                                                    
    """)

def num_random():
    global n
    n=random.randint(1,50)

def opcion():
    global op
    while True:
        cls()
        print("(╬ ಠ益ಠ)")
        op=input("No es el número ¿Quieres intentarlo otra vez? Si [S] No [N]  ")
        if op!="S" and op!="N":
            input("ERROR, solo se puede escribir 'S' o 'N' [ENTER]")
        if op=="S":
            return(0)
            break
        if op=="N":
            break
def entrada():
    global i
    global num
    global n
    #n=5
    i=0
    while True:
        cls()
        letrero()
        print("\n")
        #print(n)
        num=int(input("Adivina el número secreto del 1 al 50: "))
        i+=1
        if num<1 or num>50:
            cls()
            letrero()
            print("\n")
            input("ERROR, número fuera de rango de 1 a 50 [ENTER]")
            i-=1
        if num != n:
            opcion()
            if op=="N":
                cls()
                print("(╯°□°）╯︵ ┻━┻")
                print("El número secreto era     : ",n)
                print("Tu número de intentos fue : ",i)
                input("[ENTER]")
                break
        else:
            cls()
            print("（ ^_^）o自自o（^_^ ）")
            print("Bien hecho, el número secreto era: ",n)
            print("Tu número de intentos fue: ",i)
            input("[ENTER]")
            break
            
num_random()
entrada()