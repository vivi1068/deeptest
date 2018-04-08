# -*- coding:utf-8 -*-
if __name__ == "__main__":

    set1 = set([1,2,3,4,5,6])
    set2 = set("asdfasdfasdfaqws")
 

    print(set1)
    print(set2)


    set1.add(5)
    print("set1 add 5")
    print(set1)
    print("set add 10")
    set1.add(10)
    print(set1)

    set1.remove(3)
    print("set1 delete 3")
    print(set1)

    set1.update(['q','w'])
    print(set1)

    print(set1.issubset(['q','w']))
    print(set1.issuperset(['q','w']))

    print(set(['w','q']).issubset(set1))
    print(set(['w','q']).issubset(set2))

    print(set1.union(set2))
    print(set1.intersection(set2))

    print(set1.difference(set2))
