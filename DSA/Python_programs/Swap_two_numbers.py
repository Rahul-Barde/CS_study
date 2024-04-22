# tuple unpacking
def tuple_unpacking(x,y):
    x, y = y, x 
    return x, y

#Addition and Subtraction
def Addition_and_Subtraction():
    x = x + y
    y = x - y
    x = x - y
    return x, y

#Multiplication and Division
def Multiplication_and_Division():
    x = x * y
    y = x / y
    x = x / y
    return x, y

#XOR swap
def XOR_swap(x,y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y

x = int(input('Enter number 1:\n'))
y = int(input('Enter number 2:\n'))

x , y = tuple_unpacking(x,y)

print('The value of x after swapping:',x)
print('The value of y after swapping:',y)