def containsDuplicates(nums: list[int]):
    arr = set()
    answer = False
    i = 0

    while i < len(nums) and not answer:
        if nums[i] in arr:
            answer = True
        else:
            arr.add(nums[i])
        i +=1
    return answer
        

print(containsDuplicates([1,2,3,4]))
