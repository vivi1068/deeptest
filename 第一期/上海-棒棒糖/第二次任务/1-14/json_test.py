__author__='棒棒糖'
import json
if __name__=='__main__':
    #json转dict串示例
    print('json转dict')
    json_str='{"name": "棒棒糖", "url": "www.testingunion.com", "id": "DeepTest"}'
    #查看原类型
    print('原类型：',type(json_str))
    # 转成dict对象
    json_dict=json.loads(json_str)
    print('转后类型：', type(json_dict))
    #遍历字典
    for (x,y) in json_dict.items():
        print(x,':',y)

    #dict转json串示例
    print('dict转json')
    json_dict={"name": "棒棒糖", "url": "www.testingunion.com", "id": "DeepTest"}
    print('原类型：', type(json_dict))
    # 将字典转换成json串
    json_str=json.dumps(json_dict)
    print('转后类型：', type(json_str))
    print(json_str)

    json_demo = """
            {
                "weixin": [
                    {
                        "name": "开源优测",
                        "uid": "DeepTest",
                        "desc": "分享开源测试技术"
                    },
                    {
                        "name": "开源优测_demo",
                        "uid": "DeepTest_demo",
                        "desc": "分享开源测试技术_demo"
                    }
                ],
                "web": [
                    {
                        "url": "www.testingunion.com",
                        "name": "开源优测社区",
                        "desc": "分享各类开源测试技巧"
                    },
                    {
                        "url": "www.testingunion.com_demo",
                        "name": "开源优测社区_demo",
                        "desc": "分享各类开源测试技巧_demo"
                    }
                ]
            }
        """
    # 将json串转换成字典
    json_dict = json.loads(json_demo)
    #遍历
    for (x,y) in json_dict.items():
    # 输出第一层级
        print(x,':',y)
        for data in y:
        #输出第一层,列表
            for (data_x,data_y) in data.items():
            #遍历列表中的字典
                print("    ",data_x,':',data_y)