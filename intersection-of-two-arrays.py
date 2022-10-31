

def intersect(nums1,nums2):
    final = []

    if len(nums1) > len(nums2):
        longer = nums1
        shorter = nums2
    else :
        longer = nums2
        shorter = nums1
    for num in shorter:
        if num in longer:
            final.append(num)
            longer.remove(num)
    
    return final

print(intersect([3,1,2], [1,1]))
    
