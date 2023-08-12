arr = [45, 67, 87, 23, 5,  32, 60]

#your code below:
new_list = []
#Invierte la lista
for i in  range(len(arr) -1, -1, -1):

 new_list.append(arr[i])


# Imprimimos el resultado obtenido
print("list inicial:", arr)
print("list final:", new_list)