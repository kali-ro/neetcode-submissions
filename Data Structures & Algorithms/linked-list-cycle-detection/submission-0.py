# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        temp = True
        while slow != fast:
            if not fast or not slow:
                return False
            if temp:
                fast = fast.next
                temp = False
            else:
                slow = slow.next
                fast = fast.next
                temp = True

        return True