class Interval(object):
    def __init__(self, a, b):
        """
        :a: integer
        :b: integer
        """
        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b

    def __repr__(self):
        '''
        :return: the output of the class
        '''
        return 'Interval('+ str(self._a) +','+ str(self._b) +')'

    def __eq__(self, other):
        '''
        :param other: other Interval
        :return: true or false
        '''
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)
        return self._a == other._a and self._b == other._b

    def __lt__(self, other):
        '''
        :param other: other Interval
        :return: true or false
        '''
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)
        return self._a < other._a and self._b < other._b

    def __gt__(self, other):
        '''
        :param other: other Interval
        :return: true or false
        '''
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)
        return self._a > other._a and self._b > other._b

    def __ge__(self, other):
        '''
        :param other: other Interval
        :return: true or false
        '''
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)
        return self._a >= other._a and self._b >= other._b

    def __le__(self, other):
        '''
        :param other: other Interval
        :return: true or false
        '''
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)
        return self._a <= other._a and self._b <= other._b

    def __add__(self, other):
        '''
        :param other: other Interval
        :return: self + other
        '''
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)
        if(self == other):
            return self
        if(self._b <= other._a or other._b <= self._a):
            return [self,other]
        elif(self._a <= other._a and self._b >= other._b):
            return self
        elif(self <= other):
            return Interval(self._a,other._b)
        elif(self >= other):
            return Interval(other._a,self._b)
        elif(self._a >= other._a and self._b <= other._b):
            return other

# a = Interval(1,3)
# b = Interval(2,4)
# c = Interval(5,10)
# print(a+b)
# print(b+c)
# print(Interval(2,3)+Interval(1,2) )