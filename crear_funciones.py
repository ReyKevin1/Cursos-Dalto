import random

#creando una funcion simple
#def saludar ():
    #print("Hola Lucas, mi maetro ¿Como andas?")
    
    #ejecutando la funcion simple
    #saludar()

#crear una funcion que tenga parametros, lower convierte todo a minusculas 
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
         adjetivo = "reina"
    elif (sexo == "hombre"):
         adjetivo= "titan"
    else:
         adjetivo= "amor"
    
    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")

saludar("Camila", "mujer")
saludar("Dalto", "hombre")
saludar("Fran"," no binario")

#crear una funcion que nos retorne multiples valores, Chars = caracteres
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3= num - 5
    contraseña = f"{chars [c1]}{chars [c2]}{chars [c3]}{num * 2}"
    return contraseña,num
    
    #desempaquetando la funcion
contraseña, primer_numero = crear_contraseña_random (random.randint(10,1000))

#mostrando los resultados obtenidos y los datos utilizados para obtenerlos
frase = f"Tu contraseña nueva es: {contraseña}"
print(frase)
#print(f"El numero utilizado para crearla fue: {primer_numero}")