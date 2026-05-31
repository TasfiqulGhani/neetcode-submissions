"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node1: Optional['Node']) -> Optional['Node']:
            map={}
            def clone(node:Node):
                new_node = map.get(node)
                if new_node:
                    return new_node
                
                new_node = Node(val=node.val)
                map[node]=new_node
                for neighbor in node.neighbors:
                    new_node.neighbors.append(clone(neighbor))
                return new_node
            return clone(node1) if node1 else None