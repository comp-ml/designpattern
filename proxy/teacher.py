import abc
class Teacher(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def question1(self):
        pass
    def question2(self):
        pass
    def question3(self):
        pass

class TanakaTeacher(Teacher):
    def __init__(self):
        pass

    def question1(self):
        print('Tanaka1')

    def question2(self):
        print('Tanaka2')

    def question3(self):
        print('Tanaka3')

class FujiwaraTeacher(Teacher):
    def __init__(self):
        self.tanaka = TanakaTeacher()
    
    def question1(self):
        print('Fujiwara1')

    def question2(self):
        print('Fujiwara2')

    def question3(self):
        self.tanaka.question3()