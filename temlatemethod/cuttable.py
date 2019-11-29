import abc
class AbsCutTable(metaclass = abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Wood(AbsCutTable):
    def __init__(self):
        super().__init__('wood')


class Potate(AbsCutTable):
    def __init__(self):
        super().__init__('potate')