import script
def sum_divisor(n):
	sum = 0
	divisor = 2
	while divisor < n:
		#print(n // divisor)
		if n % divisor == 0:
			sum += n / divisor
		divisor += 1
	if n != 0:
		sum += 1
	return sum
print("summe: " + str(sum_divisor(0)) )


def sum_divisors(n):
	sum = 0
  # Return the sum of all divisors of n, not including n
	divisor = 2
	while divisor < n:
		if n % divisor == 0:
			sum += n / divisor
		divisor += 1
	if n != 0:
		sum += 1
	return sum
  
  
  
def dominoPieces(iterations):
	for leftSide in range(iterations + 1):
		for rightSide in range(leftSide,iterations + 1):
			if leftSide != rightSide:
				print("[" + str(leftSide) + "|" + str(rightSide) + "]", end=" ")
		print()

# dominoPieces(6)


def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * (x +1)
    return result
	
print(factorial(5))

#for n in range(0,10):
#    print(n, factorial(n+n))


def recursivFactorial(n):
	if n < 2:
		return 1
	return n * recursivFactorial(n-1)
	

print(recursivFactorial(5))


def recursivePrintNumber(n):
	print("Die Nummber " + str(n))
	if n == 0:
		return n
	return recursivePrintNumber(n-1)

#recursivePrintNumber(10)

def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n+1))
	
script.helloTen("Ingo")




