# __author__ ='wuwa'
# -*- coding: utf-8 -*-

"""
1. 格式：dict = {key:value}，{}表示字典，键-值对的方式存储数据，键值使用“：”分开，每一组键值对用“，”分隔
2. 键是唯一的，可以字符串、数字、元组，但是不可用列表，因为列表是可变的（可变类型不能作为字典的key）
3. 值是不唯一的，可以是列表、字典或其他可变类型
4. 支持的方法，对字典进行遍历、修改、删除
5. 参考文档python3 API等
6. 字典是python语言中唯一的映射类型
7. 键值对是一对一的关系
8. 字典是无序的
"""

if __name__ == "__main__":
    #通过hash可以判断字典的key支持的类型
    print(hash(()))

    dicts = {'phone': 1234454,'name': 'john', 'age': 12}

    # 获取字典的长度,通过python的内置函数“len”获取字典长度
    print('获取字典的长度:', len(dicts))

    # 增加新的键值对或者更新健的值，如果该key不存在字典中，则增加该键值对，若存在则改变值
    dicts['sex'] = 'boy'
    print('增加键值对的字典:', dicts)

    # 删除某个键，如果该键不存在与这个字典中会抛出keyError
    del dicts['age']
    print('删除某个键的字典:', dicts)

    # 判断key是否存在于字典中, 存在则返回True，否则返回False
    print('存在返回True：','phone' in dicts)

    if 'phone' in dicts:
        print('phone存在于dicts')

    # 字典拷贝
    dicts_new = dicts.copy()
    print('拷贝后新生成的字典:', dicts_new)

    # 返回指定key的value，若无value值，则返回默认值，若没有设置默认值，则返回None，不会抛出keyerror异常
    dicts_olds = {'phone': 'hhhh', 'test': 'tests'}

    dicts_old = dicts_olds.get('phone')
    print('显示指定key的值:', dicts_old)

    dicts_new_value = dicts_olds.get('python', 'hello python')
    print('显示默认值:', dicts_new_value)

    dicts_new_value_1 = dicts_olds.get('python3')
    print('显示默认值:', dicts_new_value_1)

    # 返回包含所有键值对元组的列表，样例[('name', 'john'), ('phone', 1234454), ('sex', 'boy')]
    dicts_value = dicts.items()
    print('显示所有key value:', dicts_value)
    # 遍历字典列表
    for key, values in dicts_value:
        print(key, values)

    # 显示字典所有的key，以列表方式返回结果
    print('打印所有的key:', dicts.keys())

    for key in dicts.keys():
        print ('key=%s,value=%s' %(key,dicts[key]))

    #通过迭代器来访问,通过sorted对字典排序，得到有序的key的值
    print('---------------我是分割线-------------')
    for key in sorted(dicts):
        print ('key=%s,value=%s' %(key,dicts[key]))


    # 显示字典所有的value，以列表方式返回结果
    print('打印所有的values:', dicts.values())

    # 创建一个新的字典 fromkeys(seq, value),seq是一个列表
    deicts_new_value_2 = {}.fromkeys([1, 2, 3], 'python')
    print('创建一个新的字典', deicts_new_value_2)

    # 删除指定key，并返回key对应的值
    print('删除指定的key:', dicts.pop('sex'))

    # 删除字典中的item，字典的最后一组key-value，并显示删除的key-value
    print('删除字典最后一组键值对且返回删除的内容:', dicts.popitem())

    # 给字典中的key设置默认值,如果key存字典中，且有值则返回key本身的值，
    # 若key不存在字典中，则返回默认值，若key不存在字典中，且无默认值，则返回None
    print('设置setdefault前dicts的值:', dicts)
    dicts.setdefault('name', 'oooo')
    dicts.setdefault('sex', 'lalala')
    dicts.setdefault('sex1')
    print(dicts)

    # 合并两个字典
    dicts.update({"hello": 'python', 'hi': 'python3'})
    print(dicts)
