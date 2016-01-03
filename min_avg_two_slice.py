def solution(A):
	minimal = 10001
	minStart = -1
	i = 0

	while i < len(A):
		last = A[i]
		j = i + 1
		while j < len(A):
			last = last + A[j]
			average = last / (j - i + 1 * 1.0)

			if average < minimal:
				minimal = average
				minStart = i
			j += 1
		i +=1

	print minStart
	return minStart

if __name__ == "__main__":
	assert solution([4, 2, 2, 5, 1, 5, 8]) == 1, "1st example"
	assert solution([10000, -10000]) == 0, "2 example"
	print "OK!"