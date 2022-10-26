# Be able to capture different string lengths that have no repeating characters
# Capture which string length is the greatest
# Output the longest string length

class Solution:
    def lengthOfLongestSubString(self,str):
        strings = [""]
        i = 0
        for letter in str:
            if strings[i].find(letter) == -1:
                strings[i].
