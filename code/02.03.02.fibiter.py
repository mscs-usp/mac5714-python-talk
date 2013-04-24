class Fib:
    def __init__(self):
        self.a = 0 # "f_{n-2}"
        self.b = 1 # "f_{n-1}"

    def next(self):
        ''' next() is the heart of any iterator
        note the use of the following tuple to not only save lines of
        code but also to insure that only the old values of self.fn1 and
        self.fn2 are used in assigning the new values '''
        fib = self.a
        (self.a, self.b) = (self.b, self.a + self.b)
        return fib

    def __iter__(self):
        return self