# Note: Need to make it run faster

nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
result  = []

def threeSum(nums: list[int]):
    for number in range(len(nums)):
        for num1 in range(len(nums)):
            for num2 in range(len(nums)):
                if num1==num2 or number==num2 or number==num1:
                    continue
                else:
                    if (nums[number] + nums[num1] + nums[num2]) == 0:
                        x = [nums[number], nums[num1], nums[num2]]
                        x.sort()
                        if x not in result:
                            result.append(x)
                    else:
                        continue
    return len(result)

print(threeSum(nums))

print(len([[-82,34,48],[-49,15,34],[-70,34,36],[-43,-6,49],[-43,-6,49],[-43,-6,49],[-43,-6,49],[-43,-14,57],[-43,-3,46],[-49,-3,52],[-49,21,28],[-49,13,36],[-49,13,36],[-66,-11,77],[-43,12,31],[-14,2,12],[-49,2,47],[-3,1,2],[-49,1,48],[-66,1,65],[-49,13,36],[-14,1,13],[-49,13,36],[-49,-6,55],[-82,-11,93],[-82,21,61],[-82,26,56],[-43,15,28],[-49,13,36],[-49,13,36],[-82,36,46],[-29,-14,43],[-29,1,28],[-43,10,33],[-66,10,56],[-11,1,10],[-70,-14,84],[-70,13,57],[-70,-6,76],[-70,15,55],[-66,-3,69],[-82,13,69],[-70,1,69],[-14,-3,17],[-11,-6,17],[-82,17,65],[-43,17,26],[-29,12,17],[-43,-6,49],[-43,-6,49],[-82,33,49],[-70,21,49],[-66,17,49]]))
print(len([[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]))