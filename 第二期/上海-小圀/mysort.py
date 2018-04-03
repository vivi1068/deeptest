import random

def quicksort(list, start, end):
    if start >= end:
        return list
    num = list[start]
    i = start
    j = end
    while(i < j):
        while(i < j and list[j] >= num):
            j -= 1
        list[i] = list[j]
        while(i < j and list[i] <= num):
            i += 1
        list[j] = list[i]
            
    list[i] = num
    quicksort(list, start, i - 1)
    quicksort(list, j + 1, end)
    return list


class Mysort(object):
    def __init__(self, start, end, count):
            self.list = []
            while(count > 0):
                self.list.append(random.randint(start, end))
                count -= 1
        
    def mysort(self):    
        return quicksort(self.list, 0, len(self.list) - 1)
        
def main():
    sorted_data = Mysort(10, 1000, 100)
    print(sorted_data.mysort())
    
main()