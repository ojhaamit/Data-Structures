class Node:
    def __init__(self, data = None, next = None):
        self.data = data #given data
        self.next = next #given next to None

class LinkedList:
    def __init__(self) -> None:
        self.head = None #Initializing head to None

    def insert_head(self, data):
        new_node = Node(data) #create a new node
        if self.head != None:
            new_node.next = self.head #link new node to head
        self.head = new_node #make new_node as head

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

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # def delete_at_index(self, index):
    #     if index < 0 or index >= self.get_length():
    #         raise Exception("Invalid Index")

    #     if index == 0:
    #         self.head == self.head.next
    #         return
        
    #     count = 0
    #     itr = self.head

    #     while itr:
    #         if count == index - 1:
    #             itr.next = itr.next.next
    #             break
    #         itr = itr.next
    #         count += 1


    # def delete_head(self, data):
    #     temp = self.head
    #     if self.head != None:
    #         self.head = self.head.next
    #         temp.next = None
    #     return temp

    def is_empty(self):
        if self.head is None:
            return None

    def print_list(self):
        itr = self.head #iterator for traversing the list
        elem = ""
        while itr is not None:
            elem += str(itr.data) + '-->'
            itr = itr.next

        print(elem)

    
def main():
    A = LinkedList()
    # print("Inserting 1st at head")
    # a1 = input()
    # A.insert_head(a1)
    # print("Inserting 2nd at head")
    # a2 = input()
    # A.insert_head(a2)
    # print("Inserting 3nd at head")
    # a3 = input()
    # A.insert_end(a3)
    # print("Print List : ")
    # A.print_list()
    print("Inserting data list")
    A.insert_values(["banana", "orange", "grapes", "mango"])
    print("Print List : ")
    A.print_list()
    print("Print List Lentgh: ")
    print(A.get_length())
    # A.delete_at_index(0)
    # print("Print New List : ")
    # A.print_list()

    # A.delete_head()
    # print("Delete Tail")
    # A.print_list()

if __name__ == "__main__":
    main()

    