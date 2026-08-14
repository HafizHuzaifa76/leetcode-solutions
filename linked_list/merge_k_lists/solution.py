# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional, ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        output = dummy
        c = 0

        while True:
            c += 1
            lowest_index = 0
            for i in range(len(lists)):
                lowest = lists[lowest_index]
                item = lists[i]
                if item:
                    if not lowest or item.val < lowest.val:
                        lowest_index = i
                    # print(item.val)
                # print(f'lowest: {lowest.val if lowest else None}')
                # print(f'item: {item.val if item else None}')
            if not lowest:
                break
            else:
                output.next = lowest
                output = output.next
                # print(f'output: {output.val if output else None}')
                lists[lowest_index] = lowest.next

        return dummy.next