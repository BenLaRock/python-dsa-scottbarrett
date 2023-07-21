def print_items(a, b):
    # o(a) + o(b)
    # simplifies to o(a+b)
    for i in range(a):
        print(i)
    for k in range(b):
        print(k)

    # simplifies to o(a*b)
    for i in range(a):
        for k in range(b):
            print(i, k)


print_items(10)