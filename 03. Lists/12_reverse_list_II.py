class Node(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __repr__(self):
        result = str(self.value)
        if self.next:
            result += str(self.next)
        return result

class Solution:
    def reverse_list(self, node):
        current = node
        previous = None

        while current != None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous


node = Node(1, Node(2, Node(3, Node(4, Node (5)))))
print(Solution().reverse_list(node))