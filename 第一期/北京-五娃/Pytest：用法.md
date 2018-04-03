* 获取有关版本、选项名称、环境变量的帮助
>  pytest --version  查看pytest版本
pytest --fixtures  查看内置参数
pytest -h| --help  帮助文档

* 失败后停止
> pytest -x  首次失败后停止执行
pytest --maxfail=2 两次失败后停止执行


* 执行/选择 测试
> pytest test_mod.py  直接执行模块文件
pythest  testing/   testing是一个目录 执行一个目录下的问你件
pythest -k "MyClass and not method"  执行字符串表达式中的用例
按照节点ID运行测试，每个收集到的测试都分配有一个唯一的nodeid，它由模块文件名组成，后跟类名称，函数名称和参数化参数等说明符，由::字符分隔
pytest test_mod.py::test_func  在模块中运行特定的测试
pytest test_mod.py::TestClass::test_method 指定测试类中的测试方法
pytest -m slow   slow 是装饰器的名字，此命令的额意思是将运行所有使用@ pytest.mark.slow修饰器装饰的测试
pytest --pyargs pkg.testing 将导入pkg.testing并使用其文件系统位置来查找并运行测试

* 失败时调用PDB(python调试器)
> Python带有一个名为PDB的内置Python调试器。 pytest允许通过命令行选项进入PDB提示符
pytest --pdb 每次失败时调用Python调试器
pytest -x --pdb 在第一次失败时丢弃到PDB，然后结束测试会话
pytest --pdb --maxfail = 3 在前三次失败时下降到PDB

* 获取最慢的10个测试持续时间的列表
> pytest --durations = 10

* 测试报告
> pytest可以方便的生成测试报告，即可以生成HTML的测试报告，也可以生成XML格式的测试报告用来与持续集成工具集成
pytest --resultlog=path   生成HTML格式报告
pytest --junitxml=path 生成XML格式的报告

