from urllib.request import urlopen
def get_average_word_length(words):
    '''
    get the average length of words
    '''
    assert isinstance(words, list)
    for s in words:
        assert isinstance(s, str)
    ave = 0
    for s in words:
        ave += len(s)
    ave /= len(words)
    return ave

def get_longest_word(words):
    '''

    get the longest word
    '''
    assert isinstance(words, list)
    for s in words:
        assert isinstance(s, str)
    max_length = ''
    for s in words:
        if(len(s) > len(max_length)):
            max_length = s
    return max_length

def get_longest_words_startswith(words,start):
    '''
    get the longest word that starts with a single letter
    '''
    assert isinstance(start, str)
    assert len(start) == 1
    assert start != ' '
    assert isinstance(words, list)
    for s in words:
        assert isinstance(s, str)
    max_length = ''
    for s in words:
        if(s[0] == start):
            if(len(s) > len(max_length)):
                max_length = s
    return max_length

def get_most_common_start(words):
    '''
    the most common starting letter
    '''
    assert isinstance(words, list)
    for s in words:
        assert isinstance(s, str)
    dic = {}
    for s in words:
        dic[s[0]] = dic.get(s[0],0)+1

    return max(dic, key=dic.get)

def get_most_common_end(words):
    '''
    the most common ending letter
    '''
    assert isinstance(words, list)
    for s in words:
        assert isinstance(s, str)
    dic = {}
    for s in words:
        dic[s[-1]] = dic.get(s[-1],0)+1

    return max(dic, key=dic.get)
# u='https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
# response = urlopen(u)
# words = [i.strip().decode('utf8') for i in response.readlines()]
# print(get_longest_words_startswith(words,'a'))
# print(get_longest_word(words))