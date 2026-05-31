"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {None: None}
        curr = head
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            n = map[curr]
            n.next = map[curr.next]
            n.random = map[curr.random]
            curr = curr.next
        return map[head]

        