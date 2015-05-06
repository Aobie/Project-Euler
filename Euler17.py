#Euler 17
import time
# 'one' = 3, 'two' = 3, 'three' = 5, etc.
# although 16 - 19 could use 6 + 'teen', small enough case to not be worth
# special processing hundred
letlen = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8,
          14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5,
          70:7, 80:6, 90:6, 100:7, 1000:8, 0:0}

#same idea as above, only using the actual phrase/string rather than char count          	
letstr = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
          8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen',
          14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
          19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
          60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred',
          1000:'thousand', 0:''}

#use character counts for each building block of the string to determine lenght
#of passed in value n
def num_word_length(n):
    if n <= 20:
        return letlen[n]
    else:
        if n >= 1000:
            # for example 'one' = 3 + 'thousand' = 8
            wordlen = letlen [int(n/1000)] + letlen[1000]
            wordlen += num_word_length (n % 1000)
            return wordlen
        elif n >= 100:
            # for example 'one' = 3 + 'hundred' = 7 + 'and' = 3
            wordlen = letlen [int(n/100)] + letlen[100]
            #only add the 3 for 'and' if not
            if n % 100:
                wordlen += 3
            wordlen += num_word_length (n % 100)
            return wordlen
        else:
            wordlen = letlen [int(n/10) * 10] + letlen [n%10]
            return wordlen

#Build the actual strings, rather than just using character counts
def num_word(n):
    if n <= 20:
        return letstr[n]
    else:
        if n >= 1000:
            # for example 'one' = 3 + 'thousand' = 8
            numstr = letstr [int(n/1000)] + letstr[1000]
            numstr += num_word (n % 1000)
            return numstr
        elif n >= 100:
            # for example 'one' = 3 + 'hundred' = 7 + 'and' = 3
            numstr = letstr [int(n/100)] + letstr[100] 
            if n % 100:
                numstr += 'and'
            numstr += num_word (n % 100)
            return numstr
        else:
            numstr = letstr [int(n/10) * 10] + letstr [n%10]
            return numstr

#Loop through the full range of n (inclusive), and return total character count
def Euler17(n):
    total = 0
    temp = 0
    for i in range(1, n + 1):
        total += num_word_length(i)
    return total

#Used for debugging purposes only
def print_words(n):
    for i in range (1, n + 1):
        print (i + ':' + num_word(i))

#Same idea as Euler17, only using strings rather than direct character counts    
def count_words(n):
    total = 0
    temp = 0
    for i in range(1, n + 1):
        total += len(num_word(i))
    return total
'''
Compare the timing of using the direct character counts vs. string manipulation.
In the end, execution time was almost identical, only noticing a 5ms difference
when calculating the range up to 9999 (max supported with current implementation).
'''

if __name__ == "__main__":
    print("Problem 17")
    print("Find the number of letters used if all numbers 1 to 1000 are")
    print("written out long hand (include 'and' in values between 100 and 999),")
    print("but not counting spaces or hyphens.")
    t1 = time.time()
    answer = Euler17(9999)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
    t1 = time.time()
    answer = count_words(9999)
    t2 = time.time()
    print((t2-t1)*1000.0, " ms")
    print(answer)
