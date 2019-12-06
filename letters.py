import csv

from quran.quran import Quran

csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)


q = Quran()

q.print_surah_table()
q.letter_counts()
