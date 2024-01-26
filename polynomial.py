class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self):
        if (isinstance(self.p1, Int) & isinstance(self.p2, Int)):
            return self.p1.i + self.p2.i
        if (isinstance(self.p1, Int)):
            return self.p1.i + self.p2.evaluate()
        if (isinstance(self.p2, Int)):
            return self.p1.evaluate() + self.p2.i
        return self.p1.evaluate() + self.p2.evaluate()

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self):
        if (isinstance(self.p1, Int) & isinstance(self.p2, Int)):
            return self.p1.i - self.p2.i
        if (isinstance(self.p1, Int)):
            return self.p1.i - self.p2.evaluate()
        if (isinstance(self.p2, Int)):
            return self.p1.evaluate() - self.p2.i
        return self.p1.evaluate() - self.p2.evaluate()

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if (isinstance(self.p1, Add) | isinstance(self.p1, Sub)):
            if (isinstance(self.p2, Add) | isinstance(self.p2, Sub)):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if (isinstance(self.p2, Add) | isinstance(self.p2, Sub)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self):
        if (isinstance(self.p1, Int) & isinstance(self.p2, Int)):
            return self.p1.i * self.p2.i
        if (isinstance(self.p1, Int)):
            return self.p1.i * self.p2.evaluate()
        if (isinstance(self.p2, Int)):
            return self.p1.evaluate() * self.p2.i
        return self.p1.evaluate() * self.p2.evaluate()

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if (isinstance(self.p1, Add) | isinstance(self.p1, Sub)):
            if (isinstance(self.p2, Add) | isinstance(self.p2, Sub)):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if (isinstance(self.p2, Add) | isinstance(self.p2, Sub)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    
    def evaluate(self):
        if (isinstance(self.p1, Int) & isinstance(self.p2, Int)):
            return self.p1.i / self.p2.i
        if (isinstance(self.p1, Int)):
            return self.p1.i / self.p2.evaluate()
        if (isinstance(self.p2, Int)):
            return self.p1.evaluate() / self.p2.i
        return self.p1.evaluate() / self.p2.evaluate()


poly = Sub( Sub( Int(5), Int(10)), Add( Int(5), Mul( Int(1), Sub( Div(Int(1), Int(1)), Int(1)))))
print(poly)
print(poly.evaluate())