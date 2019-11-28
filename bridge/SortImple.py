import abc
class AbsSortImple(object):
    __metaclass__ = abc.ABCMeta
    # インスタンス化を排除することはできるが継承先で強制実装はできない
    # TypeErrorが出力されるはずだがされない。。。
    def __init__(self):
        pass

    @abc.abstractmethod
    def sort(self, agg):
        pass

class BubbleSortImple(AbsSortImple):
    def __init__(self):
        super.__init__()

    def sort(self, agg):
        agg_sorted = sorted(agg)
        return agg_sorted


