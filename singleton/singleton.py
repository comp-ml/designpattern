class Singleton:

    _unique_instance = None

    ## 1. get_instance時に__init__が呼び出されるので
    ## その前にraiseする
    def __new__(cls):
        raise NotImplementedError('Cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()  # 変更

        return cls._unique_instance