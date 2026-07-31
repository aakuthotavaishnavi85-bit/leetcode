# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        slow= head 
        fast=head 
        temp=head 
        count=0
        while temp:
            count+=1
            temp=temp.next

        while fast and fast.next:
            if count%2==0:
                slow=slow.next
                fast=fast.next.next 
                if fast is None:
                    return slow 
            else:
                slow=slow.next 
                fast=fast.next.next
                if fast.next is None:
                    return slow
        