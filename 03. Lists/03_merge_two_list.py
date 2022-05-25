class Node:
    def __init__(self, data=None, next=None):
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

    def merge_lists(self, list1, list2):
        if list1 is None:
            return list2

        elif list2 is None:
            return list1

        elif list1.data < list2.data:
            list1.next = self.merge_lists(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_lists(list1, list2.next)
            return list2  

    def print_list(self):
        itr = self.head
        elems = ""
        while itr is not None:
            print(itr.data, end = " ")
            elems += str(itr.data) + "-->"
            itr = itr.next
        # print(elems)


def main():
    A = LinkedList()
    A.insert_values([1,2,3,4])
    print("List A: ")
    A.print_list()
    B = LinkedList()
    B.insert_values([1,2,4])
    print("\nList B: ")
    B.print_list()
    C = LinkedList()
    C.head = C.merge_lists(A.head, B.head)
    print("\nList C: ")
    C.print_list()

if __name__=="__main__":
    main()