#!/usr/bin/python

import random

# 任务1:四则运算

class Calc:
    """
    实现任意两个数的加减乘除四则运算
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self,):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        else: print("除数为0，非法")

    pass

# 任务2:100个数字排序
class Mysort:

    def __init__(self, lists):
        self.lists = lists

    def soort(self):
        bsh = 0
        ch = len(self.lists)
        for i in range(ch):
            for j in range(1, ch - i):
                if self.lists[j - 1] > self.lists[j]:
                    self.lists[j - 1], self.lists[j] = self.lists[j], self.lists[j - 1]
                    bsh += 1

            print(bsh)

        print(lists)

    def sooort(self):
        ck1 = 0
        ck2 = 0
        a = sum(self.lists) / len(self.lists)
        ch = len(self.lists)
		lll = [0]

        for kk in range(ch):
            if self.lists[ck2] > a:
                self.lists.append(self.lists(kk - ck1))
                self.lists.remove(self.lists(kk - ck1))
                ck1 += 1
            else:
                ck2 += 1
			pass

        lll = [ck2 - 1]
        a = sum(lists[0:ck2]) / ck2
		lists2 = self.lists[0:ck2]
        ck1, ck2 = 0, 0
        for kk in range(ck2):
            if lists2[ck2] > a:
                lists2.append(lists2(kk - ck1))
                lists2.remove(lists2(kk - ck1))
                ck1 += 1
            else:
                ck2 += 1
            pass

        lll.append(lll[1])
		lll[1] = ck2
        self.lists[0: ck2] = lists2
		a = sum(lists[ck2 - 1:ch]) / (ch - ck2)
		lists2 = self.lists[ck2 - 1:ch]
        ck1, ck2 = 0, 0
        for kk in range(ck2):
            if lists2[ck2] > a:
                lists2.append(lists2(kk - ck1))
                lists2.remove(lists2(kk - ck1))
                ck1 += 1
            else:
                ck2 += 1
            pass

        lll.append(lll[2] + ck2)
		self.lists[ck2 - 1: ch] = lists2
		for i in range(1,ch + 1):
			try:
				while i != lll[i]:
					ck1, ck2 = 0, 0
					lists2 = self.lists[lll[i -1]:lll[i]]
					a = sum(lists2) / len(lists2)
					for kk in range(ck2):
						if lists2[ck2] > a:
							lists2.append(lists2(kk - ck1))
							lists2.remove(lists2(kk - ck1))
							ck1 += 1
						else:
							ck2 += 1
						pass
					
					self.lists[lll[i -1]:lll[i]] = lists2
					b_len = len(lll)
					lll.append(lll[b_len])
					for j in range(1:b_len - i):
						lll[b_len - j] = lll[b_len - j - 1]
					
					lll[i] = lll[i - 1] + ck2
			except IndexError:
				ck1, ck2 = 0, 0
				lists2 = self.lists[lll[i -1]:ch]
				a = sum(lists2) / len(lists2)
				for kk in range(ck2):
					if lists2[ck2] > a:
						lists2.append(lists2(kk - ck1))
						lists2.remove(lists2(kk - ck1))
						ck1 += 1
					else:
						ck2 += 1
					pass
				
				self.lists[lll[i -1]:ch] = lists2
				lll.append(lll[i - 1] + ck2)
				
				ck1, ck2 = 0, 0
				lists2 = self.lists[lll[i -1]:lll[i]]
				a = sum(lists2) / len(lists2)
				for kk in range(ck2):
					if lists2[ck2] > a:
						lists2.append(lists2(kk - ck1))
						lists2.remove(lists2(kk - ck1))
						ck1 += 1
					else:
						ck2 += 1
					pass
				
				self.lists[lll[i -1]:lll[i]] = lists2
				b_len = len(lll)
				lll.append(lll[b_len])
				for j in range(1:b_len - i):
					lll[b_len - j] = lll[b_len - j - 1]
				
				lll[i] = lll[i - 1] + ck2
		



if __name__ == "__main__":

    a = int(input("请输入第1个数据："))
    b = int(input("请输入第2个数据："))

    calc = Calc(a, b)
    print(calc.add(), calc.sub(), calc.mul(), calc.div())
    print(calc.add() + calc.sub())

    lists = []
    for i in range(100):
        lists.append(random.randint(10, 100))

    rwu2 = Mysort(lists)
    rwu2.soort()