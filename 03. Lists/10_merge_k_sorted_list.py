class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for i in range(len(data_list)):
            self.insert_at_end(data_list[i])

    
    def merge_k_lists_util(lis1, list2):
        if list1 and not list2:
            return list1

        if list2 and not list1:
            return list2

        dummmy = itr = Node()

        while list1 and list2:
            if list1.data < list2.data:
                itr.next = list1
                list1 = list1.next
            else:
                itr.next = list2
                list2 = list2.next
            itr = itr.next

        if list1:
            itr.next = list1

        if list2:
            itr.next = list2

        return dummmy.next

    def merger_k_lists(self):
        pass
        
    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, end= ' ')
            itr = itr.next
        print()

if __name__ == "__main__":
    nums1 = [1, 2, 3]
    L1 = LinkedList()
    L1.insert_values(nums1)
    L1.print_list()

    nums2 = [4, 5]
    L2 = LinkedList()
    L2.insert_values(nums2)
    L2.print_list()

    nums3 = [5, 6]
    L3 = LinkedList()
    L3.insert_values(nums3)
    L3.print_list()

    nums4 = [7, 8]
    L4 = LinkedList()
    L4.insert_values(nums4)
    L4.print_list()

    array = [L1.head, L2.head, L3.head, L4.head]
    K = len(array)
    # print(len(array))

    # L5 = LinkedList()
    
