import Water
import abc

class AbsWaterBuilder(metaclass = abc.ABCMeta):
    def __init__(self):
        self.saltwater = Water.SaltWater(0,0)
    
    @abc.abstractmethod
    def add_solute(self, solute_amount):
        pass

    @abc.abstractmethod
    def add_solvent(self, solvent_amount):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass

class SaltWaterBuilder(AbsWaterBuilder):
    def __init__(self):
        super(SaltWaterBuilder ,self).__init__()
    
    def add_solute(self, solute_amount):
        self.saltwater.salt += solute_amount
    
    def add_solvent(self, solvent_amount):
        self.saltwater.water += solvent_amount
    
    def get_result(self):
        return self.saltwater
