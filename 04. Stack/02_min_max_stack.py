class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minmaxstack = []

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return

    def pop(self):
        if len(self.minmaxstack) > 0:
            self.minmaxstack.pop()
        return self.stack.pop()

    def push(self, number):
        min_max = {"min": number, "max": number}
        if len(self.minmaxstack) > 0:
            last_number = self.minmaxstack[len(self.minmaxstack) - 1]
            min_max["min"] = min(last_number["min"], number)
            min_max["max"] = max(last_number["max"], number)
        self.minmaxstack.append(min_max)
        self.stack.append(number)

    def getMinStack(self):
        return self.minmaxstack[len(self.minmaxstack) - 1]["min"]

    def getMaxStack(self):
        return self.minmaxstack[len(self.minmaxstack) - 1]["max"]

if __name__ == "__main__":
    Stack = MinMaxStack()
    Stack.push(4)
    Stack.push(5)
    Stack.push(1)
    print("Top Element in Stack Is: ", Stack.peek())
    print("Max Element in Stack Is: ", Stack.getMaxStack())
    print("Min Element in Stack Is: ", Stack.getMinStack())
    Stack.pop() 
    # Stack.pop()
    print("Top Element in Stack Is: ", Stack.peek())
    print("Max Element in Stack Is: ", Stack.getMaxStack())
    print("Min Element in Stack Is: ", Stack.getMinStack())
    