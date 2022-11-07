from collections import Counter

nums = [2,2,1,1,1,2,2]



def majorityElement(nums):
   return Counter(nums).most_common(1)[0][0]

print(majorityElement(nums))