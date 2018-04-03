# -*- coding:utf-8 -*-

if __name__ == "__main__":
    dic1 = {"1":"xiaowang", "2":"xiaogong", 3:4,'d':[1,2]}
    print(dic1)

    print("len(dic1) = %d"%len(dic1))
    print(str(dic1))

    dict2 = dic1.copy()
    print(dict2)

    tuple1=(1,2,3)
    print(dict.fromkeys(tuple1,'xxxx'))

    print("dic1.get(i43)"+str(dic1.get('i43', 'd')))
    print("dic1.get(3)"+str(dic1.get(3, 'd')))
  
    print("1" in dic1)
    print("3" in dic1)
    print(dic1.items())

    print(dic1.keys())

    print(dic1.values())

    print("setdefault")
    print(dic1.setdefault("1","dddd"))
    print(dic1.setdefault("ddddddd","dddd"))

    print("dict1"+str(dic1))
    print()
    print("dict2"+str(dict2))
    print()
    dict2.update(dic1)
    print("dic2 is "+str(dict2))


    print("遍历字典")
    for key, value in dic1.items():
        print(key, value)

    print("遍历keys")
    for key in dic1.keys():
        print(key)
    
    print("遍历values")
    for value in dic1.values():
        print(value)
    
    dic1['1'] = '111111111111111111'
    print(dic1)
    
    print(dic1.clear())
