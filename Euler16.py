#Euler16
import time

#Python handles really large numbers quite well, so this is pretty simple
def sum_digits(n):
    #convert the number to a string for easy access to each digit
    tempstr = str(n)
    tempsum = 0
    #loop through the string and add the integer value of each character to total
    for i in range(len(tempstr)):
        tempsum += int(tempstr[i])
    return tempsum
    
if __name__ == "__main__":
    print("Problem 16")
    print("Find the sum of all the digits of a large exponent 2^1000.")
    t1 = time.time()
    answer = sum_digits(2 ** 1000)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
