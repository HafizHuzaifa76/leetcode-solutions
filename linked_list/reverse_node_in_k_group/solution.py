# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = head.next
        previous = head
        group_prev = dummy

        while current:
            next_node = self.reverse_nodes(current, previous, group_prev, k)
            if not next_node :
                break
            group_prev = previous
            previous = next_node
            current = next_node.next


        return dummy.next

    def reverse_nodes(self, c: Optional[ListNode], p: Optional[ListNode], d: Optional[ListNode], k: int) -> Optional[ListNode]:
        next_node = c
        check = 1
        while next_node:
            next_node = next_node.next
            check += 1
            if check == k:
                break
        if check < k:
            return None
        

        i = 1
        while c:
            if i == k:
                break
            temp = d.next
            d.next = c
            p.next = c.next
            c.next = temp

            c = p.next
            i += 1
        return c