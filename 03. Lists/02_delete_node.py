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
        self.head = None
        for data in data_list:
            self.insert_end(data)

    def remove_node(self, node):
        itr = self.head

        if itr.data == node:
            self.head = itr.next
            itr = None
            return

        while itr is not None:
            if itr.data == node:
                break
            prev = itr
            itr = itr.next
        prev.next = itr.next
        itr = None

    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, end = " ")
            itr = itr.next

def main():
    A = LinkedList()
    A.insert_values([1, 2, 3, 4, 5, 6])
    print("Original List is: ")
    A.print_list()
    A.remove_node(6)
    print("\nRevised List is: ")
    A.print_list()

if __name__ == "__main__":
    main()