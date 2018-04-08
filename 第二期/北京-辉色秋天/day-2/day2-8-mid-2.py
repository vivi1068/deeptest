#-*-coding:utf-8 -*-

def find_first(obj, seq):

    start,end = 0,len(seq)-1

    while start <= end:
        mid = (end + start)//2
        
        if(mid == 0 and seq[mid] == obj) or (seq[mid] == obj and seq[mid-1]<obj):
            return mid

        elif seq[mid] > obj:
            end = mid -1

        else:
            start = mid +1

def find_last(obj, seq):

    start, end = 0, len(seq) -1

    while start <= end:
        mid = (end + start) //2

        if (mid == len(seq)-1 and seq[mid] == obj) or (seq[mid] == obj and seq[mid+1] > obj):
            return mid

        elif seq[mid] > obj:
            end = mid -1

        else:
            start = mid +1



if __name__ == "__main__":    

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15] 
    print(seq)

    print("找到first：", 1, " 索引是： ", find_first(1, seq))
    print("找到first：", 3, " 索引是： ", find_first(3, seq))
    print("找到first：", 15, " 索引是： ", find_first(15, seq))
    
    print("找到last：", 1, " 索引是： ", find_last(1, seq))
    print("找到last：", 3, " 索引是： ", find_last(3, seq))
    print("找到last：", 15, " 索引是： ", find_last(15, seq))
