"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""


class Solution:
    def connect(self, root):
        if not root:
            return None

        node = root
        while node.left:
            head = node
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            node = node.left
        return root
