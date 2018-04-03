#-*- coding:utf-8 -*-

if __name__ == "__main__":
    demo_str = "  我的前  后 和 中 间  都有空格  "
    print("原字符串是:%s"%demo_str)

    print("左侧去空格")
    print(demo_str.lstrip())

    print("右侧去空格")
    print(demo_str.rstrip())

    print("左右去空格")
    print(demo_str.strip())
