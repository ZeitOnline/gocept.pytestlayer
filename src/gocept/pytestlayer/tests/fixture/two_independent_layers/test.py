import logging
import unittest

log = logging.getLogger('zopelayer')
log.addHandler(logging.StreamHandler())


class FooLayer(object):

    @classmethod
    def setUp(cls):
        log.info('\nsetUp foo')
        cls.layer_foo = 'layer foo'

    @classmethod
    def tearDown(cls):
        log.info('\ntearDown foo')
        del cls.layer_foo

    @classmethod
    def testSetUp(cls):
        log.info('\ntestSetUp foo')
        cls.test_foo = 'test foo'

    @classmethod
    def testTearDown(cls):
        log.info('\ntestTearDown foo')
        del cls.test_foo


class BarLayer(object):

    @classmethod
    def setUp(cls):
        log.info('\nsetUp bar')
        cls.layer_bar = 'layer bar'

    @classmethod
    def tearDown(cls):
        log.info('\ntearDown bar')
        del cls.layer_bar

    @classmethod
    def testSetUp(cls):
        log.info('\ntestSetUp bar')
        cls.test_bar = 'test bar'

    @classmethod
    def testTearDown(cls):
        log.info('\ntestTearDown bar')
        del cls.test_bar


class FooTest(unittest.TestCase):

    layer = FooLayer

    def test_dummy(self):
        self.assertEqual('layer foo', self.layer.layer_foo)
        self.assertEqual('test foo', self.layer.test_foo)
        self.assertFalse(hasattr(self.layer, 'layer_bar'))
        self.assertFalse(hasattr(self.layer, 'test_bar'))


class BarTest(unittest.TestCase):

    layer = BarLayer

    def test_dummy(self):
        self.assertFalse(hasattr(self.layer, 'layer_foo'))
        self.assertFalse(hasattr(self.layer, 'test_foo'))
        self.assertEqual('layer bar', self.layer.layer_bar)
        self.assertEqual('test bar', self.layer.test_bar)