# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        1. Count the Size of Linked Lists
        2. Convert them into a proper number
        3. Add them and generate the linked list again
        """
        
        str_l1 = []
        str_l2 = []
        
        while l1:
            str_l1.append(str(l1.val))
            l1 = l1.next
        str_l1.reverse()
        print(str_l1)
        
        while l2:
            str_l2.append(str(l2.val))
            l2 = l2.next
        str_l2.reverse()
        print(str_l2)
        
        l1_num = int(''.join(str_l1))
        l2_num = int(''.join(str_l2))
        print(l1_num+l2_num) 
        
        add = str(l1_num+l2_num)
        
        str_res = list(add)
        str_res.reverse()
        print(str_res)

        result = ListNode(int(str_res[0]))
        n = len(str_res)
        root = None
        for i in range(n-1,-1,-1):
            root = self.insert(root,int(str_res[i]))
            # print(root.val)
        return root            
    
    def insert(self, root, item):  
        temp = ListNode(0)
        # temp = ListNode(item)
        temp.val = item
        temp.next = root  
        root = temp 
        return root  
        
        
        
        
#         count_l1 = 0
#         count_l2 = 0
#         sum_l1 = 0
#         sum_l2 = 0
        
#         lst = ListNode(str(0))
        
#         while l1!=None:
#             sum_l1 = sum_l1 + l1.val*(10**count_l1)
#             count_l1 += count_l1
#             l1 = l1.next
           
#         while l2!=None:
#             sum_l2 = sum_l2 + l2.val*(10**count_l2)
#             count_l2 += count_l2
#             l2 = l2.next
            
#         result = sum_l1 + sum_l2
        
#         res_str = str(result)
#         size_res = len(res_str)
        
#         while size_res!=-1:
#             lst.val = res_str[size_res-1]
#             lst = lst.next
#             size_res -= 1
#         return lst
        
        