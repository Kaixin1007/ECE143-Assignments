

def is_string_integer(ch):
    '''
    :param ch: input character.
    :return: True or False if that character represents a valid integer in base 10.
    '''
    assert isinstance(ch,str)
    assert len(ch) == 1

    return ch.isdigit()



