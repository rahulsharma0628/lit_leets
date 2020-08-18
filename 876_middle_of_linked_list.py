# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        temp = head
        length = 1
        while head.next is not None:
            head = head.next
            length += 1
        
        middle = math.ceil((length+1)/2)
        print(middle)
        
        for i in range(middle-1):
            temp = temp.next
            print(temp.val)        
        return temp
            