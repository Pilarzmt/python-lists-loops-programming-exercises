my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:

def find_dicts_and_lists(my_list):
    new_list = []
    for item in my_list:
        if isinstance(item, (dict, list)):
            new_list.append(item)
    return new_list

# Ejemplo de uso:
my_list = [42, True, "towel", [2, 1], 'hello', 34.4, {"name": "juan"}]
new_list = find_dicts_and_lists(my_list)
print(new_list)
