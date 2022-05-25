class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head != None:
            new_node.next = self.head
        self.head = new_node

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_head(data)

    def middle(self):
        first_pointer = self.head
        second_pointer = self.head

        while second_pointer and second_pointer.next:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next
        
        print("\nthe middle element is: ", first_pointer.data)


    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, end = " ")
            itr = itr.next

def main():
    A = LinkedList()
    A.insert_values([1, 2, 3, 4, 5])
    print("Original List is: ")
    A.print_list()
    A.middle()


if __name__ == "__main__":
    main()