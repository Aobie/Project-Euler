import Primes
import time

def find_sum_primes(n):
    #getPrimes gets all primes up to, but not including the passed in value
    #primeslist = Primes.getPrimes(n + 1)
    primeslist = Primes.prime_sieve(n)
    return sum(primeslist)

if __name__ == "__main__":
    print("Problem 10")
    print("Find the sum of all the primes below 2 million.")
    t1 = time.time()
    answer = find_sum_primes(2000000)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
