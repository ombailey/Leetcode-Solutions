# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = []
        second = []
        result = []
        head = None
        
        while l1:
            first.append(l1.val)
            l1 = l1.next
        
        while l2:
            second.append(l2.val)
            l2 = l2.next
            
        first.reverse()
        second.reverse()
        sum = (int("".join(map(lambda x: str(x),first))) + int("".join(map(lambda x: str(x), second))))
        
        for num in str(sum):
            result.append(int(num))
        
        for num in result:
            temp = ListNode(num)
            temp.next = head
            head = temp
        
        return head


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = temp = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            temp.next = ListNode(carry%10)
            temp = temp.next
            
            carry //= 10
            
        return head.next
