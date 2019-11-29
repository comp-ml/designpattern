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

    def create_cuttable(self):
        return cuttable.Wood()

    def cut_print(self):
        cuttable = self.create_cuttable()
        self.draw(cuttable)
        self.cut(cuttable)
        self.print_hanga(cuttable)
        

class MyWoodCutPrint(WoodCutPrint):
    def __init__(self):
        super().__init__()

    def draw(self, hanzai):
        print('木を書く')

    def cut(self, hanzai):
        print('木を切る')

    def print_hanga(self, hanzai):
        print('木にプリントする')


class MyPotateCutPrint(WoodCutPrint):
    def __init__(self):
        super().__init__()

    # override create_cuttable
    def create_cuttable(self):
        return cuttable.Potate()

    def draw(self, hanzai):
        print('ポテトを書く')

    def cut(self, hanzai):
        print('ポテトを切る')

    def print_hanga(self, hanzai):
        print('ポテトにプリントする')