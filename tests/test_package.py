# Standard Library
import unittest
from io import StringIO

# First Party
import console as console_main


class KlassForSort:
    """Example class"""

    attr1 = 1
    Attr2 = 2
    Name2 = 'name2'

    def __init__(self):
        self.name = 'Name'

    def get_name_and_method(self):
        return self.name + ' get_name_and_method'

    @property
    def admin1(self):
        return True


class MyClass:
    """Example class"""

    klass_var1 = 1
    klass_var2 = 2
    klass_var3 = 'string'
    klass_var4 = list()
    klass_var5 = dict()
    klass_var6 = set()

    def __init__(self):
        self.name = 'Name'

    def get_name_and_method(self):
        return self.name + ' get_name_and_method'

    def _private_method(self):
        return self.name + ' _private_method'

    @property
    def admin(self):
        return True

    @property
    def badmin(self):
        return True

    @property
    def cadmin(self):
        return True

    @property
    def xxadmin(self):
        return True

    @staticmethod
    def statik():
        return 'Static'

    @classmethod
    def klass_method(cls):
        return 'kls'


class TestVBConsole(unittest.TestCase):
    """vb-console tests"""

    def setUp(self):
        self.buffer = StringIO()
        self.console = console_main.console(
            source=__name__,
            writer=self.buffer,
            enabled=True,
        )

    def tearDown(self):
        self.buffer.close()

    def test_version(self):
        self.assertNotEqual(console_main.__version__, '')

    def test_basic_output1(self):
        self.console('test 1')
        self.assertEqual("('test 1',)\n", self.buffer.getvalue())

    def test_basic_output2(self):
        self.console('test 2', dict(foo=1, bar='2'))
        self.assertEqual("('test 2', {'bar': '2', 'foo': 1})\n", self.buffer.getvalue())

    def test_class_inspection(self):
        my_test_class_instance = MyClass()
        self.console.dir(my_test_class_instance)

        self.assertTrue('class_methods' in self.buffer.getvalue())
        self.assertTrue('class_variables' in self.buffer.getvalue())
        self.assertTrue('data_attributes' in self.buffer.getvalue())
        self.assertTrue('internal_methods' in self.buffer.getvalue())
        self.assertTrue('methods' in self.buffer.getvalue())
        self.assertTrue('private_methods' in self.buffer.getvalue())
        self.assertTrue('properties' in self.buffer.getvalue())
        self.assertTrue('public_attributes' in self.buffer.getvalue())
        self.assertTrue('static_methods' in self.buffer.getvalue())

    def test_sorted_output(self):
        class_instance = KlassForSort()
        self.console.dir(class_instance)
        self.assertTrue(
            "['admin1', 'attr1', 'Attr2', 'get_name_and_method', 'name', 'Name2']"
            in self.buffer.getvalue()
        )


class TestVBConsoleWithColor(unittest.TestCase):
    """vb-console color tests"""

    def setUp(self):
        self.buffer = StringIO()
        self.console = console_main.console(
            source=__name__,
            writer=self.buffer,
            enabled=True,
            colored=True,
        )

    def tearDown(self):
        self.buffer.close()

    def test_basic_output_colored1(self):
        my_test_class_instance = MyClass()
        self.console.dir(my_test_class_instance)

        self.assertTrue('\x1b[33m' in self.buffer.getvalue())
        self.assertTrue('\x1b[38m' in self.buffer.getvalue())
        self.assertTrue('\x1b[0m' in self.buffer.getvalue())


if __name__ == '__main__':
    unittest.main()
