def isHappy(n):
    nums = set()
    while n != 1:
        n = sum(list(map(lambda x: x**2, [ int(num) for num in str(n)])))
        if n in nums:
            return False
        nums.add(n)

    return True
    


print(isHappy(2))
