def Calc(x,y):
    return x+y,x-y,x*y,x/y,x%y
a = int(input("Enter the number 1:"))
b = int(input("Enter the number 2:"))
add,subtract,multiply,divide,modulas = Calc(a,b)
print("Sum of given numbers:",add)
print("Subtraction of two numbers:",subtract)
print("Multiplication of two numbers:",multiply)
print("Division of two numbers:",divide)
print("Modulus of two numbers:",modulas)
