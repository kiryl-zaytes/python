import mmap
import abc
import re

__author__ = 'kiryl_zayets'
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
from book.entities.sentence import Sentence

class Parser(metaclass=abc.ABCMeta):

    @abstractmethod
    def parse(self):
        pass

    def get_path(self):
        pass

    def set_path(self, value):
        pass

    path_file = abstractproperty(fget=get_path, fset=set_path)


class FileParser(Parser):

    pattern = re.compile(r'[.!?]')

    def __init__(self, path, all_at_once=True):
        self._path_file = path
        self._all_at_once = all_at_once

    def get_path(self):
        return self._path_file

    def set_path(self, value):
        self._path_file = value

    def parse(self):
        if self._all_at_once:
            res = self.whole_parse()
        else:
            res = self.gen_parse()
        return res

    def whole_parse(self):
        with open(self.path_file, 'r', encoding='utf-8') as file:
            text = file.read()
        list_sentences = re.split(pattern=FileParser.pattern, string=text)
        text = [Sentence(sentence) for sentence in list_sentences if len(sentence.strip('')) > 3]
        return text

    def gen_parse(self):
        pass
        # return [match.group(0) for match in re.finditer(pattern=FileParser.pattern, string=text)]
                # mm = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
                # for match in re.finditer(pattern=FileParser.pattern, string=mm):
                #     yield mm[match.start():match.end()]

    path_file = property(fget=get_path, fset=set_path)


class XMLParser(Parser):
    def parse(self):
        pass

    def get_path(self):
        pass

    def set_path(self, value):
        pass

def get_parser(parser='File', file=None):
    parser_dict = dict(File=FileParser, XML=XMLParser)
    try:
        return parser_dict[parser](file)
    except KeyError:
        raise NotImplemented
    except FileNotFoundError:
        print('Does not exist')