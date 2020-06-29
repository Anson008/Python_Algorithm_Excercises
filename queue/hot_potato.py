from queue.queue_pylist import Queue2


def hot_potato(names, num):
    q = Queue2()
    for name in names:
        q.enqueue(name)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()


if __name__ == "__main__":
    names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    times = 7
    res = hot_potato(names, times)
    print(res)