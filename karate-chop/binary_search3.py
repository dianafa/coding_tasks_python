import unittest

def search(x, tab):
	return find(x, tab, 0, len(tab) - 1)

def find(x, tab, start, end):
	if end < start:
		return -1

	if end == start:
		if tab[end] == x:
			return end
		else:
			return -1

	pivot = (start + end) / 2

	if x < tab[pivot]:
		return find(x, tab, start, pivot)
	if x > tab[pivot]:
		return find(x, tab, pivot + 1, end)

	return pivot


def test_search():
	assert search(3, []) == -1
	assert search(3, [1]) == -1
	assert search(1, [1]) == 0

	assert search(1, [1, 3, 5]) == 0
	assert search(3, [1, 3, 5]) == 1
	assert search(5, [1, 3, 5]) == 2
	assert search(0, [1, 3, 5]) == -1
	assert search(2, [1, 3, 5]) == -1
	assert search(4, [1, 3, 5]) == -1
	assert search(6, [1, 3, 5]) == -1

	assert search(1, [1, 3, 5, 7]) == 0
	assert search(3, [1, 3, 5, 7]) == 1
	assert search(5, [1, 3, 5, 7]) == 2
	assert search(7, [1, 3, 5, 7]) == 3
	assert search(0, [1, 3, 5, 7]) == -1
	assert search(2, [1, 3, 5, 7]) == -1
	assert search(4, [1, 3, 5, 7]) == -1
	assert search(6, [1, 3, 5, 7]) == -1
	assert search(8, [1, 3, 5, 7]) == -1