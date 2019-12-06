
from dataclasses import dataclass, field
from typing import List


@dataclass
class Surah:
    """Class for storing a surah."""
    number: int
    ayas: List[str] = field(default_factory=list)
    first_aya: int = 0
    last_aya: int = 0

    def add_aya(self, aya, aya_num):
        self.ayas.append(aya)
        if self.first_aya == 0:
            self.first_aya = aya_num
        self.last_aya = aya_num

    def length(self):
        return len(self.ayas)

    def word_count(self):
        result = 0
        for a in self.ayas:
            result += len(a.split())
        return result

    def count_letters(self, letters):
        for a in self.ayas:
            for b in a:
                letters.add(b)

    def count_words(self, words):
        for a in self.ayas:
            for b in a.split():
                words.add(b)
