Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here:

   def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

Fahrenheit_values = list(map(celsius_to_fahrenheit, Celsius_values))
print(Fahrenheit_values)

result = list(map(fahrenheit_values, Celsius_values))
print(result)
