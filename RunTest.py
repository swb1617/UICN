# 导包
import unittest

from BeautifulReport import BeautifulReport

from main import test_UI


# 构建测试集
def suite():
    # 创建一个测试套件
    suites = unittest.TestSuite()
    # 将测试用例加载到测试套件中
    loader = unittest.TestLoader()  # 创建一个用例加载对象
    suites.addTest(loader.loadTestsFromTestCase(test_UI))
    return suites


if __name__ == '__main__':
    report = BeautifulReport(suite())
    report.report(filename='TestReport.html', description='自动化测试报告', log_path='.', report_dir='.')
