def solution(A):
    tab = sorted(A)
    if tab[0] != 0:
    	return 0;

    start = 0
    result = check_position(tab, start)

    print "result:"
    print result

    return result

def check_position(tab, start):
	print "****\ntab:"
	print tab
	print "start:"
	print start
	if len(tab) == 2:
		if tab[0] == start and tab[1] == start + 2:
			return tab[0] + 1
		elif tab[0] > start:
			return start - 1 
		else: return tab[1] + 1
	elif len(tab) == 1:
		if tab[0] > start:
			return start;
		else: return start + 1;
	else:
		pivot = len(tab)/2
		print "pivot:"
		print pivot
		if tab[pivot] > start + pivot: #zrabane z przodu
			print "tab[pivot] > start + pivot"
			return check_position(tab[:pivot], start)
		else: #tab[pivot] <= pivot zrabane z tylu
			return check_position(tab[pivot:], tab[pivot])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert solution([1,8,5,2,4,6,0,7]) == 3, "[1,8,5,2,4,6,0,7] == 3"
    assert solution([1,8,5,2,3,6,0,7]) == 4, "[1,8,5,2,3,6,0,7] == 4"
    assert solution([1,8,4,2,3,6,0,7]) == 5, "[1,8,4,2,3,6,0,7] == 5"
    assert solution([1,7,5,2,4,6,0]) == 3, "[1,7,5,2,4,6,0] == 3"
    assert solution([1,7,5,2,3,6,0]) == 4, "[1,7,5,2,3,6,0] == 4"
    assert solution([1,7,4,2,3,6,0]) == 5, "[1,7,4,2,3,6,0] == 5"
    assert solution([1,7,4,2,3,6,5]) == 0, "[1,7,4,2,3,6,5] == 0"
    assert solution([2, 3, 1, 4]) == 0, "ostatni"
    assert solution([2, 3, 1, 5, 0]) == 4, "ostatni"