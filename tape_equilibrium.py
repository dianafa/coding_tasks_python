#Write a function that, given a non-empty zero-indexed array A of N integers,
#returns the minimal difference that can be achieved.

def solution(A):
    min = 1000000
    min_index = -1
    sumP = 0
    sumL = 0
    
    for i in A:
        sumP += i;
        
    for index, j in enumerate(A):
        if abs(sumP-sumL) < min:
            min = abs(sumP-sumL)
            min_index = index
        sumP -= j
        sumL += j
    
    return min