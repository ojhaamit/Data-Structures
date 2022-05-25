class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_head(data)

    def return_num(self):
        num = 0
        itr = self.head
        #num = itr.data
        # print(num)
        while itr:
            num = num*10 + itr.data
            itr = itr.next

        print("\nthe resulting number is: ", num)
        return int(num)

    def sum_list(self, data):
        values = []
        while data > 0:
            values.append(data%10)
            data = data//10

        # print(values)
        return values
        

    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, "-> ", end = '')
            itr = itr.next
        print("")
    
def main():
    A = LinkedList()
    A.insert_values([2, 4, 7, 1])
    print("A list is: ")
    A.print_list()
    B = LinkedList()
    B.insert_values([9, 4, 5])
    print("\nB list is: ")
    B.print_list()
    C = LinkedList()
    # C.head = C.sum_list(A.head, B.head)
    num1 = A.return_num()
    num2 = B.return_num()
    num3 = num1 + num2
    print("\nThe sum of numbers is: ", num3)
    translated_array = []
    translated_array = C.sum_list(num3)
    print(translated_array)

if __name__ == "__main__":
    main()