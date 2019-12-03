
import abc
class IIceCream(metaclass = abc.ABCMeta):
    def __init__(self):
        pass

    def get_name(self):
        pass

    def how_sweet(self):
        pass


class VanillaIceCream(IIceCream):
    def __init__(self):
        pass

    def get_name(self):
        return 'vanilla_icecream'

    def how_sweet(self):
        return 'vanilla_sweet'

class CashuNutsVanillaIceCream(VanillaIceCream):
    def __init__(self):
        pass

    def get_name(self):
        return 'cashunuts'