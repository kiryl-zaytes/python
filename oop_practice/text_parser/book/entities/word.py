import weakref

__author__ = 'kiryl_zayets'


class Word(object):
    """ Represent word entity.
    Use flyweight and weak references to store object.
    """

    vowel_pattern = ['a','e','i','o','u']
    _word_pool = weakref.WeakValueDictionary()

    def __new__(cls, chars):
        """ Flyweight starts here to cash redundant objects"""
        obj = Word._word_pool.get(chars, None)
        if not obj:
            obj = object.__new__(cls)
            Word._word_pool[chars] = obj
            obj.word = chars
        return obj

    def __init__(self, chars):
        self.word = chars
        self.vowel_count = None
        self.consonant_count = None
        self.length = None
        self()

    def __call__(self, *args, **kwargs):
        """ Calculate word length and count of vowels and consonant."""
        self.length = len(self.word)
        self.vowel_count = len([char for char in self.word if char in Word.vowel_pattern])
        self.consonant_count = self.length - self.vowel_count

    def __hash__(self):
        return hash(self.word)

    def __eq__(self, other):
        return isinstance(other, Word) and self.word == other.word

    def __str__(self):
        return 'Word: {0} Vowels:{1} Consonant:{2}'.format(self.word, self.vowel_count, self.consonant_count)
