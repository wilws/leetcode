from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head = temp = ListNode(0)
        temp = ListNode(0)
        head = temp
        while list1 and list2: 
            if list1.val < list2.val:
                temp.next = list1 # ans next Node
                list1 = list1.next
            else:
                temp.next = list2 # ans next Node
                list2 = list2.next # move next
                print(temp)
                print(head)

            temp = temp.next # ans move next
            print(temp)
            print(head)
        temp.next = list1 or list2 # remain things
        print(temp)
        print(head)
        return head.next
       



list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
list2 =  ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))



solution = Solution()
a = solution.mergeTwoLists(list1,list2)

while a:
    print(a.val)
    a = a.next
# print(a.val)
# print(a.next.val)
# print(a.next.next.val)
# print(a.next.next.next.val)
# print(a.next.next.next.next.val)
# print(a.next.next.next.next.next.val)