list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:

def merge_two_list(numbers_list):
    odd = []
    even = []

    for number in numbers_list:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    merged_list = [odd, even]
    return merged_list

# Example usage:
numbers = [1, 2, 33, 10, 20, 4]
result = merge_two_list(numbers)
print(result)
