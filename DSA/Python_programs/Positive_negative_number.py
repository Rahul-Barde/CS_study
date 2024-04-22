def pnn_normal(x):
    if x == 0:
        print('Given number is zero')
    elif x < 0:
        print(x,'is a negative number')
    else:
        print(x,'is a positive number')

def pnn_nested_ifelse(x):
    if x >= 0:
        if x == 0:
            print("Zero")
        else:
            print("Positive number")
    else:
        print("Negative number")

x = int(input('Enter a number:\n'))

pnn_normal(x)
pnn_nested_ifelse(x)