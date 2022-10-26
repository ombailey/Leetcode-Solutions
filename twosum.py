def twoSum(list, target):
        for num in range(len(list)):
            for second_num in range(num+1, len(list)):
                if list[num] + list[second_num] == target:
                    return [num,second_num]
        
# Test Case
nums = [6,2,8,9]
target = 14
    
print(twoSum(nums, target))