from Sorter import Sorter
from SortImple import BubbleSortImple
import time

class TimerSorter(Sorter):
    def __init__(self, sort_imple):
        super.__init__(sort_imple)

    def timer_sort(self, agg):
        start = time.time()
        self.sort_imple.sort(agg)
        elapsed_time = time.time() - start
        return elapsed_time

if __name__ == 'main':
    bubble_timer = TimeSorter(BubbleSortImple)
    print(bubble_timer.timer_sort([5,6,1]))