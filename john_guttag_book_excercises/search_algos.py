""" number**root - y == 0 -> x**root == y -> x == sqrt(y)"""


def find_root(x: float, power: float, epsilon: float) -> float | str:
	if x < 0 and power % 2 == 0:
		return f"Error: {x} is negative and the power is even. A negative number must have an off power to cancel out the negative sign."
	low = min(-1.0, x)
	high = max(1.0, x)
	guess = (high + low) / 2
	while (current := abs(guess ** power - x)) >= abs(epsilon):
		print(f"current: {current}, low: {low}, high: {high}, guess: {guess}")
		if guess ** power < x:
			low = guess
		else:
			high = guess
		guess = (high + low) / 2
	return guess


number = float(input("You want to find the nth root of what number?: "))
root = float(input("What root?: "))
eps = float(input("What epsilon?: "))

a = find_root(x=number, power=root, epsilon=eps)
print(
	f"The nth root of {number} is about {a}.\n"
	f"The error is {abs(a**root - number)}."
	)
