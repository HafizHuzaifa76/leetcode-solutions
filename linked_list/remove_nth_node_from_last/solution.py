# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        t = head
        while t.next:
            t = t.next
            length += 1
        
        element = length-n
        
        if element == 0:
            return head.next
        else: 
            t = head

        for i in range(element-1):
            t = t.next
            print(i, length, t.val)

        t.next = t.next.next

        return head
