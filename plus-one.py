def plusOne(digits):
    digits = int("".join(map(lambda x: str(x), digits))) + 1
    return [int(num) for num in str(digits)]

print(plusOne([9]))