import time
import numpy as np


def doubles(maxk: int, maxn: int) -> float:
	"""
	Calculate the sum of a series up to the specified maximum values for k and n.

	The function computes the sum of 1 / (k * (n + 1) ** (2 * k)) for each combination
	of k and n within the range 1 to maxk and 1 to maxn, respectively. This series
	converges towards a specific value as maxk and maxn increase.

	Parameters:
	- maxk (int): The maximum value of k to be used in the series.
	- maxn (int): The maximum value of n to be used in the series.

	Returns:
	- float: The sum of the series for the given ranges of k and n.
	"""
	
	k = np.arange(1, maxk + 1)[:, np.newaxis]
	n = np.arange(1, maxn + 1)
	
	# To prevent overflow, we need to use logarithms for large exponentiation
	log_term = -np.log(k) - 2 * k * np.log(n + 1)
	term = np.exp(log_term)
	
	return np.sum(term)


# Testing the function with debug prints
start = time.time()

a = doubles(1, 10)  # Expected: 0.5580321939764581
b = doubles(10, 1000)  # Expected: 0.6921486500921933
c = doubles(10, 10000)  # Expected: 0.6930471674194457
d = doubles(20, 10000)  # Expected: 0.6930471955575918

end = time.time()

print("Results:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("Time taken:", end - start)
