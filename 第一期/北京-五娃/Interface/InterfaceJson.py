# __author__ ='wuwa'
# -*- coding: utf-8 -*-

# dumps 无文件操作，dump 序列化+文件写入 通俗解释就是将python对象转换为json字符串
# loads 无文件操作，load 反序列化+文件读取 通俗解释就是将已编码的json字符串转变为python对象
import json


class jsondemo():
    def pythonobject_to_json(self, seq):
        """
        将python对象转为json字符串
        :param seq:
        :return:
        """
        json_str = json.dumps(seq)
        return json_str

    def json_to_pythonobject(self, seq):
        """
        将json字符串转为python对象
        :param seq:
        :return:
        """
        python_obj = json.loads(seq)
        return python_obj

    def pythonobject_to_json_writefile(self, seq, fp):
        """
        将python对象转为json字符串，并以可读性格式写入文件中
        :param seq:
        :param fp:
        :return:
        """
        with open(fp, 'w') as f:
            json.dump(seq, f, sort_keys=True, indent=4, separators=(',', ': '))

            f.close()

    def readfile_json_to_pythonobject(self, fp):
        """
        读取文件中的json串
        :param fp:
        :return:
        """
        with open(fp, 'r') as f:
            json_fp = json.load(f)
        f.close()
        return json_fp


if __name__ == "__main__":
    # json字符串
    data = [{'a': 1, 'b': 2, 'c': 53, 'd': 4, 'e': 56}]
    # 实例化
    eg = jsondemo()
    # python对象转为json
    json_str1 = eg.pythonobject_to_json(data)
    print(json_str1)
    print(type(json_str1))
    print("----------------------------")
    # 以可读性格式输出data内容
    print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
    python_obj = eg.json_to_pythonobject(json_str1)
    print(python_obj)
    print(type(python_obj))
    # 将json写入文件
    eg.pythonobject_to_json_writefile(data, fp='data.json')
    # 读取文件中的json
    fp_r_data = eg.readfile_json_to_pythonobject(fp='data.json')
    print(fp_r_data)
