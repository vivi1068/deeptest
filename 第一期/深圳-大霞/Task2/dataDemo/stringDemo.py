__author__ = "大霞"
"""
字符串String类型练习
String内置函数join和split
"""
if __name__ == "__main__":
    num = [1,2,3,4,5]
    num.append(6)
    print(num)
    num.extend([7,8])#使用一个列表扩展为另一个列表
    print(num)
    st = ['a','b', 'o','u','t']
    st.append('est')
    print(st)
    st.insert(1,'A')
    print(st)
    st.remove('a')#remove()删除元素，remove()方法并不能删除某个位置的元素
    print(st)
    # 可以使用del知道删除某个位置的元素
    del st[0]
    print(st)
    t = ['a','1','2', '3','4', '5','6','ef','a','b']
    str_demo='_'.join(t)
    print(str_demo)
    # 将str_demo进行分割
    str_set=str_demo.split('_')
    print(str_set)