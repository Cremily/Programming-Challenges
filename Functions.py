from copy import copy


class Term():
    def __init__(self,base,power,multiples):
        self.base = str(base)
        self.power = float(power)
        self.mul = float(multiples)




class Polynomial(Term):
    def __init__(self,base,power,multiples):
        Term.__init__(self,base,power,multiples)
    def display(self):
        a = '{0:g}'.format(self.mul)
        b ='{0:g}'.format(self.power)
        string = str(a) + " * " + str(self.base) + " ^ " + str(b)
        return(string)
    def derive(self):
        orig = self.display()
        save_mul = copy(self.mul)
        save_power = copy(self.power)
        self.mul = self.mul * self.power
        self.power = self.power - 1 
        new = (self.display())
        print("The derivative with respect to %s of %s is %s" % (self.base,orig,new))
        self.mul = save_mul
        self.power = save_power

class NaturalExpo(Term):
    def __init__(self,base,power,multiples):
        Term.__init__(self,base,power,multiples)
    def display(self):
        a = '{0:g}'.format(self.mul)
        b ='{0:g}'.format(self.power)
        string = "(" + str(a) + ") * e ^ (" + str(b) + str(self.base) + ")"
        return(string)
    def derive(self):
        orig = self.display()
        save_mul = copy(self.mul)
        self.mul = self.mul * self.power
        new = self.display()
        print("The derivative with respect to %s of %s is %s" % (self.base,orig,new))
        self.mul = save_mul
class Sine(Term):
    def __init__(self,base,power,multiples,inmul,inpower,inadd):
        Term.__init__(self,base,power,multiples)
        self.inmul = inmul
        self.inpower = inpower
        self.inadd = inadd
    def display(self):
        a = '{0:g}'.format(self.mul)
        b ='{0:g}'.format(self.power)
        c = '{0:g}'.format(self.inmul)
        d ='{0:g}'.format(self.inpower)
        f = '{0:g}'.format(self.inadd)
        string = str(a) + " * sine(" + str(c) + str(self.base) + "^(" + str(d) +") + " + str(f) + ")"
        if b != "1":
            string += " ^ " + b
        print(string)
    def derive(self):
        orig = self.display()
        


        

b = NaturalExpo("x",5,25)
b.derive()
print(b.display())
