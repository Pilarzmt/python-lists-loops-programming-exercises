arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_of_odd_numbers(my_list):
    total_sum = 0  # Variable auxiliar para llevar la suma de valores
    for item in my_list:
        if isinstance(item, int) and item % 2 != 0:  # Verificar si el elemento es un número impar
            total_sum += item
    return total_sum
