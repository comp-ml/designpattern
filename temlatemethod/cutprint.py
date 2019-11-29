import abc
import cuttable
class WoodCutPrint(metaclass = abc.ABCMeta):
    def __init__(self):
        pass
    
    @abc.abstractmethod
    def draw(self, hanzai):
        pass

    @abc.abstractmethod
    def cut(self, hanzai):
        pass

    @abc.abstractmethod
    def print_hanga(self, hanzai):
        pass

    def cut_print(self):
        wood = cuttable.Wood()
        self.draw(wood)
        self.cut(wood)
        self.print_hanga(wood)
        

class MyWoodCutPrint(WoodCutPrint):
    def __init__(self):
        super().__init__()

    def draw(self, hanzai):
        print('木を書く')

    def cut(self, hanzai):
        print('木を切る')

    def print_hanga(self, hanzai):
        print('木にプリントする')