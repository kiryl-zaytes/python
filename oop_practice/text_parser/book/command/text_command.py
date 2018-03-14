from book.entities.word import Word

__author__ = 'kiryl_zayets'


class Sort(object):
    def __init__(self, sentences, char):
        self.text = sentences
        self.char = char
        self.sortedlist = []

    def execute(self):
        return self()

    def __call__(self, *args, **kwargs):
        for sentence in self.text:
            self.sortedlist.append(sorted(sentence.words, key=lambda wordobj: wordobj.word.count(self.char)))
        return self.sortedlist

    def undo(self):
        self.sortedlist = None
        return self.text


class Change(object):
    def __init__(self, sentence, word_len, new_word):
        self.word_len = word_len
        self.new_word = new_word
        self.sentence = sentence

    def execute(self):
        return self()

    def __call__(self, *args, **kwargs):
        for i, word in enumerate(self.sentence.words):
            if word.length == self.word_len:
                self.sentence.words[i] = Word(self.new_word)
        return self.sentence
