# __author__ ='wuwa'
# -*- coding: utf-8 -*-
'''
通过python list实现堆栈
特点：先进后出，例如一个死胡同一辆辆车开进去，只能末尾的先出来，其他车辆才依次可以出来
'''


class Stack:
    def __init__(self, size=10):

        # # 初始化堆栈大小
        self.size = size

        # 初始化堆栈列表
        self.stack = []

        # 初始化堆栈默认指针值
        self.top = -1

    # 设置堆栈大小
    def set_size(self, size):
        self.size = size

    # 判断堆栈是否为空
    def size_empty(self):
        res = False

        if self.top == -1:
            res = True

        return res

    # 判断堆栈是否已满
    def stack_is_full(self):
        res = False
        if self.top + 1 == self.size:
            res = True

        return res

    # 打印堆栈的内容即self.stack的内容
    def show_stack(self):
        print(self.stack)

    # 入栈
    def push(self, obj):
        if self.stack_is_full():
            raise Exception("堆栈满了，加不了")
        else:
            self.stack.append(obj)
            self.top += 1

    # 出栈
    def pop(self):
        if self.size_empty():
            raise Exception('堆栈空了，空了')
        else:
            self.top -= 1
            self.stack.pop()


if __name__ == "__main__":
    # 实例化
    stacks = Stack(5)
    #入栈
    for i in range(0, 5):
        stacks.push(i)
    #显示入栈数据
    stacks.show_stack()

    data = stacks.pop()
    stacks.show_stack()

    #总结
    # 入栈
    # 判断指针的值，是否大约等于列表的长度，若是，则弹出异常，否则添加元素，指针向后移动一位
    # 出栈
    # 判断指针的值是否小于等于0.若是则抛出异常，否则删除元素，且指针向前移动一位
