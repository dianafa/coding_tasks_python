def isHappy(n):
	"""
	:type n: int
	:rtype: bool
	"""
	visited = [n]
	res = checkHapiness(n, visited)

	return res

def checkHapiness(n, visited):
	sum = 0
	strN = str(n)

	for letter in strN:
		m = int(letter)
		sum += m * m

	if sum == 1:
		return True
	if sum in visited:
		return False

	visited.append(sum)
	return checkHapiness(sum, visited)

if __name__ == "__main__":
	assert isHappy(19) == True
	assert isHappy(1) == True
	assert isHappy(12) == False
	assert isHappy(2) == False