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

def listPrimeComponents(n): #return a list of all prime factors of n
	allprimes = getPrimes(n)
	primefactors = []
	for x in allprimes:
		if n % x == 0:
			primefactors.append(x)
	else:
		return primefactors
		
def getLargestPrimeFactor(n):
	primes = listPrimeComponents(n)
	return primes[-1]
