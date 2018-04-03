* 偶然间在微信公众号(开源优测)看到pytest的实例介绍，就追溯到[官网](https://docs.pytest.org/en/latest/getting-started.html#install-pytest)，进行详细了解。
#[ Pytest介绍](http://blog.csdn.net/liuchunming033/article/details/46501653)
* 非常容易上手，入门简单，文档丰富，文档中有很多实例可以参考
* 能够支持简单的单元测试和复杂的功能测试
* 支持参数化
* 执行测试过程中可以将某些测试跳过，或者对某些预期失败的case标记成失败
* 支持重复执行失败的case
* 支持运行由nose, unittest编写的测试case
* 具有很多第三方插件，并且可以自定义扩展
* 方便的和持续集成工具集成

# 安装pytest
   1.安装方法 
 pip install -U pytest

   2.查看安装的版本
pytest --version
结果：This is pytest version 3.4.1, imported from python安装路径\lib\site-packages\pytest.py

# 实例一（官网实例）

1、定义被测试函数func，将传递进来的参数加1后返回
2、定义测试函数 test_answer对func进行测试
3、test_answer中利用断言进行结果验证
4、将代码保存，命名为test_sample.py
```
def func(x):
    return x +1

def test_answer():
    assert func(3)==5
```
运行结果：在test_sample.py所在目录下执行pytest或者pytest -q（q是quiet的简拼），会寻找以test开头的py文件，找到文件后，在文件中找到以test开头函数并执行。
测试结果为F，并在FALURES中输出部分详细的错误原因，实际是 assert func(3)==5出现问题了，错误的原因是 4 = func(3)而我们的断言是 func(3)=5
```
E:\python3file>pytest -q
F                                                                        [100%]
================================== FAILURES ===================================
_________________________________ test_answer _________________________________

    def test_answer():
>       assert func(3)==5
E       assert 4 == 5
E        +  where 4 = func(3)

test_reqesrs_pytest_demo.py:31: AssertionError
1 failed in 0.22 seconds

```

# 实例二（多个测试样例）

 多个测试样例，可以将其放到一个测试类中：
```
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
```
# 编写pytest测试样例的规则
* 测试文件以test_开头（以_test结尾也可以）
* 测试类以Test开头，并且不能带有 __init__ 方法
* 测试函数以test_开头
* 断言使用基本的assert即可

