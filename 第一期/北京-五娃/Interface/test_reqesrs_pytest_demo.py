# __author__ ='wuwa'
# -*- coding:utf-8 -*-
import pytest


# 测试加减法
class TestDemo:
    # 加法
    @pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 8)])
    def test_add(self, a, b, expected):
        # 求和
        sum = a + b
        # 断言
        assert sum == expected

        # 减法

    @pytest.mark.parametrize("a, b, expected", [(1, 2, -1), (8, 3, 5), (3, 4, 8)])
    def test_sub(self, a, b, expected):
        # 减法
        s = a - b

        # 断言
        assert s == expected


def func(x):
    return x +1

def test_answer():
    assert func(3)==5
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

