#Euler 18
import time

#easiest way to find the sum of each path without traversing them individually
#is to reduce the pyramid from the bottom up (evaluating the largest sum of each
#term one level at a time and replacing the upper level with the sums)
def max_sum_tripath(tri):       
    while len(tri) > 1:
        #print(tri)
        temp = []
        t0 = tri.pop() 
        t1 = tri.pop() 
        #print("New t1: ", t1)
        for i,t in enumerate(t1):
            #print(i, t, t0[i], t1)
            temp.append(max(t0[i], t0[i+1]) + t)
        tri.append(temp)
        #print("Reduce Step: ", temp)
    return tri[0][0]


if __name__ == "__main__":
    print("Problem 18")
    print("Find maximum sum path of a given triangle of numbers.")
    t1 = time.time()
    data = []
    input18 = open('Euler18.txt', 'r')
    for row in input18:
        #print(row)
        data.append(list(map(int, row.split())))
        #print(data)
    answer = max_sum_tripath(data)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
