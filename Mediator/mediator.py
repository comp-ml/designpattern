import abc

class ICollegue(metaclass = abc.ABCMeta):
    def __init__(self):
        pass

    def set_secretlover(self, collegue):
        pass

    def need_advice(self):
        pass


class IMediator(metaclass = abc.ABCMeta):
    def __init__(self):
        pass

    def add_collegue(self, collegue):
        pass

    # seacret_loverに相談
    def consultation(self, collegue, secretlover):
        pass

class Collegue(ICollegue):
    def __init__(self, name, saito):
        self.mediator = saito
        self.name = name

    def set_secretlover(self, collegue):
        self.secretlover = collegue

    def get_name(self):
        return self.name

    def get_lover_name(self):
        return self.secretlover.get_name()

    def need_advice(self):
        comment = self.mediator.consultation(self, self.secretlover)
        return comment



class Saito(IMediator):
    def __init__(self):
        self.collegue_dict = {}

    def add_collegue(self, collegue):
        self.collegue_dict[collegue.get_name()] = collegue

    def consultation(self, collegue, secretlover):
        if collegue.get_name() == secretlover.get_lover_name():
            return 'OK'
        else:
            return 'NG'





