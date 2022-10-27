import re

def isPalindrome(string):
    string = re.sub("[^a-zA-Z0-9]", "", string).lower()
    reverse = string[::-1]
    return string == reverse

print(isPalindrome("race a car"))