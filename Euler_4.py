#Euler Problem 4
#Largest palindromic number made from the product of two 3-digit numbers
import math
import time

def get_digits(n): #returns the number of digits
    #This only reliably works for numbers with less than 15 digits
    if n <= 99999999999999:
        digits = math.floor(math.log10(n))+1
        return digits
    else:
        return None

def is_palindrome(n):
    length = get_digits(n)
    fulcrum = int(math.floor(length/2))
    #print ("Fulcrum: ", fulcrum)
    for x in range(fulcrum + 1):
        modulo = 10 ** x
        divisor = 10 ** (length - x)
        #print ("X: ", x)
        #print ("Modulo-test: ", n % modulo)
        #print ("Divisor-test: ", int(n / divisor))
        if x > 1:
            right_test = int((n % modulo) / (10 ** (x - 1)))
            z = x
            while z > 1:
                left_test = int(n/divisor) % (10 ** (z - 1))
                z -= 1
            
        else:
            right_test = n % modulo
            left_test = int (n / divisor)
        #print ("Right_test: ", right_test)
        #print ("left_test: ", left_test)
        if left_test != right_test:
            return False
    else:
        return True

def largest_palindrome_flex(n):
    minimum = (10 ** (n-1))
    maximum = ((10 ** n) - 1)
    largest = 0
    left_list = list(range(minimum, maximum + 1))
    right_list = left_list
    x, y = -1, -1
    while x >= -len(left_list):
        y = -1
        while y >= -len(right_list):
            number = (left_list[x]) * (right_list[y])
            if is_palindrome(number):
                if number > largest:
                    largest = number
            y -= 1
        x -= 1
    else:
        return largest
        
def largest_palindrome():
    #looking for the largest palindrome between 10000 and 998001
    t1 = time.time()
    answer = largest_palindrome_flex(3)
    t2 = time.time()
    print ("Largest palindrome: ", answer)
    print ((t2-t1)*1000.0, " ms")
    return None
