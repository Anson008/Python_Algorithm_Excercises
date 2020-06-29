class QueueMax:
    def __init__(self):
        self.entries = []
        self.max_vals = []

    def enqueue(self, x):
        self.entries.append(x)
        while self.max_vals:
            if self.max_vals[-1] >= x:
                break
            self.max_vals.pop()
        self.max_vals.append(x)

    def dequeue(self):
        if self.entries:
            res = self.entries.pop(0)
            if res == self.max_vals[0]:
                self.max_vals.pop(0)
            return res
        raise Exception("empty queue")

    def max(self):
        if self.max_vals:
            return self.max_vals[0]
        raise Exception("empty queue")


if __name__ == "__main__":
    queue_max = QueueMax()
    queue_max.enqueue(4)
    queue_max.enqueue(3)
    queue_max.enqueue(1)
    queue_max.enqueue(0)

    print("Current max:", queue_max.max())
    queue_max.dequeue()
    print("Current max:", queue_max.max())
