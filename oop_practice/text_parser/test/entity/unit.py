from book.entities.sentence import Sentence
from book.entities.word import Word
from unittest import TestCase
from book.parser.splitter import FileParser
from book.parser.splitter import get_parser
from book.command.text_command import *

class EntityTest(TestCase):
    def setUp(self):
        self._word = Word('privet')
        self._word1 = Word('privet')
        self._word2 = Word('paka')
        self.path ='/Users/kiryl_zayets/Dropbox/Python/text_parser/static/linux.txt'

    def test_word_creation_flyweight(self):
        self.assertEqual(id(self._word), id(self._word1))

    def test_word_creation_diff_obj(self):
        self.assertNotEqual(id(self._word), id(self._word2))

    def test_word_callable_calculating(self):
        props = [self._word1.length, self._word1.consonant_count, self._word1.vowel_count]
        check_props = [6, 4, 2]
        self.assertListEqual(props, check_props)

    def test_equal_hash(self):
        self.assertEqual(self._word, self._word1)
        self.assertNotEqual(self._word, self._word2)

    def test_file_parsing(self):

        text_obj = get_parser(file=self.path).parse()
        print(text_obj[3])
        words_count = text_obj[3].words_count()
        self.assertEqual(words_count, 7)


class CommandTest(TestCase):

    def setUp(self):
        self.path ='/Users/kiryl_zayets/Dropbox/Python/text_parser/static/linux.txt'

    def test_sorting(self):
        text_obj = get_parser(file=self.path).parse()
        char = 'o'
        sorted_text = sorted(text_obj[6].words, key=lambda wordobj: wordobj.word.count(char))

    def test_command_sort(self):
        text = get_parser(file=self.path).parse()
        command = Sort(text, 'a')
        sortedlsit = command.execute()
        self.assertIsNotNone(sortedlsit)

    def test_command_change(self):
        text = get_parser(file=self.path).parse()
        command  = Change(text[457], 5, 'newword')
        new_text = command.execute()
        self.assertEqual(new_text.words[5].word, 'newword')






