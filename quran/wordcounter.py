import operator


class WordCount:
    def __init__(self, normalised_word):
        self.word = normalised_word
        self.count = 0
        self.counts = dict()

    def add(self, value):
        self.count += 1
        if value not in self.counts:
            self.counts[value] = 1
        else:
            self.counts[value] += 1

    def __repr__(self):
        sorted_x = sorted(self.counts.items(), key=operator.itemgetter(1), reverse=True)
        return ', '.join([f'{x[0]} ({x[1]})' for x in sorted_x])


class WordCounter:
    def __init__(self):
        self.counts = dict()

    def add(self, value):
        normalised_word = self.normalise(value)
        if normalised_word not in self.counts:
            self.counts[normalised_word] = WordCount(normalised_word)
        self.counts[normalised_word].add(value)

    def print_counts(self):
        sorted_x = [(key, self.counts[key]) for key in sorted(self.counts, key=lambda word: self.counts[word].count,
                                                              reverse=True)]
        for i, x in enumerate(sorted_x, 1):
            print(f'{i:>4}  {x[0]:>10}  {x[0][-1]:>2}  {(x[0][-1]).encode("unicode_escape")}  {(x[0][:7]).encode("unicode_escape")}  {x[1].count:>7}')
            print(x[1])
            if i >= 300:
                break

    @staticmethod
    def normalise(word):
        result = word
        if result[-1] in ('\u064b', '\u064c', '\u064d', '\u064e', '\u064f', '\u0650', '\u0651', '\u0652'):
            result = result[:-1]
        if result == '\u0627\u0644\u0644\u0651\u064e\u0647':  # Allah
            pass
        elif result[:3] == '\u0627\u0644\u0652':  # al
            result = result[3:]
        elif result[:2] in ('\u0648\u064e', '\u0627\u0644'):  # wa, al
            result = result[2:]
        return result
