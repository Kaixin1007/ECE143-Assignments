def compute_average_word_length(instring, unique=False):
    '''

    :param instring: input string
    :param unique: True: True, then exclude duplicated words
    :return: average length of the words
    '''
    assert isinstance(instring, str)
    assert isinstance(unique,bool)
    l = instring.split()
    res = []
    for s in l:
        if unique == False:
            res.append(s)
        elif unique == True:
            if s not in res:
                res.append(s)
    if len(res) == 0:
        return 0
    sum = 0
    for s in res:
        sum += len(s)
    ave = sum / len(res)

    return ave
