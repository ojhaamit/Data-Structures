class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

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

    def binary(self):
        num = self.head.data
        itr = self.head

        while itr.next:
            num = num*2 + itr.next.data
            itr = itr.next

        print("\nthe numeric representation is: ", num)


    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, end = " ")
            itr = itr.next

def main():
    A = LinkedList()
    A.insert_values([1, 0, 1])
    print("Original List is: ")
    A.print_list()
    A.binary()


if __name__ == "__main__":
    main()