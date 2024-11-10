
def swap_numbers(a, b):
    print("Before swapping: a =", a, ", b =", b)
    
    
    temp = a
    a = b
    b = temp
    
    print("After swapping: a =", a, ", b =", b)


a = 5
b = 10
swap_numbers(a, b)
