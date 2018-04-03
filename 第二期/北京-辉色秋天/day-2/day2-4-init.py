#-*-coding:utf-8-*-

import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.add_section("这是section1")
    config.set("这是section1",'key1','value1')
    config.set("这是section1",'key2','value2')
    config.set("这是section1",'key3','value3')
    config.set("这是section1",'key4','value4')
    config.set("这是section1",'key5','value5')
    config.set("这是section1",'key6','value6')
    config.set("这是section1",'key7','value7')
    config.set("这是section1",'key8','value8')

    config.add_section('这是section2')
    with open("/root/init1.init",'w') as configfile:
        config.write(configfile)

    config.read("init1.init")

    sections = config.sections()
    print(sections)

    for sec in sections:
        options = config.options(sec)

        print(options)

    for sec in sections:
        for option in config.options(sec):
            print("[%s]%s = %s"%(sec,option,config.get(sec,option)))
