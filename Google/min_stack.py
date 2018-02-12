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
"""
Keep stack1 for storing elements and stack2 that stores min element.
Have a min variable that stores the min value in the stack.
Every push operation will do the following:
    push an element into the stack1.
    if the min value variable is greater than the current element,
        set the min value to the current element
    push the min value to the stack2

Every pop operation will do the following:
    pop an element from stack1:
    pop an element from stack2 which is actually the min element computed when the item was inserted into the stack.
    
getmin will return the minimum value stored in the variable.
"""
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

    def pop(self):
        """
        :rtype: void
        """

    def top(self):
        """
        :rtype: int
        """

    def getMin(self):
        """
        :rtype: int
        """



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()