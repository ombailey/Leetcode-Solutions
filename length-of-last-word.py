s = "omar          is     the    best           "

def lengthOfLastWord(s):
    words = s.split()
    return len(words[-1])

print(lengthOfLastWord(s))