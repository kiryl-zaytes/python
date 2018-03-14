__author__ = 'kiryl_zayets'
from book.entities.word import Word

class Sentence(object):

    def __init__(self, line):
        self.line = line
        self._words = []
        self()

    def __call__(self, *args, **kwargs):
        self._words = [Word(word) for word in self.line.split(' ')]

    @property
    def words(self):
        if self._words:
            return self._words

    @words.setter
    def words(self, value):
        # self._words = []
        self.line = value

    def words_count(self):
        return len(self.words)

    def __str__(self):
        return 'Sentence: Words:{0} Length:{1}'.format(self.line, self.words_count())