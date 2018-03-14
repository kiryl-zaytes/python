

def title_is_text(value):
    if value.startswith(u'fuck'):
        msg = u'It is now allowed to use this word'
        raise ValueError(msg)
