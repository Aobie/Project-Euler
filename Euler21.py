#Euler 21
import time
import Primes

def amicable_num_sum(n):
    amicables = []
    #primes won't have amicable pairs by definition, therefore filter them out
    prime_list = Primes.prime_sieve(n)
    for i in range(2, n + 1):
        if not (i in prime_list):
            #get_all_factors includes i, so we will need to remove it
            tempfactors = Primes.get_all_factors(i)
            tempfactors.pop() #remove the number itself from factors (proper only)
            #print("Temp: ", tempfactors)
            sumfactors = sum(tempfactors)
            if i != sumfactors:
                #print (i, sumfactors)
                tempfactors = Primes.get_all_factors(sumfactors)
                tempfactors.pop()
                if sum(tempfactors) == i:
                    amicables.append(i)
                    #amicables.append(sumfactors)
                    #print("Amicables: ", amicables)
    return sum(amicables)

if __name__ == "__main__":
    print("Euler Project - Problem 21")
    print("Find the sum of all amicable numbers under 10000")
    t1 = time.time()
    answer = amicable_num_sum(10000)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
