class QueueWithStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self,item):
        self.stack_in.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeueing from empty stack")
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def peek(self):
        if self.is_empty():
            raise IndexError("peeking in to empty list")
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]
if __name__ == "__main__":
    q = QueueWithStacks()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(f"Front element peek: {q.peek()}")
    print(f"Dequeued: {q.dequeue()}")
    print(f"Dequeued: {q.dequeue()}")

