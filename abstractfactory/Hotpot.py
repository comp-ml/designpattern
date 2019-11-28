from Pot import Pot

class HotPot:
    def __init__(self, pot):
        self.pot = pot

    def add_soup(self, addsoup):
        self.soup = addsoup

    def add_vegitables(self, addvegi):
        self.vegitables = addvegi

    def teach_vegitables(self):
        print(self.vegitables)

    def teach_soup(self):
        print(self.soup)

