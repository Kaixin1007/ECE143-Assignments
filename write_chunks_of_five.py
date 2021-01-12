
def write_chunks_of_five(words,fname):
    '''
    :param words:words is a list of words from the above corpus
    :param fname: the output filename string
    :return: NULL
    '''
    assert isinstance(words,list)
    assert isinstance(fname, str)
    for word in words:
        assert isinstance(word, str)
    f = open(fname, 'w')
    cnt = 0
    for word in words:
        cnt += 1
        if cnt != 5:
            f.write('{} '.format(word))
        else:
            cnt = 0
            f.write('{}\n'.format(word))

    f.close()
