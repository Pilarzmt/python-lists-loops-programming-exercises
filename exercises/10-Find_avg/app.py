my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

#Your code here:
def calculate_average(my_list):
    total_sum = 0
    for num in my_list:
        total_sum += num

    average = total_sum / len(my_list)
    return average

result = calculate_average(my_list)
print(result)