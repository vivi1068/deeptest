#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


import  time



def show_time(f):
    def inner():

        start = time.time()
        f()
        end = time.time()
        print("%s" % (end - start))
    return  inner
@show_time
def foo():


    print("foo. .....")
    time.sleep(1)

@show_time
def bar():

    print("bar. .....")
    time.sleep(1)

bar()
foo()
# foo=show_time(bar)
# foo()