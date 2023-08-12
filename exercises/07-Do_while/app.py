
#Your code go here:
def liftoff_countdown():
    x = 20
    while x >= 1:
        if x % 5 == 0:
            print(x, "!")
        else:
            print(x)
        x -= 1
    print("LIFTOFF")

# Llamada a la función
liftoff_countdown()