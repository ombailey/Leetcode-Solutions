def isPowerOfFour(n,i=0):
    if 4 ** i == n:
        return True
    elif 4** i > n:
        return False
    return isPowerOfFour(n, i+1)