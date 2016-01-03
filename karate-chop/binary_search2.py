import unittest

def search(x, tab):
	start = 0

	while len(tab) > 0:
		pivot = len(tab) / 2;

		if x < tab[pivot]:
			tab = tab[:pivot]
		elif x > tab[pivot]:
			tab = tab[pivot + 1:]
			start += pivot + 1
		else:
			return pivot + start

	if tab == []:
		return -1

	return -1


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