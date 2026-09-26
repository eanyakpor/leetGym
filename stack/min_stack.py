'''
RAMPER
R - Restate the problem
    design a stack the supports the speicifed methods
    push pop top getMin top 
    all methods must be implmeented in constant time 
    
    methods pop, top and getMin will be called non empty stacks always 

A - ask any questions 
    can i use stack functions? 
    or do i just need another data structure 
    to use to perform the constant operations on the input
M - make an example 
    [-2,-1,0]
    push -2 
    push -1 
    push 0
pop // 0
getMin // -2 
array doesn't have to be indecreasing order it seems
P - pick a pattern
    stack / maybe hashing for quick lookup
E - explain the plan
    create a stack array
    im thinking have the values, what gets pushed into the tstack be the keys the indicies whats on the stack be the values 
    so if you pop on the stack
    stack[myMap[stack.pop()]]
    would need to then delete from the map

'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)

        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
