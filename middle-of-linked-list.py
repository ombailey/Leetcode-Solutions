# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length +=1
            current = current.next
        
        mid = length // 2
        count = 0
     
        while head:
            if count == mid:
                return head
            head.val = None
            head = head.next
            count +=1
                
            
        