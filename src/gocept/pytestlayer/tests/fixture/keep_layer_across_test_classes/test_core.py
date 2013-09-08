from gocept.pytestlayer.testing import log_to_terminal
import unittest


class FooLayer(object):

    @classmethod
    def setUp(cls):
        cls.layer_foo = 'layer foo'

    @classmethod
    def tearDown(cls):
        del cls.layer_foo

    @classmethod
    def testSetUp(cls):
        log_to_terminal(cls.pytest_request, '\ntestSetUp foo')
        cls.test_foo = 'test foo'

    @classmethod
    def testTearDown(cls):
        log_to_terminal(cls.pytest_request, '\ntestTearDown foo')
        del cls.test_foo


class BarLayer(object):

    @classmethod
    def setUp(cls):
        cls.layer_bar = 'layer bar'

    @classmethod
    def tearDown(cls):
        del cls.layer_bar

    @classmethod
    def testSetUp(cls):
        log_to_terminal(cls.pytest_request, '\ntestSetUp bar')
        cls.test_bar = 'test bar'

    @classmethod
    def testTearDown(cls):
        log_to_terminal(cls.pytest_request, '\ntestTearDown bar')
        del cls.test_bar


class FooBarLayer(FooLayer, BarLayer):

    @classmethod
    def setUp(cls):
        cls.layer_foobar = 'layer foobar'

    @classmethod
    def tearDown(cls):
        del cls.layer_foobar

    @classmethod
    def testSetUp(cls):
        log_to_terminal(cls.pytest_request, '\ntestSetUp foobar')
        cls.test_foobar = 'test foobar'

    @classmethod
    def testTearDown(cls):
        log_to_terminal(cls.pytest_request, '\ntestTearDown foobar')
        del cls.test_foobar


class FooTest(unittest.TestCase):

    layer = FooLayer

    def test_dummy(self):
        self.assertEqual('layer foo', self.layer.layer_foo)
        self.assertEqual('test foo', self.layer.test_foo)
        self.assertFalse(hasattr(self.layer, 'layer_bar'))
        self.assertFalse(hasattr(self.layer, 'test_bar'))


class FooBarTest(unittest.TestCase):

    layer = FooBarLayer

    def test_dummy(self):
        self.assertEqual('layer foo', self.layer.layer_foo)
        self.assertEqual('test foo', self.layer.test_foo)
        self.assertEqual('layer bar', self.layer.layer_bar)
        self.assertEqual('test bar', self.layer.test_bar)
        self.assertEqual('layer foobar', self.layer.layer_foobar)
        self.assertEqual('test foobar', self.layer.test_foobar)


class BarTest(unittest.TestCase):

    layer = BarLayer

    def test_dummy(self):
        self.assertFalse(hasattr(self.layer, 'layer_foo'))
        self.assertFalse(hasattr(self.layer, 'test_foo'))
        self.assertEqual('layer bar', self.layer.layer_bar)
        self.assertEqual('test bar', self.layer.test_bar)