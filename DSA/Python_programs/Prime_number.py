# num = int(input('Enter a number '))



def with_var(num):
    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")

'''      
def with_if_else(num):
    if num == 1:
        print(num,'is not a prime number')
    else:
        for i in range(2, num):
            if (num % i) == 0:
                print(num,'is not a prime number')
                break
        else:
            (num,"is a prime number")
'''
                
for i in range(0,10):
    with_var(i)
