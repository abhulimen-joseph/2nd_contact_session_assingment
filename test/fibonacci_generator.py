def fibonacci(number):
    sequence = []
    a,b = 0, 1
    for i in range(number):
        sequence.append(a)
        a, b = b, a + b
        
    return sequence

print(fibonacci(20))

