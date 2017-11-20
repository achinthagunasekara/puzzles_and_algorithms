class ListNode(object):
    def __init__(self, x):
        self._val = x
        self._next = None

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        self._next = next_node


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l3 = ListNode(x=0)
        carry = 0
        while l1 is not None or l2 is not None:
            total = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0)
            l1, l2 = (l1.next if l1 is not None else None), (l2.next if l2 is not None else None)
            total += carry
            add = total % 10
            carry = total / 10
            l3.next = ListNode(x=add)
            l3 = l3.next
        if carry:
            l3.next = ListNode(x=carry)
        return head.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()
link_list = solution.addTwoNumbers(l1, l2)
while link_list is not None:
    print link_list.val
    link_list = link_list.next


