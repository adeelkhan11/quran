import operator


class DictCounter:
    def __init__(self):
        self.counts = dict()

    def add(self, value):
        if value not in self.counts:
            self.counts[value] = 1
        else:
            self.counts[value] += 1

    def print_counts(self):
        sorted_x = sorted(self.counts.items(), key=operator.itemgetter(1), reverse=True)
        for i, x in enumerate(sorted_x, 1):
            print(f'{i:>3}  {x[0]}  {x[0][-1]}  {(x[0][-1]).encode("unicode_escape")}  {x[1]:>7}')
            if i >= 200:
                break
