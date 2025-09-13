class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = None
        current_node = l3
        next_nodes = [l1, l2]
        next_nodes2 = []
        remainder = 0

        while next_nodes or remainder:
            val = 0
            while next_nodes:
                node = next_nodes.pop()
                val += node.val
                if node.next:
                    next_nodes2.append(node.next)
            val += remainder
            remainder = val // 10
            val = val % 10
            if not current_node:
                current_node = ListNode(val=val)
                l3 = current_node
            else:
                current_node.next = ListNode(val=val)
                current_node = current_node.next
            next_nodes = next_nodes2[:]
            next_nodes2 = []
        return l3
        