import HTMLTestRunner
import unittest
import time,os


class TestRunner(object):

    def __init__(self, cases="./"):
        self.case = cases

    def get_all_cases(self, class_name):
        return unittest.defaultTestLoader.loadTestsFromTestCase(class_name)

    def run(self, suite, tittle_text='pywinauto test report', description_text=''):
        for filename in os.listdir(self.cases):
            if filename == 'report':
                break
            else:
                os.mkdir(self.cases + '\\report')
        new = time.strftime("%Y-%M-%D-%H_%M_%S")
        filename = self.cases + '\\report\\' + new + 'result.html'
        fp = open(filename, 'wb')

        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, tittle=tittle_text, description=description_text)
        runner.run(suite)
        fp.close()


if __name__ == '__main__':
    test = TestRunner()
    test.run()