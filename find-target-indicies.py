nums = [1,2,5,2,3]
target = 2

def targetIndicies(nums, target):
    nums.sort()
    return [index for index,num in enumerate(nums) if num == target]

print(targetIndicies(nums,target))
