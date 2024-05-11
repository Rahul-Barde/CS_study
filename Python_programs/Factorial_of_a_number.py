num = int(input('Enter a number: '))

factorial = 1

if num <0:
    print('you have entered a negative number')
elif num == 0 :
    print('you have entered 0')
else:
    for i in range (1,num + 1):
        factorial = factorial*i
    print('factorial of',num,' is ', factorial)