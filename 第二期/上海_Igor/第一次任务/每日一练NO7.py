#将一个列表的数据复制到另一个列表中。

a = [1,2,3,4]
b = a
print(a)
print(id(a),id(b)) #指向同一个地址

c = a[ : ]
print(c)
print(id(a),id(c))

d = []
for i in a :
    d.append(i)
print(d)
print(id(a),id(d))