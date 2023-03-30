print("BIENVENIDO/A A NUESTRO PROGRAMA","\n")

print

infracciones= int(input("Ingrese el numero de infracciones de este mes: "))

infra_Dia= infracciones / 30

prom_matutino= infracciones * 0.2

print("El promedio de infracciones de la mañana es de: ", prom_matutino)
prom_vespirino= infracciones * 0.35

print("El promedio de infracciones de la tarde es de: ",prom_vespirino,)

prom_nocturno= infracciones * 0.45

print("El prromedio de infracciones nocturnas es de: ", prom_nocturno)



