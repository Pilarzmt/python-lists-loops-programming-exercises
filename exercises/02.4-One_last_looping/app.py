names = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']


    # Cambiar el valor del segundo elemento a "Steven"
names[1] = "Steven"

# Establecer el valor de la última posición a "Pepe"
names[-1] = "Pepe"

# Asignar al primer elemento el valor del 3er elemento concatenado con el valor del 5to elemento
names[0] = str(names[2]) + str(names[4])

# Realizar un bucle for para imprimir los elementos en orden inverso
for i in range(len(names) - 1, -1, -1):
    print(names[i])

    