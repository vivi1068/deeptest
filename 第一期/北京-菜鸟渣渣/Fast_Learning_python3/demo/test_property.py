# coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def get_score(self):
        return self.__score

    @get_score.setter
    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score


s = Student('Bob', 59)
s.set_score = 100
print(s.get_score)
ws = {}
for col in ("A", "B", "C", "D", "E", "F"):
    ws["%s1" % col] = "开源优测"
for i in ws.items():
    print(i, ws.get(i))

print("helhelehle")

print("423423")
print(end="\n")
print("rerwer")

for x  in (1,2):
    print("wwwww",end=" \2f   ")
    print(x)
