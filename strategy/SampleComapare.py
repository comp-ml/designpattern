import compare
class SampleCompare():
    def __init__(self, compare_cls):
        self.compare_cls = compare_cls

    def compare(h1, h2):
        return self.compare_cls.compare(h1 ,h2)
        
