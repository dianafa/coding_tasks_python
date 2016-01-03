def solution(A, B):
	i = 0
	strA = str(A)
	strB = str(B)
	result = ""

	while i < max(len(strA), strB):
		if isset(strA[i]):
			result += strA[i]
		if isset(strB[i]):
			result += strB[i]


	print result
	return result




if __name__ == "__main__":
	assert solution(5555, 4444) == 54545454, "1st example"
	assert solution(5, 4) == 54, "1st example"
	print "OK!"