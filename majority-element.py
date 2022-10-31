nums = [10,7,7,7,7,7,1,1,1,1,1,1,11,1,1,1,1,100,100,100,100,100,100,100]

def majorityElement(nums):
    s= set()
    count = 0
    final = 0
    for num in nums:
        if num in s:
            continue
        else:
            if nums.count(num) > count:
                count = nums.count(num)
                final = num
            s.add(num)

    return final

print(majorityElement(nums))