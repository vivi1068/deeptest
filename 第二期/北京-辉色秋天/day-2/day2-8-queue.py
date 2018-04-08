# -*-coding:utf-8 -*-

class Queue:

    def __init__(self, size):
        self.size = size
        self.queue = []

        self.fron = 0
        self.rear = -1


    def is_empty(self):
        if -1 == self.rear:
            return True

    def is_full(self):
        res = False
        if(self.rear - self.fron == self.size -1):
            res = True

        return res

    def add(self, obj):
        if self.is_full():
            print("队列已满")
            return False

        else:
            self.queue.append(obj)
            self.rear += 1

    def delete(self):
        if self.is_empty():
            print("队列已空")
            return False

        else:
            self.rear -= 1
            return self.queue.pop(0)

    
    def get_last(self):
        if self.is_empty():
            print("队列已空")
            return False

        else:
            return self.queue[self.rear]

    def get_first(self):
        if self.is_empty():
            print("队列已空")
            return False

        else:
            return self.queue[self.fron]

    def show(self):
        print(self.queue)


if __name__ == "__main__":

    queue = Queue(5)
    print(queue.is_empty())

    for i in range(6):
        queue.add(i)

    queue.get_first()
    queue.get_last()
    queue.show()
    for i in range(6):
        print(queue.delete())
    queue.show()
