# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_node = ListNode(0)
        sum_node_traverse = sum_node 
        
        cross_over = 0
        while(l1 or l2):
            if l1 and l2:
                sm = l1.val + l2.val + cross_over
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sm = l1.val + cross_over
                l1 = l1.next
            elif l2:
                sm = l2.val + cross_over
                l2 = l2.next
            rem = sm%10
            sum_node_traverse.next = ListNode(rem)
            sum_node_traverse = sum_node_traverse.next
            cross_over = sm//10
            
        if cross_over > 0:
            sum_node_traverse.next = ListNode(cross_over)
            
        return sum_node.next