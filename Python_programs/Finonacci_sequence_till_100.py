def fibonacci_sequence(limit):
    a, b = 0, 1
    while a <= limit:
        print(a)
        a, b = b, a + b
    
fibonacci_series = fibonacci_sequence(100)

