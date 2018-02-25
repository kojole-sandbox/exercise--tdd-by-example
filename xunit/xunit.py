class TestResult:
    def __init__(self):
        self.run_count = 0
        self.error_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.error_count += 1

    def summary(self):
        return '{} run, {} failed'.format(self.run_count, self.error_count)


class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def run(self, result):
        result.test_started()
        self.setup()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.teardown()

    def teardown(self):
        pass


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class WasRun(TestCase):
    def setup(self):
        self.log = "setup "

    def teardown(self):
        self.log += "teardown "

    def test_method(self):
        self.log += "test_method "

    def test_broken_method(self):
        raise Exception


class TestCaseTest(TestCase):
    def setup(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert(test.log == "setup test_method teardown ")

    def test_result(self):
        test = WasRun('test_method')
        test.run(self.result)
        assert(self.result.summary() == '1 run, 0 failed')

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        test.run(self.result)
        assert(self.result.summary() == '1 run, 1 failed')

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        assert(self.result.summary() == '1 run, 1 failed')

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_broken_method'))
        suite.run(self.result)
        assert(self.result.summary() == '2 run, 1 failed')


def main():
    suite = TestSuite()
    suite.add(TestCaseTest('test_template_method'))
    suite.add(TestCaseTest('test_result'))
    suite.add(TestCaseTest('test_failed_result'))
    suite.add(TestCaseTest('test_failed_result_formatting'))
    suite.add(TestCaseTest('test_suite'))
    result = TestResult()
    suite.run(result)
    print(result.summary())


if __name__ == '__main__':
    main()
