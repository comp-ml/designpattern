import abc
from Human import Human

class AbsCompare(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def compare(self, human1, human2):
        pass

class HeightCompare(AbsCompare):
    def compare(self, human1, human2):
        if human1.height > human2.height:
            return 1
        else:
            return -1

class WeightCompare(AbsCompare):
    def compare(self, human1, human2):
        if human1.weight > human2.weight:
            return 1
        else:
            return -1
    
if __name__ == 'main':
    height = HeightCompare()
    human1 = Human('tanaka', 4,6,3)
    human2 = Human('takesi', 6,3,4)
    x = height.compare(human1, human2)