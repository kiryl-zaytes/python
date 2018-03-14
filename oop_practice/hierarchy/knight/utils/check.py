__author__ = 'kiryl_zayets'

class CheckValueUtils:

    @staticmethod
    def is_pos(var):
        if var > 0:
            return var

    @staticmethod
    def is_less(var, value):
        if var < value:
            return var