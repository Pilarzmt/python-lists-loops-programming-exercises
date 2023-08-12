#Remember import random function here:
import random
my_list = [4,5,734,43,45]

#The magic is here:

for _ in range(10):
    random_integer = random.randint(2, 96)
    my_list.append(random_integer)

print(my_list)