#-*-coding:utf-8 -*-

if __name__ == "__main__":

   t = ['l','o','v','e','i','n','g','!']

   print("- 连接字符串")
   str_demo = '-'.join(t)
   print(str_demo)

   print("以 - 分割字符")
   str_split = str_demo.split('-')
   print(str_split)

   print("合成一个新的字符串")
   str_demo = ''.join(str_split)
   print(str_demo)
