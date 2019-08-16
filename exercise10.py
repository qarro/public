#LeetCode232题，用栈实现队列
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q =[]
        self.tmp = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.tmp.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.q)==0:
            while len(self.tmp):
                self.q.append(self.tmp.pop())
        return self.q.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.q)==0:
            while len(self.tmp):
                self.q.append(self.tmp.pop())
        return self.q[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.q)==0 and len(self.tmp)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()