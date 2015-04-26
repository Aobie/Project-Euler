import time
import math

def printTiming(func):
   def wrapper(*arg):
       t1 = time.time()
       res = func(*arg)
       t2 = time.time()
       print ('%s took %0.3f ms' % (func.__name__, (t2-t1)*1000.0))
       return res
   return wrapper

def isEven(n):
	if n % 2 == 0:
		return True
	else:
		return False

def isPrime(n): #determine if n is a prime number
	if isEven(n) and n != 2:
		return False
	else: 
		#One 'shortcut' to finding a prime is only to check for factors
		#between 3 and the ceiling of the square root of the number
		#for example factors of 100 are: 1x100, 2x50, 4x25, 5x20, 10x10, 20x5, 25x4, 50x2, 100x1
		#everything after 10x10 is a repeat of the factors discovered beforehand
		s = math.ceil(math.sqrt(n)) + 1 #add one since the range function does not include the terminal value
		for x in range (3, s): #loop through 3 to the square root of the entered value
			if n % x == 0:
				return False
		else: #went through the loop without finding any factors
			return True #Therefore number must be prime
			
def getPrimes(n): #return a list of all prime numbers up to but NOT including n
	primeslist = []
	for x in range (2, n): 
		if isPrime(x):
			primeslist.append(x)
	else:
		return primeslist

def get_all_factors(n):
	factorslist = []
	for x in range (2, math.ceil(math.sqrt(n))):
		if n % x == 0:
			factorslist.append(x)
			factorslist.append(int(n/x))
	else:
		return factorslist
		
def listPrimeComponents(n): #return a list of all prime factors of n
	t1 = time.time()
	x = 2
	primefactors = []
	while x * x <= n:
		if n % x:
			x += 1
		else:
			n //= x
			primefactors.append(x)
	if n > 1:
		primefactors.append(n)
	t2 = time.time()
	tfinal = (t2-t1)*1000.0
	print (tfinal, " ms to calculate.")	
	return primefactors
		
def getLargestPrimeFactor(n):
	if isPrime(n):
		return n
	else:
		primes = listPrimeComponents(n)
		primes.sort()
		return primes[-1]
	
def getLargestPrimeFactorFast(n):
	x = 2
	while x * x <= n:
		if n % x:
			x += 1
		else:
			n //= x
	return n
	
def main(n):
	import time
	t1 = time.time()
	answer = getLargestPrimeFactorFast(n)
	t2 = time.time()
	tfinal = (t2-t1)*1000.0
	print ('Updated')
	print ('Largest prime factor of ', n, ' is: ', answer)
	print (tfinal, " ms to calculate.")
	
