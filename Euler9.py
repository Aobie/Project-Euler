#Euler 9
#Pythagorean triplet is a set of 3 natural numbers which can define a right triangle
#a ** 2 + b ** 2 = c ** 2, where a < b < c
import math
import time
def find_product():
    # since a, b, and c are natural numbers and a < b < c
    # the smallest set possible is a = 1, b = 2, c = 3
    # this also means that the largest a is 1000 / 3 - 1 = 332
    # since this would lead to a = 332, b = 333, c = 334
    for a in range(1, 332):
        # since b > a, start the inner loop at a + 1
        # since b < c, and a + b + c = 1000, set a = 1 to find largest b
        # leads to b + c = 999, so largest b = floor (999 / 2)
        for b in range (a + 1, 499): 
            if (math.sqrt (a ** 2 + b ** 2)).is_integer():
                c = int(math.sqrt(a ** 2 + b ** 2))
                #print ("A: ", a, "B: ", b, "C: ", c)
                if a + b + c == 1000:
                    return a * b * c

if __name__ == "__main__":
    print("Problem 9")
    print("Find the product of the one Pythagorean triplet for which a + b + c = 1000.")
    t1 = time.time()
    answer = find_product()
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
