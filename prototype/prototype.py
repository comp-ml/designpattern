import abc
class IClonable(metaclass  = abc.ABCMeta):
    @abc.abstractmethod
    def createClone(self):
        pass

class Paper(IClonable):
    def __init__(self, name):
        self.name = name
        self.draw = 'Nothing'
        self.cut = 'Nothing'

    def createClone(self):
        paper = Paper('hogehoge')
        paper.name = self.name
        paper.draw = self.draw
        paper.cut = self.cut

        return paper

class Teacher:
    def __init__(self):
        pass

    def createManyCrystal(self):
        paper = Paper('hogehoge')
        self.draw_crystal(paper)
        self.cut_accordance_with_line(paper)
        return [paper.createClone() for i in range(100)]
    
    def draw_crystal(self, prototype):
        prototype.draw = 'crystal'

    def cut_accordance_with_line(self, prototype):
        prototype.cut = 'cut'
