# __author__ ='wuwa'
# -*- coding: utf-8 -*-

'''
特点：先进先出
队列的前端进行删除操作，后端进行加入元素操作，即队头进行删除，队尾进行插入操作
'''


class Queues(object):
    def __init__(self, size=10):
        # 初始化操作
        self.size = size

        # 初始化队列列表
        self.queue = []

        # 初始化队列前端、后端位置参数
        self.front = 0
        self.rear = -1

    # 队列为空
    def is_empty(self):
        return self.rear == 0

    # 队列为满
    def is_full(self):
        res = False
        if (self.rear - self.front + 1) == self.size:
            res = True
        return res

    # 展示队列内容
    def show(self):
        print(self.queue)

    # 入队
    def add_ietm(self, obj):
        if self.is_full():
            raise Exception('队列已满')
        else:
            self.queue.append(obj)
            self.rear += 1
            # print(self.rear)

    # 出队
    def delete_ietm(self):
        if self.is_empty():
            raise Exception('队列已空')
        else:
            self.rear -= 1
            print(self.rear)
            self.queue.pop(self.front)

    # 队列头元素
    def first(self):
        if self.is_empty():
            raise Exception("队列已空")
        else:
            return self.queue[self.front]

    # 队列尾元素
    def last(self):
        if self.is_empty():
            raise Exception("队列已空")
        else:
            return self.queue[self.rear]


if __name__ == "__main__":
    queue = Queues(5)

    for i in range(6, 11):
        queue.add_ietm(i)
    print('显示队列')
    queue.show()

    print('显示队列首个队元素', queue.first())
    print('显示队列最后一个队元素:', queue.last())

    print('删除队列队元素')
    queue.delete_ietm()
    queue.show()
    print('删除队列队元素')
    queue.delete_ietm()
    queue.show()
