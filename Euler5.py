def Euler5(n):
    x = 0
    y = n
    flag = False
    while x <= 99999999999999:
        x += n
        y = n
        if x % y == 0:
            while y > 0:
                if x % y == 0:
                    flag = True
                else:
                    flag = False
                    break
                y -= 1
            else:
                print(x)
                if flag:
                    return x
