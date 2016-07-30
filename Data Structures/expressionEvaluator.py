class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def top(self):
        return self.stack[self.size() - 1]

    def size(self):
        return len(self.stack)

def evaluator(string):
    length = len(string)
    operator_stack = Stack()
    operand_stack = Stack()

    for x in range(0, length):
        item = string[x]
        print item
        if(item not in "()+-*/"):
            operand_stack.push(item)


        elif item == ')':
            operand1 = int(operand_stack.pop())
            operand2 = int(operand_stack.pop())
            operator = operator_stack.pop()

            if operator == '+':
                operand_stack.push(operand1 + operand2)
            elif operator == '-':
                operand_stack.push(operand2 - operand1)
            elif operator == '*':
                operand_stack.push(operand2 * operand1)
            elif operator == '/':
                operand_stack.push(operand2 / operand1)

        elif item in "+-/*":
            operator_stack.push(item)

    return operand_stack.pop()

print(evaluator("(2+3)"))
