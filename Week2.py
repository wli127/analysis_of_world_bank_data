def nth_power(high,n=2):
	'''
	ARGS:
	high: upper limit for integers
	RETURNS:list of integer with power n

	'''
	return (i**n for i in range(high))
	
print(list(nth_power(10)))
