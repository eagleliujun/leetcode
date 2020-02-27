"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""

class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)


class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.element = []
        self.data = []
        self.mindata = 'inf'

    def push(self, x: int) -> None:
        if self.data == []:
            self.mindata = x
            self.element = [x, x]
            self.data.append(self.element)
        else:
            if x < self.mindata:
                self.mindata = x
            self.element = [x, self.mindata]
            self.data.append(self.element)

    def pop(self) -> None:
        self.data.pop()
        if self.data != []:
            self.mindata = self.data[-1][1]

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]

class MinStack3:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mindata = []
        self.data = []

    def push(self, x: int) -> None:
        if self.data == [] or x <= self.mindata[-1]:
            self.mindata.append(x)
        self.data.append(x)

    def pop(self) -> None:
        if self.data[-1] == self.mindata[-1]:
            self.mindata.pop()
        self.data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.mindata)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()