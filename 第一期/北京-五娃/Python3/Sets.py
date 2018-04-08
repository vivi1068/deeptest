# __author__ ='wuwa'
# -*- coding: utf-8 -*-

'''
set()：python内置函数
返回值：返回新的集合对象
特点：无序、值唯一 可进行集合对象的并、交、差操作
'''

if __name__ == '__main__':

    #创建集合,可变集合
    sets = set('deeptest')
    print('生成新集合：', sets)

    #通过内建函数len获取集合的长度
    print('集合长度：', len(sets))

    #增加元素
    sets.add(3)
    print('add元素后的新集合：', sets)
    setnew = 'python'

    sets.update(setnew)
    print('update元素后的新集合：', sets)

    # 删除元素，discard(),值不存在也不会报错，但remove会引发KeyError错误
    # pop随机删除元素不列举例子
    sets.discard('d')
    print('discard元素后的新集合：', sets)

    sets.remove('p')
    print('remove元素后的新集合：', sets)

    #清空列表
    sets.clear()
    print('clear元素后的新集合：', sets)

    #元素在集合内是否存在 in和not in即可满足
    sets_old = set('iffen')
    sets_new = set('difference')
    if 'i' in sets_old:
        print('i元素存在于sets_old中：',True)
    else:
        print('i元素不存在于sets_old中：',False)

    #两个集合是否存在子集合issubset、issuperse
    print('sets_old中的每个元素是否在sets_new中:',sets_old.issubset(sets_new))

    # 两个集合的并集，包含两个集合的所有元素
    sets_olds = set('ienmh')
    sets_news = set('diff')
    print('并集：',sets_olds.union(sets_news))

    # 两个集合的交集，包含两个集合的相同元素
    print('交集：', sets_olds.intersection(sets_news))

