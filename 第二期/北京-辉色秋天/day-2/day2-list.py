# -*- coding:utf-8 -*-
if __name__ == "__main__":

    list1 = [1,2,3,4,5,6,7,8,9]

    print("len(listq1)=%d"%len(list1))

    print("max(list1) is %d"%max(list1))
    print("min(list1) is %d"%min(list1))

    tuple1 = (2,3,5,6,)
    list2 = list(tuple1)
    print(list2)
   
    list2.append("xx")
    print(list2)

    list2.append("xx")
    print(list2)
    print("xx长度是%d"%list2.count('xx'))

    list2.extend(list1)
    print(list2)
    
    list2.insert(2,"ddafsdfa") 
    print(list2)

    list2.pop()
    print(list2)
    list2.pop(2)
    print(list2)

    list2.remove(2)
    print(list2)
    list2.reverse()
    print(list2)


    list2.remove("xx")
    list2.remove("xx")
    list2.sort()
    print(list2)

    list3 = list2.copy()
    print(list3)
    list2.clear() 
    print(list2)

    list3[3] = "sdfasdfasdf"
    print(list3)


    print(list3[::-1])
    print(list3[0::3])
