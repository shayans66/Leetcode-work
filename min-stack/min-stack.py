class MinStack:
    
    head = None

    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, val, None)
        else:
            # self.head.next = Node(val, min(self.head.val, val), None)
            print(self.head.val, val, min(self.head.val, val),end=' ')
            print('be4',self.head.min,end=' ')
            self.head = Node(val, min(self.head.min, val), self.head)
            print('aftr',self.head.min)
        
    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val


    def getMin(self) -> int:
        return self.head.min


class Node:
    def __init__(self,val,min,next):
        self.val = val
        self.min = min
        self.next = next
            

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()