from dataclasses import dataclass
from traceback import print_list


class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        # self.head = None
        for data in data_list:
            self.insert_end(data)

    def remove_duplicates(self, linkedlist):
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            while next_node is not None and next_node.data == current_node.data:
                next_node = next_node.next
            current_node.next = next_node
            current_node = next_node
        return linkedlist

    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, "-->", end='')
            itr = itr.next
        print("None")

def main():
    A = LinkedList()
    A.insert_values([1, 1, 3, 4, 4, 4, 5, 6, 6])
    A.print_list()
    A.head = A.remove_duplicates(A.head)
    A.print_list()

if __name__ == "__main__":
    main()