# FIFO로 값을 받고 내는 큐. 최대 길이가 고정되어 있다
class MyCircularQueue:

    def __init__(self, k):
        self.length = 0
        self.head = 0
        self.vals = [-1 for _ in range(k)]
        self.max_len = k

    # Queue에 값을 삽입하고, 작업의 성공 여부를 반환함
    def enQueue(self, value):
        if self.length >= self.max_len:
            return False
        new_idx = (self.head + self.length) % self.max_len
        self.vals[new_idx] = value
        self.length += 1
        return True

    # Queue에서 맨앞의 값을 삭제하고, 작업의 성공 여부를 반환함
    def deQueue(self):
        if self.length <= 0:
            return False
        self.head = (self.head + 1) % self.max_len
        self.length -= 1
        return True

    # Queue 맨앞의 값을 반환한다
    def Front(self):
        return self.vals[self.head] if self.length > 0 else -1

    # Queue 맨끝의 값을 반환한다
    def Rear(self):
        return self.vals[(self.head + self.length - 1)%self.max_len] if self.length > 0 else -1
    
    # Queue가 비어있는지 여부를 반환한다
    def isEmpty(self):
        return self.length == 0

    # Queue가 꽉 차있는지 여부를 반환한다
    def isFull(self):
        return self.length == self.max_len


def test_queue(orders, args):
    assert(orders[0] == "MyCircularQueue")
    test_queue = MyCircularQueue(args[0][0])
    test_results = [None]

    for order, arg in zip(orders[1:], args[1:]):
        if order == "enQueue":
            test_results.append(test_queue.enQueue(arg[0]))
        elif order == "deQueue":
            test_results.append(test_queue.deQueue())
        elif order == "Rear":
            test_results.append(test_queue.Rear())
        elif order == "Front":
            test_results.append(test_queue.Front())
        elif order == "isEmpty":
            test_results.append(test_queue.isEmpty())
        elif order == "isFull":
            test_results.append(test_queue.isFull())
        else:
            print("No such order. Check the possible order list")

    return test_results


if __name__ == "__main__":
    assert(test_queue(["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"], [[3], [1], [2], [3], [4], [], [], [], [4], []]) == [None, True, True, True, False, 3, True, True, True, 4])
    print("All examples passed")