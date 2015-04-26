def Euler2():
    x = 1
    y = 2
    max = 4000000
    even_fib_list = [2]
    while x < max and y < max:
        x += y
        if x % 2 == 0:
            even_fib_list.append(x)
        y += x
        if y % 2 == 0:
            even_fib_list.append(y)
    else:
        return sum(even_fib_list)
