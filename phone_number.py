# Create a dict that map each number to an array of letters
# Create a function that split the numbers in digit and returns the letters associated
# For each number in each string add the combinations together
# If digits doesnt contain numbers between 2-9 return ""


digits = "456"

def letterCombinations(digits):
    phone_num = {
        2: ["a","b","c"],
        3:["d","e","f"],
        4:["g","h","i"],
        5:["j","k", "l"],
        6: ["m","n","o"],
        7:["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9:["w", "x", "y", "z"]
    }

    if digits == "":
        return []
    
    elif len(digits) == 1:
        return phone_num[int(digits)]

    else :
        letters = [phone_num[int(num)] for num in digits]
        final =[]
        for letter in letters[0]:
            for num in range(1,len(letters)):
                        final.append("")
                        final
    
        return final
print(letterCombinations(digits))
