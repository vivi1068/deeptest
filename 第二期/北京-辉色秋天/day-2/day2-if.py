#-*-coding:utf-8-*-

if __name__ == "__main__":

    ss = input("请任意输出")

    if ss.isalnum():
        if ss.isdigit():
            print("all digit")
            if int(ss) > 1000:
                print("ss > 1000")
            else:
                print("ss< 1000")
        elif ss.isalpha():
            print("they are  all letter") 
        else:
            print("digit and letters")
    elif ss.isspace():
        print("they are all space")
    else:
        print("随机字符")
