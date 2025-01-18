# File: tests/test_search_algos.py

from john_guttag_book_excercises.search_algos import find_root


def test_find_root_positive_integer():
	result = find_root(27, 3, 0.01)
	assert abs(result ** 3 - 27) < 0.01, f"Expected root close to 3, but got {result}"


def test_find_root_negative_integer_odd_power():
	result = find_root(-27, 3, 0.01)
	assert abs(result ** 3 + 27) < 0.01, f"Expected root close to -3, but got {result}"


def test_find_root_negative_integer_even_power():
	result = find_root(-16, 2, 0.01)
	assert isinstance(result, str), f"Expected error message, but got {result}"
	assert result.startswith("Error:"), f"Unexpected error message format: {result}"


def test_find_root_small_number():
	result = find_root(0.001, 3, 0.0001)
	assert abs(result ** 3 - 0.001) < 0.0001, f"Expected root close to 0.1, but got {result}"


def test_find_root_large_number():
	result = find_root(1000000, 2, 0.1)
	assert abs(result ** 2 - 1000000) < 0.1, f"Expected root close to 1000, but got {result}"


def test_find_root_edge_case_zero():
	result = find_root(0, 3, 0.0001)
	assert result == 0, f"Expected root 0, but got {result}"


def test_find_root_precision_edge():
	result = find_root(2, 2, 0.000001)
	assert abs(result ** 2 - 2) < 0.000001, f"Expected root close to sqrt(2), but got {result}"


def test_find_root_invalid_epsilon():
	result = find_root(2, 2, -0.1)
	assert isinstance(result, float), f"Expected a float result, but got {result}"

test_find_root_invalid_epsilon()
