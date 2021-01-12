def write_columns(data,fname):
    '''
    :param data: input data
    :param fname: path
    :return: null
    '''
    assert isinstance(data,list)
    assert isinstance(fname, str)
    for dat in data:
        assert(dat,(int,float))

    f = open(fname,'w')
    for row in data:
        f.write('{:.2f},{:.2f},{:.2f}\n'.format(row,row**2,(row+row**2)/3))
    f.close()
