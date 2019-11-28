from SortImple import BubbleSortImple, AbsSortImple

class Sorter:
    def __init__(self, sort_imple):
        self.sort_imple = sort_imple

    def sort(self, agg):
        sorted_agg = self.sort_imple.sort(agg)
        return sorted_agg

if __name__ == "main":
    sortcls = Sorter(BubbleSortImple())
    print(sortcls.sort([2,5,3]))