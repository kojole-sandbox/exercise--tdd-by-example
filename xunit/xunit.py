class TestResult:
    def __init__(self):
        self.run_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self):
        return '{} run, 0 failed'.format(self.run_count)


class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.setup()
        method = getattr(self, self.name)
        method()
        self.teardown()
        return result

    def teardown(self):
        pass


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
    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert(test.log == "setup test_method teardown ")

    def test_result(self):
        test = WasRun('test_method')
        result = test.run()
        assert(result.summary() == '1 run, 0 failed')

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        result = test.run()
        assert(result.summary() == '1 run, 1 failed')


def main():
    TestCaseTest('test_template_method').run()
    TestCaseTest('test_result').run()
    # TestCaseTest('test_failed_result').run()


if __name__ == '__main__':
    main()
