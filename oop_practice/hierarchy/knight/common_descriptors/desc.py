__author__ = 'Kiryl_Zayets'


class Check(object):
    """
        Base descriptor for custom verification.
        @value - verify.
        @typ - expecting type of value.
        @func - custom function for verification.
    """
    def __init__(self, value=None, typ=None, func=None):
        self.value = value
        self.typ = typ
        self.func = func

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, self.typ):
            if self.func:
                if self.func(value):
                    self.value = value
                else:
                    raise AttributeError
            else:
                self.value = value
        else:
            raise AttributeError