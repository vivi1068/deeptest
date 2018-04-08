# __author__ ='wuwa'
# -*- coding:utf-8 -*-
import unittest

import requests


class JsonPlactTest(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.url = "http://jsonplaceholder.typicode.com"
        self.session = requests.session()

    # 测试用例
    def test_get_posts(self):
        """
        测试获取所有用户信息接口
        :return:
        """
        r = self.session.get(self.url + "/posts")
        # print(r.json())

        # 断言 响应头信息
        self.assertEqual(r.headers["Content-Type"], "application/json; charset=utf-8")

        # 断言响应码
        self.assertEqual(r.status_code, 200)

        # 断言用户总数
        self.assertEqual(len(r.json()), 100)

    def test_get_posts_by_id(self):
        """
        测试指定用户的id
        :return:
        """
        r = self.session.get(self.url + '/posts/1')

        # 断言状态码
        self.assertEqual(r.status_code, 200)

        # 断言响应头信息
        self.assertEqual(r.headers["Content-Type"], "application/json; charset=utf-8")

        # 断言用户id
        self.assertEqual(r.json()['userId'], 1)

    def test_delete_posts_by_id(self):
        """
        测试删除用户指定id
        :return:
        """
        r = self.session.delete(self.url + '/posts/1')

        # 断言验证码
        self.assertEqual(r.status_code, 200)

        # 断言响应头信息
        self.assertEqual(r.headers["Content-Type"], "application/json; charset=utf-8")

        # 断言用户总数
        self.assertEqual(len(r.json()), 0)

    # 清理
    def tearDown(self):
        if self.session:
            self.session.close()


if __name__ == "__main__":
    print("requests unittest接口测试实例")
    unittest.main()
