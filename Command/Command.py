import abc

class Beaker:
    def __init__(self, salt, water):
        self.salt = salt
        self.water = water
        self.mix()

    def mix(self):
        if ( self.salt / (self.water + self.salt) )*100 < 26.5:
            self.melted = True
        else:
            self.melted = False

    def add_salt(self, salt):
        self.salt+=salt

    def add_water(self, water):
        self.water+=water

    def get_salt(self):
        return self.salt

    def get_water(self):
        return self.water

    def is_melted(self):
        return self.melted

    def note(self):
        print('water:', self.water)
        print('salt', self.salt)
        print('dense', self.salt / (self.water + self.salt) * 100 )

class Command(metaclass = abc.ABCMeta):
    def __init__(self,beaker):
        self.beaker = beaker

    @abc.abstractmethod
    def experiment(self):
        pass

class AddSaltCommand(Command):
    def __init__(self, beaker):
        super().__init__(beaker)

    def experiment(self):
        while(self.beaker.is_melted() == True):
            self.beaker.add_salt(1)
            self.beaker.mix()

        self.beaker.note()
        
class AddWaterCommand(Command):
    def __init__(self, beaker):
        super().__init__(beaker)
    
    def experiment(self):
        while(self.beaker.is_melted() == False):
            self.beaker.add_water(100)
            self.beaker.mix()

        self.beaker.note()


    





    