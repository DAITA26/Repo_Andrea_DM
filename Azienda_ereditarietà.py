class Employee:
    def __init__(self, name, h_pay):
        self.name = name
        self.h_pay = h_pay

    def calc_mensile(self):
        rml = self.h_pay * 8 * 20
        return rml

    def calc_tredicesima(self):
        tredicesima = self.calc_mensile() * 0.8
        return tredicesima

    def calc_wage(self):
        ral = self.calc_mensile() * 12 + self.calc_tredicesima()
        print(f"""Ciao sono {self.name} e prendo {self.h_pay}€ all'ora. 
Il mio stipendio mensile è di {self.calc_mensile()}€.
Includendo la tredicesima di {self.calc_tredicesima()}€, prendo {ral}€ annualmente.""")
        return ral


class Manager(Employee):
    # variabile di classe
    yearly_bonus = 20

    def __init__(self, name, h_pay, division):
        super().__init__(name, h_pay)
        self.division = division

    def calc_wage(self):
        ral = super().calc_wage() * (100 + self.yearly_bonus) / 100
        print(f"Con il bonus del {self.yearly_bonus}%, annualmente prendo {ral}€.")
        return ral


class Clerk(Employee):
    def __init__(self, name, h_pay, boss):
        super().__init__(name, h_pay)
        self.boss = boss


class Intern(Clerk):
    forfait = 500

    def __init__(self, name, boss):
        super().__init__(name, 0, boss)

    # override del metodo calc_wage()
    def calc_wage(self):
        ral = self.forfait * 12
        print(f"""Ciao sono {self.name}.
Il mio stipendio mensile è di {self.forfait}€. 
All'anno prende {ral}€ al mese.""")
        return ral


print("--------------------------------------------------------------------")
obj1 = Manager("Marco il manager", 50, "XXX")
# print(type(obj1.calc_wage()))
# print(type(obj1.calc_tredicesima()))
obj1.calc_wage()
print("--------------------------------------------------------------------")
obj2 = Clerk("Mario un dipendente", 30, obj1)
obj2.calc_wage()
print("--------------------------------------------------------------------")
obj3 = Intern("Maria la stagista", obj1)
obj3.calc_wage()