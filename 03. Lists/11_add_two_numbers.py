class ListNode(object):
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, num1, num2):
        return self.recursiveAddHelper(num1, num2, 0)

    def recursiveAddHelper(self, num1, num2, carry):
        val = num1.val + num2.val + carry
        carry = val // 10

        sum_num = ListNode(val % 10)

        if num1.next != None or num2.next != None:
            if not num1.next:
                num1.next = ListNode(0)
            if not num2.next:
                num2.next = ListNode(0)
            sum_num.next = self.recursiveAddHelper(num1.next, num2.next, carry)
        elif carry:
            sum_num.next = ListNode(carry)

        return sum_num


num1 = ListNode(2)
num1.next = ListNode(4)
num1.next.next = ListNode(3)

num2 = ListNode(5)
num2.next = ListNode(6)
num2.next.next = ListNode(4)

answer = Solution().addTwoNumbers(num1, num2)
while answer:
    print(answer.val, end = " ")
    answer = answer.next