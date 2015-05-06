#Euler 15
import time

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def gridpaths(row, col):
    moves = row + col
    #the number of possible routes can be determined by treating the path
    #as a combination of Down and Right moves where we don't care about order
    #so we need row + col moves and need to choose rows(20) of Downs out of moves(40) 
    #moves! / (rows! * columns!)
    answer = (factorial (moves)) / (factorial(row) * factorial(col))
    return answer
        
if __name__ == "__main__":
    print("Problem 15")
    print("Find the number of possible paths in a 20x20 grid.")
    t1 = time.time()
    answer = gridpaths(20, 20)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
