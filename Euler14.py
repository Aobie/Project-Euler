#Euler 14
import time

def collatz_step(n):
    if n % 2 == 0:
        return (n / 2)
    else:
        return (3 * n + 1)
     
def Collatz (n):
    resultchain = [n]
    stepstone = n
    while stepstone > 1:
        print (stepstone)
        stepstone = collatz_step(stepstone)
        resultchain.append(stepstone)
    else:
        resultchain.append(1)
    return resultchain

# Return the number of steps to reach 1 using a Collatz Sequence
def Collatz_Num(n):
    steps = 1
    val = n
    #1 is expected to be the terminal value of all Collatz Sequences
    while val > 1:
        val = collatz_step(val)
        steps += 1
    else:
        return steps

def Euler14(maxval):
    longchain, checkval = 0, 0
    result = 2
    for i in range(2, maxval):
        checkval = Collatz_Num(i)
        #print (i, ": ", checkval)
        if checkval > longchain:
            longchain = checkval
            result = i
    else:
        return result

# Using OOP and a lookup cache to speed things up
class ChainCache:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n == 1:
            return 1
        elif n in self.cache:
            return self.cache[n]
        else:
            c = self.__call__(collatz_step(n))
            self.cache[n] = c + 1
            return c + 1

chainlen = ChainCache()

def max_length(x):
    maxlen = 0
    value = 0
    for i in range(1, x):
        newlen = chainlen(i)
        if newlen > maxlen:
            maxlen = newlen
            value = i
    return value, maxlen

        
if __name__ == "__main__":
    print("Problem 14")
    print("Find the number under 1 million that produces the longest Collatz") 
    print("sequence (intermediate steps in the chain may exceed 1 million).")
    t1 = time.time()
    answer = max_length(1000000)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
