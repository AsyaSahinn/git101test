a = 1
b = 1
fibonacci = [a, b]


for n in range(20):

    a, b = b, a+b
    fibonacci.append(b)
print(fibonacci)
