#z-*-coding:utf-8-*-

if __name__ == "__main__":
    str_1 = "1234567890"
    str_2 = "abcdefABCDEF"
    str_3 = "12345abcdeABCDE"
    str_4 = "abcdef"
    str_5 = "ABCDEF"
    str_6 = "    "
    str_7 = " sfsdf "
    str_8 = 'fasdfasfasdf..,./,./,./'

    print("str_3.isalnum"+str(str_3.isalnum()))
    print("str_8.isalnum"+str(str_8.isalnum()))

    print("str_1.isdigit"+str(str_1.isdigit()))
    print("str_8.isdigit"+str(str_8.isdigit()))


    print("str_2.isalpha"+str(str_2.isalpha()))
    print("str_8.isalpha"+str(str_8.isalpha()))


    print("str_4.islower"+str(str_4.islower()))
    print("str_5.islower"+str(str_5.islower()))

    print("str_5.isupper"+str(str_5.isupper()))
    print("str_4.isupper"+str(str_4.isupper()))

    print("str_7.isspace"+str(str_6.isspace()))
    print("str_8.isspace"+str(str_8.isspace()))
