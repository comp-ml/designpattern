import abc
# abstract-class
class AbsHotSoupFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_soup(self):
        pass

    @abc.abstractmethod
    def get_vegitables(self):
        pass

class KimuchiHotSoupFactory(AbsHotSoupFactory):
    def get_soup(self):
        return 'kimuchi'

    def get_vegitables(self):
        return ['a', 'b']

class SaltHotSoupFactory(AbsHotSoupFactory):
    def get_soup(self):
        return 'salt'

    def get_vegitables(self):
        return ['c', 'd']