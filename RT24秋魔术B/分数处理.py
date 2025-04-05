#RT Lesson Fraction V1.0
def gcf(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def tongfen(f1, f2):
    d = f1.deno * f2.deno
    nf1 = Fraction(f1.nume * f2.deno, d)
    nf2 = Fraction(f2.nume * f1.deno, d)
    return (nf1, nf2)
class Fraction(object):
    def __init__(self, nume, deno):
        self.nume = nume
        self.deno = deno
    def display(self):
        print(self.nume, '/', self.deno)
    def simplify(self):
        n = gcf(self.nume, self.deno)
        self.nume //= n
        self.deno //= n
    def add(self, f2):
        nf1, nf2 = tongfen(self, f2)
        f = Fraction(nf1.nume + nf2.nume, nf1.deno)
        f.simplify()
        return f
    def c(self, f2):
        na1, na2 = tongfen(self, f2)
        f = Fraction(nf1.nume * na2.nume, na1.deno)
        f.simplify()
        return f
#----
n1, d1 = eval(input('n1, d1 = '))
f1 = Fraction(n1, d1)
f1.display()
n2, d2 = eval(input('n2, d2 = '))
f2 = Fraction(n2, d2)
f2.display()
f1.add(f2).display()
