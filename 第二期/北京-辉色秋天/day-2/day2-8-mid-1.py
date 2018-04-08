#-*-coding:utf-8-*-

def find_t(obj, seq):
    start, end = 0, len(seq)-1

    while start <= end:
        mid = (start + end) //2
        val = seq[mid]

        if obj == val:
            return mid

        elif obj >val:
            start = mid+1

        elif obj < val:
            end = mid-1

    return None



if __name__ == "__main__":
    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    print(seq)

    print("找到：", 5, " 索引是： ", find_t(5, seq))
    print("找到：", 15, " 索引是： ", find_t(15, seq))
    print("找到：", 3, " 索引是： ", find_t(3, seq))
