import random
jugar = 1
print("Bienvenidos/as a todos!")
while jugar == 1:
    print("\nIntenta adivinar el número entre 1 y 20, tienes 3 intentos.\n")
    n = random.randint(1,20)
    intentos = 0
    while jugar == 1 and intentos < 3:
        r = int(input("Dime en cual número estoy pensando: \n"))
        if r == n:
            print("\nCorrecto!!! Has ganado!! :D\n")
            jugar = 'fin'
            break
        elif (r - n) >= -2 and (r - n) < 0:
            if intentos == 2:
                print("\nMuy cercaaa!!, es un poco más mayor!")
            else:
                print("\nMuy cercaaa!!, es un poco más mayor!, prueba de nuevo...")
        elif (r - n) <= 2 and (r - n) > 0:
            if intentos == 2:
                print("\nMuy cercaaa!!, es un poco más menor!")
            else:
                print("\nMuy cercaaa!!, es un poco más menor!, prueba de nuevo...")
        elif (r - n) >= -5 and (r - n) < -2:
            if intentos == 2:
                print("\nCerca!, es un poco mayor.")
            else:
                print("\nCerca!, es un poco mayor, prueba de nuevo...")
        elif (r - n) <= 5 and (r - n) > 2 :
            if intentos == 2:
                print("\nCerca!, es un poco menor.")
            else:
                print("\nCerca!, es un poco menor, prueba de nuevo...")
        elif (r - n) >= -8 and (r - n) < -5:
            if intentos == 2:
                print("\nTibio..., es mayor.")
            else:
                print("\nTibio..., es mayor, prueba de nuevo...")
        elif (r - n) <= 8 and (r - n) > 5:
            if intentos == 2:
                print("\nTibio..., es menor.")
            else:
                print("\nTibio..., es menor, prueba de nuevo...")
        elif (r - n) >= -12 and (r - n) <-8:
            if intentos == 2:
                print("\nFrío, es mayor.")
            else:
                print("\nFrío, es mayor, prueba de nuevo...")
        elif (r - n) <= 12 and (r - n) > 8:
            if intentos == 2:
                print("\nFrío, es menor.")
            else:
                print("\nFrío, es menor, prueba de nuevo...")
        elif (r - n) < -12:
            if intentos == 2:
                print("\nEstás muuuy lejos, es mucho mayor.")
            else:
                print("\nEstás muuy lejos, es mucho mayor, prueba de nuevo...")
        elif (r - n) > 12:
            if intentos == 2:
                print("\nEstás muuuy lejos, es mucho menor.")
            else:
                print("\nEstás muuy lejos, es mucho menor, prueba de nuevo...")
        intentos += 1
        if intentos == 1:
            print("Te quedan 2 intentos.\n")
        if intentos == 2:
             print("Solo te queda 1 intento!!\n")
        if intentos == 3:
            print("Oohh!! No te quedan mas intentos :( El número era",str(n),". Para la próxima tendrás más suerte :)\n")
            jugar = 'fin'
    
    while jugar == 'fin':
        jugar = input("¿Quieres volver a jugar? Responde Si o No: \n")
        if jugar == 'si' or jugar == 'SI' or jugar == 'sI' or jugar == 'Si':
            print("\nOk! :) Buena suerte!")
            jugar = 1
        elif jugar == 'no' or jugar == 'NO' or jugar == 'No' or jugar == 'nO':
            print("\nBueno, hasta la próxima! :)")
            jugar = 0
            input("\nPresiona Enter para salir...")
        elif jugar != 'si' or jugar != 'SI' or jugar != 'sI' or jugar != 'Si' or jugar != 'no' or jugar != 'NO' or jugar != 'No' or jugar != 'nO':
            print("\nPor favor, responde si quieres volver a jugar.")
            jugar = 'fin'
            
        


    
    
        
        


