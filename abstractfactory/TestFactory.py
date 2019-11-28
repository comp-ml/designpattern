import unittest
from Hotpot import HotPot
from HotSoupFactory import AbsHotSoupFactory, KimuchiHotSoupFactory, SaltHotSoupFactory

class TestFactory(unittest.TestCase):
    def test_factory(self):
        factory = KimuchiHotSoupFactory()
        self.assertEqual(factory.get_soup(), 'kimuchi')
        self.assertEqual(factory.get_vegitables(), ['a','b'])

        factory = SaltHotSoupFactory()
        self.assertEqual(factory.get_soup(), 'salt')
        self.assertEqual(factory.get_vegitables(), ['c','d'])

if __name__ == "__main__":
    unittest.main()



