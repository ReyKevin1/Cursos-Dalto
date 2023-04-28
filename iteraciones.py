
frutas = ("banana", "manzana","durazno", "granada", "pera","ciruela", "naranja")
cadena = "Hola Dalto"
numeros = [2, 5, 8,10]


#evitando que se coma una fruta con la sentencia continue
for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Me voy a comer una {fruta}")
    
    
#evitar que el bucle siga ejercitandose
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break
else:
    print("Terminado")
    

#recorrer una cadena de texto
for letra in cadena:
    print(letra)


#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros ]
print(numeros_duplicados)