class LendBookCheck:
    def __init__(self):
        self.current_list = ['c']

    def lend_check(self, book):
        if not (book in self.current_list):
            print('status: lend')
        else:
            print('status: OK')



class BookSearchCheck:
    def __init__(self):
        self.book_list = ['a','b','c']

    def book_search(self, book):
        if not(book in self.book_list):
            print('status: nothing')
        else:
            print('status: OK')


class Libraritan:
    def __init__(self):
        pass

    def book_search(self, book):
        lend_check = LendBookCheck()
        book_check = BookSearchCheck()

        book_check.book_search(book)
        lend_check.lend_check(book)
        

