#RT Lwsson Fraction V1.0
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
    def mul(self, f2):
        f = Fraction(self.nume * f2.nume, self.deno * f2.deno)
        f.simplify()
        return f
        
#----main----
n1, d1 = eval(input('n1, d1 = '))
f1 = Fraction(n1, d1)
f1.display()
n2, d2 = eval(input('n2, d2 = '))
f2 = Fraction(n2, d2)
f2.display()
n3, d3 = eval(input('n3, d3 = '))
f3 = Fraction(n3, d3)
f3.display()
n4, d4 = eval(input('n4, d4 = '))
f4 = Fraction(n4, d4)
f4.display()
##nf = f1.add(f2)
##nf.display()
xxx = f1.mul(f2.add(f3)).add(f4)
xxx.display()
