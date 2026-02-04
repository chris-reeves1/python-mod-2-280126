class Calculator:
    def add(self, a , b):
        if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
            raise TypeError("numeric")
        return a + b
