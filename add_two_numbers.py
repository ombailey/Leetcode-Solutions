# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1 = ListNode(l1)
        l2 = ListNode(l2)

        dummy = ListNode()
        tail = dummy
        sum = 0

        while l1 and l2:
            sum += l1.val
            sum += l2.val
            l1 = l1.next
            l2 = l2.next
             
        return sum

l1 = [2,4,3]
l2 = [5,6,4]
example = Solution()
print(example.addTwoNumbers(l1,l2))