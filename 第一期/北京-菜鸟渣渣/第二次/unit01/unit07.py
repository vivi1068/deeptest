# coding=utf-8
__author__ = 'Young'
global a
def a():
 a=2
 a+=1
 print a


def do():
    a()

if __name__ == "__main__":
     do()
     print a

def scope_test():
    '''
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        # nonlocal spam
        spam = "nonlocal spam"
        '''
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    # do_local()
    # print("After local assignment:", spam)
    # do_nonlocal()
    # print("After nonlocal assignment:", spam)


scope_test().do_global()

print("After global assignment:", spam)
print("In global scope:", spam)

