class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head != None:
            new_node.next = self.head
        self.head = new_node

    def insert_values(self, data_list):
        for i in range(len(data_list)):
            self.insert_at_head(data_list[i])

    def merge_lists(self, list1, list2):
        if list1 and not list2:
            return list1

        if list2 and not list1:
            return list2

        dummy = itr = Node()
        # itr = dummy

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
        elif list2:
            itr.next = list2

        return dummy.next

    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, "-->", end = "")
            itr = itr.next
        print("")

if __name__ =="__main__":
    nums1 = [1, 3, 4]
    nums2 = [1, 2, 4, 5]
    L1 = LinkedList()
    L1.insert_values(nums1[::-1])
    L1.print_list()
    L2 = LinkedList()
    L2.insert_values(nums2[::-1])
    L2.print_list()
    L3 = LinkedList()
    L3.head = L3.merge_lists(L1.head, L2.head)
    L3.print_list()

    

        