#-*-encoding:utf-8-*-

class Stack:

    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1


    def set_size(self, size):
        self.size = size

    def is_empty(self):
        res = False
        if -1 == self.top:
            res = True

        return res

    def is_full(self):
        res = False

        if self.size - 1 == self.top:
            res = True

        return res

    def show(self):
        print(self.stack)

    def push(self, obj):
        if self.is_full():
            print("栈已满")

        else:
            self.stack.append(obj)
            self.top += 1

    def pop(self):
        if self.is_empty():
            print("已空")
        else:
            obj = self.stack.pop()
            self.top -= 1
            return obj


if __name__ == "__main__":

    stack = Stack(6)
    for i in range(6):
        stack.push(i)
    
    stack.show()
    stack.pop()
    stack.push(6)

    stack.show()
        
        
