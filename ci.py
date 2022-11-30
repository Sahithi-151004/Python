#calculate the compound intrest for proncipal amount as 10,000 at rate of intrest 5% and number of years the amount is deposited is 7 years # Python3 program to find compound
# interest for given values.


def ci(p, r, t):
	Amount = p * (pow((1 + r / 100), t))
	ci = Amount - p
	print("Compound interest is",ci)
ci(10000, 5, 7)
