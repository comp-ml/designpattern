import abc
class IChairPerson(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def organize_class(self):
        pass

class Taro:
    def __init__(self):
        pass
    def enjoy_classmate(self):
        print('lets enjoy')

class NewTaro(IChairPerson, Taro):
    def __init__(self):
        super().__init__()

    def organize_class(self):
        self.enjoy_classmate()