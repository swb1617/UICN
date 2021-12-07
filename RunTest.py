# 导包
import unittest

from BeautifulReport import BeautifulReport
from main import test_UI


# 构建测试集
def suite():
    # 创建一个测试套件
    suite = unittest.TestSuite()
    # 将测试用例加载到测试套件中
    loader = unittest.TestLoader()  # 创建一个用例加载对象
    suite.addTest(loader.loadTestsFromTestCase(test_UI))
    return suite


if __name__ == '__main__':
    br = BeautifulReport(suite())
    br.report(filename='testdemoreport.html', description='自动化测试报告', log_path='.', report_dir='.')
