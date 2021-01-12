def encrypt_message(message,fname):
     '''
  3     Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
  4     name of a text file source for the codebook, generate a sequence of 2-tuples that
  5     represents the `(line number, word number)` of each word in the message. The output is a list
  6     of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple.
  7
  8     :param message: message to encrypt
  9     :type message: str
 10     :param fname: filename for source text
 11     :type fname: str
 12     :returns: list of 2-tuples
 13     '''
     assert isinstance(message, str)
     assert message.islower()
     assert isinstance(fname, str)

     assert message.replace(' ','').isalpha()
     message = message.split()
     loc = dict()
     f = open(fname, 'r')
     cnt = 0
     while True:
         line = f.readline()
         cnt += 1
         if not line:
             break
         line = line.lower()
         line = line.split()
         if line:
            for i in range(len(line)):
                if line[i] not in loc:
                    loc[line[i]] = []
                loc[line[i]].append((cnt,i+1))

     loc_message = dict()
     for j in message:
         loc_message[j] = loc_message.get(j,0) + 1
         assert loc_message[j] <= len(loc[j])
     encrypt_mes = []
     for j in message:
         i = 0
         while True:
             mess = loc[j][i]
             if mess not in encrypt_mes:
                 encrypt_mes.append(mess)
                 break
             else:
                 i+=1
     return encrypt_mes



def decrypt_message(inlist,fname):
    '''
 35     Given `inlist`, which is a list of 2-tuples`fname` which is the
 36     name of a text file source for the codebook, return the encrypted message.
 37
 38     :param message: inlist to decrypt
 39     :type message: list
 40     :param fname: filename for source text
 41     :type fname: str
 42     :returns: string decrypted message
    '''

    assert isinstance(inlist, list)
    assert isinstance(fname, str)
    for l in inlist:
        assert isinstance(l, tuple)
    assert (len(i) == 2 for i in inlist)
    loc = dict()
    f = open(fname, 'r')
    cnt = 0
    while True:
        line = f.readline()
        cnt += 1
        if not line:
            break
        line = line.lower()
        line = line.split()
        if line:
            for i in range(len(line)):
                if line[i] not in loc:
                    loc[line[i]] = []
                loc[line[i]].append((cnt, i + 1))
    final_str = ''
    for i in inlist:
        for words in loc:
            if i in loc[words]:
                final_str += words
                final_str += ' '
    return final_str[:-1]

# a = "encrypt.txt"
# string_test = 'let us not say we met late at the night about the secret'
# temp = encrypt_message(string_test,a)
# print(temp)
# res = decrypt_message(temp,a)
# print(res == string_test)
# print(res)