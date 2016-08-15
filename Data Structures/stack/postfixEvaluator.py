class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return self.stack == []
    def peek(self):
        return self.stack[self.size() - 1 ]
    def size(self):
        return len(self.stack)

def infix2postFix(string):
    opStack = Stack()
    result = ""
    expression = string.split(" ")

    for x in expression:
        if x == "(":
            opStack.push(x)
        elif x == ")":
            if opStack.peek() == "(":
                opStack.pop()
            else:
                while(opStack.peek() != "("):
                    result+=opStack.pop() + " "
                opStack.pop()
        elif x in "abcdefghijklmnopqrstuvwxyz" or x in "1234567890":
            result += x + " "

        elif x in "+-/*" and opStack.size() > 0:
            if opStack.peek() in "*/+-":
                while(prec[opStack.peek()] >= prec[x]):
                    result+=opStack.pop() + " "
            opStack.push(x)

        elif x in "+-/*" and opStack.size() == 0:
            opStack.push(x)

    stackLeft = opStack.size()
    while(stackLeft > 0):
        stackLeft -=1
        result += opStack.pop() + " "

    return result[:-1]


def evaluatePostFix(expression):
    listExpression = expression.split(" ")
    operandStack = Stack()
    operatorStack = Stack()

    for x in listExpression:
        if x in "1234567890":
            operandStack.push(x)
        elif x in "*/+-":
            operatorStack.push(x)


    while(operatorStack.size() > 0):
        a = int(operandStack.pop())
        b = int(operandStack.pop())

        sym = operatorStack.pop()

        if sym == "+":
            operandStack.push(a+b)
        elif sym == "-":
            operandStack.push(a-b)
        elif sym == "/":
            operandStack.push(a/b)
        elif sym == "*":
            operandStack.push(a*b)

    return operandStack.pop()

exp = raw_input("Enter = ")
print(evaluatePostFix(infix2postFix(exp)))
