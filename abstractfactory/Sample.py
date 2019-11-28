from Hotpot import HotPot
from HotSoupFactory import AbsHotSoupFactory, KimuchiHotSoupFactory, SaltHotSoupFactory
from Pot import Pot

class CreateHotSoup:
    def __init__(self, kind_hotsoup):
        factory = CreateHotSoup.create_factory(kind_hotsoup)
        hotpot = HotPot(Pot(10))
        hotpot.add_soup(factory.get_soup())
        hotpot.add_vegitables(factory.get_vegitables())

        hotpot.teach_soup()
        hotpot.teach_vegitables()

    @classmethod
    def create_factory(cls, kind_hotsoup):
        if kind_hotsoup == 'kimuchi':
            return KimuchiHotSoupFactory()
        else:
            return SaltHotSoupFactory()

if __name__ == '__main__':
    CreateHotSoup('kimuchi')
    CreateHotSoup('salt')








