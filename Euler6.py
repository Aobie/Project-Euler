import time
# Brute force solution, very fast for small values of n
# O(n), becomes noticeably slow for values of 1,000,000 or higher
# n = 1,000,000 => 670ms 
def sum_square_diff(n):
    t1 = time.time()
    sumsquares, squaresums, answer = 0, 0, 0
    for x in range (n+1):
        sumsquares += x ** 2
        squaresums += x
    else:
        squaresums **= 2
    answer = squaresums - sumsquares
    t2 = time.time()
    print ((t2-t1)*1000.0, " ms")
    return answer
    
# Use handy mathematical formulas to skip the brute force
# O(1) = approximately 0 ms per this timing method   
def sum_square_ind(n): #looked up the formulas for mathematic induction
    t1 = time.time()
    squaresums = ((n * (n + 1)) / 2) ** 2
    sumsquares = (n * (n + 1) * (2 * n + 1)) / 6
    answer = squaresums - sumsquares
    t2 = time.time()
    print ((t2-t1)*1000.0, " ms")
    return answer
    
if __name__ == "__main__":
    print("Problem 6")
    print("Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.")
    answer = sum_square_ind(100)
    print(answer)
