#promedio de duracion 
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_pro = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#mostrando las diferencias de duracion 
diferencias_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_con_max = 100 - dalto_curso * 1000  // otros_cursos_max / 10
diferencias_con_pro = 100 - dalto_curso / otros_cursos_pro *100

#calculando el porcentaje de tiempo vacio removido 
tiempo_vacio_pro = 100 - otros_cursos_pro / crudo_promedio * 100
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 100

#mostrando las diferencias de duracion (ejercicio A)
print(f"El curso de dalto dura un {diferencias_con_min}% menos que el mas rapido")
print(f"El curso de dalto dura un {diferencias_con_max}% menos que el mas lento")
print(f"El curso de dalto dura un {diferencias_con_pro}% menos que el promedio")

#mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f"Un curso promedio elimina un {tiempo_vacio_pro}% de tiempo vacio")
print(f"Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")

#mostrando diferencias si los cursos duraran 10 horas 
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_pro * 1000 // dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas de este curso equivale a ver {dalto_curso * 1000 // otros_cursos_pro / 10} horas de este curso")

