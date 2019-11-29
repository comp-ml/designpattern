import Builder

class SaltDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.add_solute(10)
        self.builder.add_solvent(20)

    def get_status(self):
        return self.builder.get_result()