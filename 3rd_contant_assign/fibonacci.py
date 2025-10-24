def fibonacci(terms):
    sequence = []
    a, b = 0, 1
    for i in range(terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence
print(fibonacci(10))