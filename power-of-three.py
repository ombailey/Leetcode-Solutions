def isPowerOfThree(n):
    count = 0
    base = 3
    final = 0
    if n < 1:
        return False
    while final < n:
        final = base ** count
        count +=1
    return final == n

print(isPowerOfThree(0))
        

