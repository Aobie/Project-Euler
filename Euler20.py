#Euler 20

import time
import math

def factorial_sum(n):
    total = 0
    workstr = str(math.factorial(100))
    for i in range(len(workstr)):
        total += int(workstr[i])
    return total

if __name__ == "__main__":
    print("Problem 20")
    print("Find the sum of the digits in the number 100!")
    t1 = time.time()
    answer = factorial_sum(100)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
