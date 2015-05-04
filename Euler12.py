import time
import Primes

def triangle_num(n):
    return sum(range(n+1))

def highly_divisible(n):
    numfactors = 0
    i = n
    ti = triangle_num (i)
    while numfactors <= n:
        if not Primes.isPrime(ti):
            numfactors = Primes.get_num_factors(ti)
        if numfactors <= n:
            i += 1
            ti = triangle_num (i)
            #print (ti)
    else:
        return ti

if __name__ == "__main__":
    print("Problem 12")
    print("Find the value of the first triangle number to have over five hundred divisors.")
    t1 = time.time()
    answer = highly_divisible(500)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
