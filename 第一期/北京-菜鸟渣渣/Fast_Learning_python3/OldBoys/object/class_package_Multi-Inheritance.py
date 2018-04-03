# coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

'''
class F0:
    def a(self):
        print("F0.a")
class F1(F0):
    def a(self):
        print("F1.a")


class F2:
    def a(self):
        print("F2.a")

class S(F1,F2 ):
    pass

obj = S()
obj.a()
'''


class BaseRequest():
    def __init__(self):
        print("BaseRequest __init__")
        pass


class RequestsHander(BaseRequest):
    def __init__(self):
        print("RequestsHander __init__")
        pass
    def serve_forever(self):
        print("serve_forever(self):")
        self.process_request()

    def process_request(self):
        print("process_request(self):")


class Minx:
    def process_request(self):
        print("Minx process_request(self):")


class Son(Minx, RequestsHander, ):
    pass

obj=Son()
obj.serve_forever()