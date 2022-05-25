class StackUsingList:
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) -1]
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def push(self, number):
        self.stack.append(number)


if __name__ == "__main__":
    Stack = StackUsingList()
    Stack.push(3)
    print(Stack.peek())