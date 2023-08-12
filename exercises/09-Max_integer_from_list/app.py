my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:
def max_integer(my_list):
    max_number = my_list[0]  
    for num in my_list:
        if num > max_number:
            max_number = num

    return max_number

# Encuentra la cifra más alta
result = max_integer(my_list)
print(result)
