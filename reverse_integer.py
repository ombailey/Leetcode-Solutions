numbers = -976

 
def reverse(x):
    x = str(x)[::-1]
    if x.find("-") != -1:
        list = [number for number in x]
        negative = list.pop()
        list.insert(0,negative)
        x = int("".join(list))
    x = int(x)

    if abs(x) > 2 **31-1:
        return 0
    else :
        return x
  
print(reverse(numbers))


