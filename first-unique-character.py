s = "leetcode"

def firstUniqChar(s):
    for letter in s:
        if s.count(letter) == 1:
            return s.index(letter)

    return -1

print(firstUniqChar("unique"))
