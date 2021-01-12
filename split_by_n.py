import os
def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    assert isinstance(fname, str)
    assert isinstance(n, int)
    assert n >= 1
    ave_size = os.path.getsize(fname)/n
    lines = []
    size = 0
    cnt = 0
    f = open(fname, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        size += len(line)
        lines.append(line)
        if(size > ave_size):
            size = 0
            file_name = fname + '_'+str(cnt).zfill(3)+'.txt'

            fn = open(file_name,'wt')
            for i in range(0,len(lines)):
                # print(type(lines[i]))
                fn.write(lines[i])

            fn.close()
            lines = []
            cnt = cnt +1
    file_name = fname + '_' + str(cnt).zfill(3) + '.txt'

    fn = open(file_name, 'wt')
    for i in range(0, len(lines)):
        # print(type(lines[i]))
        fn.write(lines[i])

    fn.close()
# a = "pg5200.txt"
# print(type(a))
# split_by_n(a,8)