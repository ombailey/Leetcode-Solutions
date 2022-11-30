def intersection(n1,n2):
    short = n1
    long = n2
    ans = set()
    
    if len(n2) < len(short):
        short = n2
        long = n1

    for num in short:
        if num in long:
            ans.add(num)

    return list(ans)

nums1 = [1,2,2,1]
nums2 =[2,2]

print(intersection(nums1,nums2))