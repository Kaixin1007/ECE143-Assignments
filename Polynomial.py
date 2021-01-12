class Polynomial:
    '''
    Polynomial class
    '''

    def __init__(self,dic):
        '''init function'''
        assert isinstance(dic,dict)
        for i in dic:
            assert isinstance(i,int)
            assert isinstance(dic[i],int)
        temp = {}
        for key in sorted(dic):
            if dic[key] != 0:
                temp[key] = int(dic[key])
        self.poly = temp
    def __repr__(self):
        '''repr function'''
        s = ""
        for key in self.poly:
            if(self.poly[key] != 0):
                if(key == 0):
                    s += str(self.poly[key]) + " + "
                elif(key == 1):
                    if(self.poly[key] == 1):
                        s += "x + "
                    else:
                        s += str(self.poly[key]) + " x + "
                else:
                    if (self.poly[key] == 1):
                        s += "x^(" + str(key) + ") + "
                    else:
                        s += str(self.poly[key]) + " x^("+str(key)+") + "
        return s[:-3]

    def __add__(self, num):
        '''
        :param num:
        :return:
        '''

        if isinstance(num, int):
            tmp_dict = self.poly
            tmp_dict[0] += num
        else:
            tmp_dict = {}
            for i in self.poly:
                tmp_dict[i] = 0
            for i in num.poly:
                tmp_dict[i] = 0

            for i in self.poly:
                tmp_dict[i] = self.poly[i]
            for i in num.poly:
                tmp_dict[i] += num.poly[i]

        return Polynomial(tmp_dict)

    def __radd__(self, num):
        '''
        :param num:
        :return:
        '''
        return self + num

    def __sub__(self, num):
        '''
        :param num:
        :return:
        '''
        if isinstance(num, int):
            tmp_dict = self.poly
            tmp_dict[0] -= num
        else:
            tmp_dict = {}
            for i in self.poly:
                tmp_dict[i] = 0
            for i in num.poly:
                tmp_dict[i] = 0

            for i in self.poly:
                tmp_dict[i] = self.poly[i]
            for i in num.poly:
                tmp_dict[i] -= num.poly[i]

        return Polynomial(tmp_dict)

    def __rsub__(self, num):
        '''
        :param num:
        :return:
        '''
        return -self + num

    def __mul__(self, num):
        '''
        :param num:
        :return:
        '''
        tmp_dict = self.copy_dict(self.poly)
        if(isinstance(num, int)):
            tmp_dict = {}
            for i in self.poly:
                tmp_dict[i] = self.poly[i] * num
        else:
            tmp_dict = dict()
            for i in num.poly:
                for j in self.poly:
                    tmp_dict[i + j] = num.poly.get(i,0) * self.poly.get(j,0)+tmp_dict.get(i+j,0)

        return Polynomial(tmp_dict)


    def __rmul__(self, num):
        '''
        :param num:
        :return:
        '''
        return self * num

    def __truediv__(self, num):
        '''
        :param num:
        :return:
        '''
        if isinstance(num, Polynomial):
            p = {}
            a = Polynomial(self.poly)
            b = Polynomial(num.poly)
            while a != 0:
                if len(a.poly) < len(b.poly):
                    raise NotImplementedError
                if a.poly[max(a.poly)] % b.poly[max(b.poly)] != 0:
                    raise NotImplementedError
                p[max(a.poly) - max(b.poly)] = int(a.poly[max(a.poly)] / b.poly[max(b.poly)])
                temp = b * Polynomial(p)
                a = self - temp

        elif isinstance(num, int):
            p = {}
            for i in self.poly:
                if self.poly[i] % num != 0:
                    raise NotImplementedError
                p[i] = self.poly[i] / num

        return Polynomial(p)
    def get_key_max(self,dic):
        l = [key for key, value in dic.items()]
        return max(l)


    def __rtruediv__(self, num):
        '''
        :param num:
        :return:
        '''
        return 1/(self/num)
    def __neg__(self):
        '''
        :return:
        '''
        return -1 * self
    def subs(self,num):
        '''
        :param num:
        :return:
        '''
        assert isinstance(num, int)
        res = 0
        for key in self.poly:
            res += self.poly[key] * pow(num,key)
        return res

    def __eq__(self,num):
        '''
        :param num:
        :return:
        '''
        if(isinstance(num, int)):
            if(len(self.poly) == 0):
                return num == 0
            elif 0 in self.poly:
                for key in self.poly:
                    if(key != 0 and self.poly[key] != 0):
                        return False
                return self.poly[0] == num
            else:
                return False
        else:
            return self.poly == num.poly

    def copy_dict(self,d):
        'helper function'
        res = {}
        if not d:
            return {}
        for key in sorted(d):
            res[key] = d[key]
        return res

# if __name__ == '__main__':
#     p=Polynomial({0:8,1:2,3:4})
#     qq = Polynomial({0:8,1:2,3:4,4:5})
#     q=Polynomial({0:8,1:2,2:8,4:4})
#     print(repr(p))
#     print(type(p))
#     print(p*3 == 3*p)
#     print(p+q)
#     print(p*4 + 5 - 3*p - 1)
#     print(type(p-p))
#     print(p*q)
#     print(p.subs(10))
#     print((p-p) == 0)
#     print(p == q)
#     p = Polynomial({0: 8, 1: 0, 3: 4})
#     print(repr(p))
#     p = Polynomial({2: 1, 0: -1})
#     q = Polynomial({1: 1, 0: -1})
#     print(p/q)
#     p3 = Polynomial({3: 6, 2: 29, 1: 46, 0: 24})
#     q3 = Polynomial({1: 2, 0: 3})
#     print(p3/q3)
#     print(p  / Polynomial({1:1,0:-3}))
