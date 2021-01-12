

class Rational:
    '''
    Rational class
    '''
    def __init__(self, a, b = 1):
        '''
        :param a: numerator
        :param b: denominator
        '''
        assert b !=0
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b
        div = self.gcd(self._a,self._b)
        self._a = self._a // div
        self._b = self._b // div


    def gcd(self,a, b):  # note no self parameter for static method
        '''Return the greatest common divisor of the pair'''
        while b != 0:
            a, b = b, a % b
        return a


    def __repr__(self):
        '''
        :return: str. represent the Rational class
        '''
        if(self._b == 1):
            return str(self._a)
        # return "\'"+ str(self._a)+"/"+str(self._b)+"\'"
        return str(self._a) + '/' + str(self._b)
    def __str__(self):
        '''
        :return:
        '''
        if (self._b == 1):
            return str(self._a)
        return str(self._a) + '/' + str(self._b)

    def __add__(self, num):
        '''
        :param num:
        :return:
        '''
        #  self.add(num) <- self + num   num + self  num.add(self)
        if isinstance(num,float):
            return float(self) + num
        if isinstance(num, int):
            num = Rational(num)
        return Rational(self._a * num._b + self._b * num._a,(self._b*num._b))

    def __sub__(self,num):
        '''
        :param num:
        :return:
        '''
        return self + -num
    def __mul__(self,num):
        '''
        :param num:
        :return:
        '''
        if isinstance(num, float):
            return float(self) * num
        if isinstance(num, int):
            num = Rational(num)
        return Rational((self._a * num._a ) , (self._b * num._b))

    # def __div__(self,num):
    #     '''
    #     :param num:
    #     :return:
    #     '''
    #     if not isinstance(num, Rational):
    #         num = Rational(num)
    #     return Rational((self._a * num._b) , (self._b * num._a))

    def __truediv__(self, num):
        '''
        :param num:
        :return:
        '''
        if isinstance(num,float):
            return float(self) / num
        if isinstance(num, int):
            num = Rational(num)
        return Rational((self._a * num._b) , (self._b * num._a))

    def __radd__(self, num):
        '''
        :param num:
        :return:
        '''
        #
        return self + num

    def __rsub__(self, num):
        '''
        :param frac2:
        :return:
        '''
        return -self + num
    def __rmul__(self, num):
        '''
        :param num:
        :return:
        '''
        return self * num

    def __rtruediv__(self, num):
        '''
        :param num:
        :return:
        '''
        return Rational(self._b, self._a) * num

    def __neg__(self):
        '''
        :return:
        '''
        return Rational(-self._a, self._b)
    def __float__(self):
        '''
        :return:
        '''
        return self._a / self._b

    def __int__(self):
        '''
        :return:
        '''
        return int(self._a / self._b)

    def __lt__(self, num):
        '''
        :param num:
        :return:
        '''
        if not isinstance(num, Rational):
            num = Rational(num)
        return self._a * num._b < self._b * num._a

    def __eq__(self, num):
        '''
        :param num:
        :return:
        '''
        if isinstance(num, int):
            num = Rational(num)
        if isinstance(num, float):
            return float(self) == num
        return self._a == num._a and self._b == num._b
# r = Rational(3,4)
# print(repr(r))
# print(-1/r)
# print(float(-1/r))
# print(int(r))
# print(int(Rational(10,3)))
# print(Rational(10,3) * Rational(101,8) - Rational(11,8))
# print([Rational(10,3),Rational(9,8), Rational(10,1), Rational(1,100)])
# print(sorted([Rational(10,3),Rational(9,8), Rational(10,1), Rational(1,100)]))
# print(Rational(100,10))
# print(-Rational(12345,128191) + Rational(101,103) * 30 /44)
# print(r == Rational(3,4))
