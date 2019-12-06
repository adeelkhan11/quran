import csv

from quran.dictcounter import DictCounter
from quran.surah import Surah
from quran.wordcounter import WordCounter

csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)


class Quran:
    def __init__(self, data_file='data/quran-simple-enhanced.txt'):
        # Line[0] is the name of the data file, so the index of each line that follows is the actual line number
        self.lines = [data_file]
        self.surahs = dict()
        with open(data_file) as f:
            reader = csv.reader(f, dialect='piper')

            for quran_aya_num, line in enumerate(reader, 1):
                try:
                    if len(line) == 3:
                        surah_num, aya_num, text = line
                        self.lines.append(line)
                        if surah_num not in self.surahs:
                            self.surahs[surah_num] = Surah(surah_num)
                        self.surahs[surah_num].add_aya(text, quran_aya_num)
                except ValueError:
                    print(f'Problem processing line: {line}')
                    raise
                # if quran_aya_num >= 3:
                #     break

    def print_surah_table(self):
        print('Surah  Len  Words  First   Last')
        for surah in self.surahs.values():
            print(f'{surah.number:>5}  {surah.length():>3}  {surah.word_count():>5}  {surah.first_aya:>5}  {surah.last_aya:>5}')

    def letter_counts(self):
        letters = DictCounter()
        for surah in self.surahs.values():
            surah.count_letters(letters)

        letters.print_counts()

    def word_counts(self):
        words = WordCounter()
        for surah in self.surahs.values():
            surah.count_words(words)

        words.print_counts()
