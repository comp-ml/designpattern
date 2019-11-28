import unittest
from SortImple import BubbleSortImple, AbsSortImple

class TestSorter(unittest.TestCase):
    def test_sorter(self):
        bubblesorter = BubbleSortImple()
        self.assertEqual(bubblesorter.sort([5,3,4]), [3,4,5])


if __name__ == 'main':
    unittest.main()

