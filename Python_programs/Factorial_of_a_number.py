import math

factorial = 1

def factorial(n):
    if n <0:
        print('you have entered a negative number')
    elif n == 0 :
        print('you have entered 0')
    else:
        for i in range (1,n + 1):
            s *= s
        print('factorial of',n,' is ', s)

def factorial_math(n):
    print('factorial of',n,' is ',math.factorial(n))

#taking user input
num = int(input('Enter a number: '))

factorial_math(num)
