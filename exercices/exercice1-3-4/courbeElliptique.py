from math import sqrt

class CourbeElliptique:
    a = 0;
    b = 0;

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
        if  4*a**3+27*b**2 == 0:
            raise ValueError('({}, {}) n\'est pas une courbe valide'.format(a, b));

    def __eq__(self, courbeelliptique):
        return self.a == courbeelliptique.a;

    def print(self):
        chaine = 'a:{} b:{}'.format(self.a, self.b);
        print(chaine);

    def testPoint(self, x, y):
        if y**2 != x**3 + self.a * x + self.b:
            return False;
        return True;

c = CourbeElliptique(1,1);
c.print();
print(c.testPoint(2,sqrt(11)))
print(c.testPoint(2,12))

