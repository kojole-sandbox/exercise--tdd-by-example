class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def run(self):
        self.setup()
        method = getattr(self, self.name)
        method()
        self.teardown()

    def teardown(self):
        pass


class WasRun(TestCase):
    def setup(self):
        self.log = "setup "

    def teardown(self):
        self.log += "teardown "

    def test_method(self):
        self.log += "test_method "


class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        assert(test.log == "setup test_method teardown ")


def main():
    TestCaseTest('test_template_method').run()


if __name__ == '__main__':
    main()
