from robot.api import TestSuite
from robot.api import ResultWriter
from robot.model import Keyword

class BaiduTest(object):

    def __init__(self,name,librarys = ['SeleniumLibrary']):
        #创建测试套件
        self.suite = TestSuite(name)

        #导入seleniumlibrary
        for lib in librarys:
            self.suite.resource.imports.library(lib)

    def create_variables(self):
        variables = {
        "${baidu}":"http://www.baidu.com",
        "${browser}":"Chrome",
        "${search_input}":"id = kw",
        "${search_btn}":"id = su"
        }
        for k,v in variables.items():
            self.suite.resource.variables.create(k,v)

    #测试用例
    def open_browser(self):
        test_01 = self.suite.tests.create('启动浏览器')
        test_01.keywords.create("Open Browser",args = ["${baidu}","${browser}"])
        test_01.keywords.create('Title Should Be',args = ['百度一下，你就知道'])

    def search_words(self):
        test_02 = self.suite.tests.create('百度搜索测试')
        test_02.keywords.create("Input Text",args = ["${search_input}","测试教程网"])
        test_02.keywords.create("Click Button",args = ["${search_btn}"])
        test_02.keywords.create("Sleep",args = ['5s'])

    def assert_title(self):
        test_03 = self.suite.tests.create('断言结果')
        test_03.keywords.create("Title Should Be",args = ["测试教程网_百度搜索"])

    def close_browsers(self):
        test_04 = self.suite.tests.create("关闭浏览器")
        test_04.keywords.create("Close All Browsers")
        test_04.keywords.create("Sleep", args=['5s'])

    def run(self):
        self.create_variables()
        self.open_browser()
        self.search_words()
        self.assert_title()
        self.close_browsers()

        # 运行套件
        result = self.suite.run(critical="百度搜索",output="output.xml")

        # 生成日志、报告文件
        ResultWriter(result).write_results(report="report.html", log="log.html")

if __name__ == "__main__":
    print("用Python写Robot Framework测试")
    suite = BaiduTest("百度搜索测试套件")
    suite.run()
