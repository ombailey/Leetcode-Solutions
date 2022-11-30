nums = [0,1]

def missingNumber(n):
    n.sort()
    if len(n) not in n:
        return len(n)
    for num in range(len(n)):
        if num == n[num]:
            continue
        else:
            return num

print(missingNumber(nums))