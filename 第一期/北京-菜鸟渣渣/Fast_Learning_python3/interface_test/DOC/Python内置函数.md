# <center> Python 内置函数总结</center>
1.    abs()　绝对值或复数的模

            print(abs(-6))#>>>>6
 
2.    all()　接受一个迭代器，如果迭代器的所有元素都为真，那么返回True，否则返回False

            print(all([1,0,3,6]))#>>>>False
 
3.    any()　接受一个迭代器，如果迭代器里有一个元素为真，那么返回True,否则返回False

        print(any([0,0,0,[]]))#>>>>False
 
4.  ascii()　调用对象的__repr__()方法p，获得该方法的返回值.  

            print(ascii([1,2,3,1,22,123]))#>>>>>[1, 2, 3, 1, 22, 123]
 
5.   bin()　将十进制转换为二进制

            print(bin(10))#>>>>>0b1010
 
6.  oct()　将十进制转换为八进制

            print(oct(7))#>>>>>>0o7
 
7.  hex()　将十进制转换为十六进制

            print(hex(15))#>>>>>>0xf

8.  bool()　测试一个对象是True还是False.  

            print(bool([]))#>>>>>False

9.  bytes()　将一个字符串转换成字节类型

            s="apple"
            v=bytes(s,encoding="utf-8")
            print(v)#>>>>>>b'apple'

10.  str()　将字符类型/数值类型等转换为字符串类型  

            s=100  
            print(type(s))#>>>><class 'int'>  
            s=str(s)  
            print(type(s))#>>>><class 'str'>  


11.  challable()　判断对象是否可以被调用，能被调用的对象就是一个callables对象，比如函数

            print(callable(str))#>>>>>True

12.  chr()　查看十进制数对应的ASCII字符

13.  ord()　查看某个ascii对应的十进制数

            print(ascii(12323))#>>>>12323
 
14.  classmethod()　用来指定一个方法为类的方法，由类直接调用执行，只有一个cls参数,执行类    的方法时，自动将调用该方法的类赋值给cls.  没有此参数指定的类的方法为实例  方法。

15.  complie()　将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译。

        compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

        将source编译为代码或者AST对象。代码对象能过通过exec语句来执行或者eval()进行求值。

            参数source：字符串或者AST（abstract syntax trees.  对象。

            参数filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。

            参数model：指定编译代码的种类。可以指定'exec', 'eval', 　'single'。

            参数flag和dont_inherit：这两个参数为可选参数。

            s  = "print('helloworld')"
            r = compile(s, "<string>", "exec")
            print(r)#>>>>>>><code object <module> at 0x0000000000B426F0, file"<string>", line 1>
 
16.   complex()　创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。如果第一个参数是字符串，则不需要指定第二个参数。

            print(complex("123"))#>>>>(123+0j)
 
17.  delattr()　删除对象的属性

18.  dict()　创建数据字典  


            print(dict())#>>>>>>{}
 
19.  dir()　不带参数时返回当前范围内的变量，方法和定义的类型列表，带参数时返回参数的属性 , 方法列表。

            print(dir())#>>>>>['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'r', 's']
 
20.  divmod()　　分别取商和余数  

            print(divmod(10,3))#>>>>>(3, 1)
21.  enumerate()　返回一个可以枚举的对象，该对象的next()方法将返回一个元组。

            s = ["a","b","c"]
            for i ,v in enumerate(s,1):
                print(i,v)#>>>>>1 a  2 b   3 c
	 
22.  eval()　1.  将字符串str当成有效的表达式来求值并返回计算结果2.  取出字符串中内容

            s = "1 + 3 +5"
            print(eval(s))#>>>>>>9
 
23.  exec()　执行字符串或complie方法编译过的字符串，没有返回值

24.  filter()　过滤器，构造一个序列，等价于[ item for item in iterables if function(item)]，在函数中  设定过滤条件，逐一循环迭代器中的元素，将返回值为True时的元素留下，形成一个filter类型数据。

            filter(function, iterable)

            参数function：返回值为True或False的函数，可以为None。

            参数iterable：序列或可迭代对象。

            def uno(x):
                return x > 10
            v=filter(uno,[1,11,2,45,7,6,13])
            print(v)#>>>>><filter object at 0x0000000001143160>
            
25.  float()　讲一个字符串或整数转换为浮点数。

            print(float(11))#>>>>>11.  0
 
26.  format()　格式化输出字符串，format(value, format_spec)实质上是调用了value的__format__(format_spec)方法。

            print("i am {0},age{1}".  format("tom",18))#>>>>>>i am tom,age18
 
27.  frozenset()　创建一个不可修改的集合。

            frozenset([iterable])

      set和frozenset最本质的区别是前者是可变的，后者是不可变的。当集合对象会被改变时（例如删除，添加元素.  ，只能使用set，

      一般来说使用fronzet的地方都可以使用set。

      参数iterable：可迭代对象。

28.  getattr()　获取对象的属性

            getattr(object, name [, defalut])

            获取对象object名为name的特性，如果object不包含名为name的特性，将会抛出AttributeError异常；如果不包含名为name的特性

            且提供default参数，将返回default。

            参数object：对象

            参数name：对象的特性名

            参数default：缺省返回值

29.  globals()　返回一个描述当前全局变量的字典
        
            a = "apple"
            print(globals())#>>>>>{'__name__': '__main__', '__package__': None, '__cached__': None, 'a': 'apple','__loader__': <_frozen_importlib_external.  SourceFileLoader object at 0x00000000006A5B70>, '__file__': 'D:/pycharm/pythonS3/内置函数.  py', '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__doc__': None}
 
30.  hasattr()，hasattr(object，name)判断对象object是否包含名为name的特性（hasattr是通过调用getattr(object，name).  是否抛出异常来实现的。

            print(hasattr(dict,"get"))#>>>>True
31.   hash()　哈希值hash(object)注意：可哈希的即不可变数据类型，不可哈希即可变数据类型

            如果对象object为哈希表类型，返回对象object的哈希值。哈希值为整数，在字典查找中，哈希值用于快递比价字典的键。

            两个数值如果相等，则哈希值也相等。

32.  help()　返回对象的帮助文档

       调用内建的帮助系统，如果不包含参数，交互式帮助系统将在控制台启动。如果参数为字串，则可以是模块，类，方法等名称，并且帮助页面将会在控制台打印。参数也可以         为任意对象

33.  id()　返回对象的内存地址

            a = 1
            print(id(a))#>1519780304
 
34.   input()　　获取用户输入内容

            print(input("aaa"))#>>>>>aaa
 
35.   int()　将一个字符串或数值转换为一个普通整数int([x[,radix]])

        如果参数是字符串，那么它可能包含符号和小数点。参数radix表示转换的基数（默认是10进制.  。

        它可以是[2,36]范围内的值，或者0。如果是0，系统将根据字符串内容来解析。

        如果提供了参数radix，但参数x并不是一个字符串，将抛出TypeError异常；

        否则，参数x必须是数值（普通整数，长整数，浮点数.  。通过舍去小数点来转换浮点数。

        如果超出了普通整数的表示范围，一个长整数被返回。

        如果没有提供参数，函数返回0。

       

            s = "123"
            print(type(s))#>>>>><class 'str'>
            s=int(s)
            print(type(s))#>>>>><class 'int'>
 
36.   isinstance()　检查对象是否是类的对象，返回True或False，isinstance(obj, cls)

            检查obj是否是类cls的对象, 返回True 或 False

            class Foo(object):
                pass
            obj = Foo()
            print(isinstance(obj, Foo))#>>>>>True
 
37.  issubclass()　检查一个类是否是另一个类的子类。返回True或False，，，issubclass(sub, super)

            检查sub类是否是super类的派生类（子类.  。返回True 或 False

                class Foo(object):
                    pass
                class Bar(Foo):
                    pass
                print(issubclass(Bar, Foo))#>>>>>>True
 
38.  iter()　iter(o[, sentinel])

            返回一个iterator对象。该函数对于第一个参数的解析依赖于第二个参数。

            如果没有提供第二个参数，参数o必须是一个集合对象，支持遍历功能（__iter__()方法.  或支持序列功能（__getitem__()方法.  ，

            参数为整数，从零开始。如果不支持这两种功能，将处罚TypeError异常。

            如果提供了第二个参数，参数o必须是一个可调用对象。在这种情况下创建一个iterator对象，每次调用iterator的next()方法来无

            参数的调用o，如果返回值等于参数sentinel，触发StopIteration异常，否则将返回该值。

39.  len()　返回对象长度，参数可以是序列类型（字符串，元组或列表.  或映射类型（如字典.  

            s = "ajljflajfl"
            print(len(s))#>>>>>10
 
40.  list()　列表构造函数。

41.  locals()　打印当前可用的局部变量的字典

42.  map()　map(function, iterable,.  .  .  )

        对于参数iterable中的每个元素都应用fuction函数，并将结果作为列表返回。

        如果有多个iterable参数，那么fuction函数必须接收多个参数，这些iterable中相同索引处的元素将并行的作为function函数的参数。

        如果一个iterable中元素的个数比其他少，那么将用None来扩展改iterable使元素个数一致。

        如果有多个iterable且function为None，map()将返回由元组组成的列表，每个元组包含所有iterable中对应索引处值。

            li = [1,2,3]
            data = map(lambda x :x*100,li)
            print(type(data))#>>>>>><class 'map'>
            data = list(data)
            print(data)#>>>>>>>[100, 200, 300]
 
43.  max()　返回给定元素里最大值，max(iterable [,args.  .  .  ][, key])

            如果只提供iterable参数，函数返回可遍历对象（如：字符串，元组或列表.  中最大的非空元素。

            如果提供多个参数，那么返回值最大的那个参数。

            可选参数key是单参数的排序函数。

            如果提供key参数，必须是以命名的形式，如：max(a, b, c, key = fun)

44.  meoryview()

45.   min()　返回给定元素里最小值，min(iterable [,args.  .  .  ][, key])，具体用法跟max()相同

46.  next()　返回一个可迭代数据结构（如列表.  中的下一项

47.  object()　获取一个新的，无特性(geatureless)对象。Object是所有类的基类。它提供的方法将在所有的类型实例中共享。

48.  open()　打开文件open(filename [, mode [, bufsize]])

            打开一个文件，返回一个file对象。 如果文件无法打开，将处罚IOError异常。

            应该使用open()来代替直接使用file类型的构造函数打开文件。

            参数filename表示将要被打开的文件的路径字符串；

            参数mode表示打开的模式，最常用的模式有：'r'表示读文本，'w'表示写文本文件，'a'表示在文件中追加。

            Mode的默认值是'r'。

            当操作的是二进制文件时，只要在模式值上添加'b'。这样提高了程序的可移植性。

            可选参数bufsize定义了文件缓冲区的大小。0表示不缓冲；1表示行缓冲；任何其他正数表示使用该大小的缓冲区；

            负数表示使用系统默认缓冲区大小，对于tty设备它往往是行缓冲，而对于其他文件往往完全缓冲。如果参数值被省却。

            使用系统默认值。

49.  pow(x,y,z)　幂函数,表示取x得y次幂，如果存在第三个参数z，则表示乘方结果对第三个参数取余

     

            s=pow(2,8,)
            print(s)#>>>>256
            s2=pow(2,8,5)
            print(s2)#>>>>>1
 
50.  print()　输出函数

51.  property()

52.  range()　根据需要生成一个指定范围的数字，可以提供你需要的控制来迭代指定的次数

            用于创建包含连续算术值的列表(list)。常用于for循环。参数必须是普通整数。

            参数step默认值为1，参数start的默认值为0。

            全参数调用该函数将返回一个普通整数列表。

            step 可以是正整数或者负整数。不可以为0，否则将触发ValueError异常。

53.  repr()　将任意值转换为字符串，供计时器读取的形式  repr(object)

            返回一个对象的字符串表示。有时可以使用这个函数来访问操作。

            对于许多类型来说，repr()尝试返回一个字符串，eval()方法可以使用该字符串产生对象；

            否则用尖括号括起来的，包含类名称和其他二外信息的字符串被返回。

54.  reversed()　反转，逆序对象

55.  round()　四舍五入round(x [, n])

            对参数x的第n+1位小数进行四舍五入，返回一个小数位数为n的浮点数。

            参数n的默认值是0。结果是一个浮点数。如round(0.  5)结果为1.  0

56.  set()　将对象转换成集合

57.  setattr()　　与getattr()相对应

58.  slice()　　切片功能

            s = ["a","b""c","d"]
            print(slice(1,3,s))
                            
59.  sorted()　　排序

            列表排序，按数轴方向排

            高阶函数，以绝对值大小排序

            字符串排序，按照ASCII的大小排序

            如果需要排序的是一个元组，则需要使用参数key，也就是关键字。

            反向排序，reserve=True

60.  sum()　求和
                
61.  tuple()　元组构造函数

62.  type()　显示对象所属的类型

63.  zip()　将对象逐一配对

