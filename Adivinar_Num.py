import random

def juegoAdivinar():
    
    #Generar un numero del 1 al 100
    
    numero_secreto = random.randint(1,100) 
    intentos = 0
    adivinado = False 
    
    print("¡Bienvenido al juego de adivinanza de numero!")
    print("Debes adivinar un  numero del 1 al 100")
    print("¡Intenta Adivinarlo!")
    
    
    while not adivinado:
        
        #Solicitar un numero
        adivinanza = input("Introduzca un numero del 1 al 100: ")
    
    
        if adivinanza.isdigit():
         adivinanza = int(adivinanza) #se pasa de str a int
         intentos += 1
        
         if adivinanza < numero_secreto:
            print(f"El numero secreto es mayor a {adivinanza}")
         elif adivinanza > numero_secreto:
            print(f"El numero secreto es menor a {adivinanza}")
         else:
            print(f"Haz ganado, el numero {adivinanza} es el secreto y los has logrado en {intentos} intentos.")
        else:
             print("Por favor introduzca un numero valido entre el 1 al 100")
        
juegoAdivinar()


