# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def get_linked_list_size(self, head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count
    def add_zeros(self, i, size, num):
        while size > i:
            num *= 10
            i += 1
        return num
    def create_list(self, sumNum):
        l3 = ListNode(0)
        current = l3

        while sumNum >= 10:
            digit = sumNum % 10
            current.next = ListNode(digit)
            current = current.next
            sumNum = sumNum // 10

        current.next = ListNode(sumNum)
        return l3.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        size = self.get_linked_list_size(l1)
        size_loop = size
        while l1 is not None:
            num1 += self.add_zeros(size_loop, size, l1.val)
            l1 = l1.next
            size_loop -= 1

        num2 = 0
        size = self.get_linked_list_size(l2)
        size_loop = size
        while l2 is not None:
            num2 += self.add_zeros(size_loop, size, l2.val)
            l2 = l2.next
            size_loop -= 1

        sumNum = num1 + num2
        return self.create_list(sumNum)