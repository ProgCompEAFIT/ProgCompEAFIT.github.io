import Person3

class Person:
    poblacion = 0

    def __init__(self, name,edad,altura,reloj):
        self.name = name
        self.edad = edad
        Person.poblacion += 1
        self.getpob()
        self.altura = altura
        self.reloj = reloj

    def say_hi(self):
        print('Hello, my name is', self.name, " y tengo ",self.edad, "años")

    def getpob(self):
        print("la poblacion es: ", Person.poblacion)

    def saltar(self):
        print("yo ",self.name, " he saltado ", self.altura/4," centimetros")


class NBAPerson(Person):
    def saltar(self):
        print("yo ",self.name, " he saltado ", self.altura/2," centimetros")

reloj = Person3.Reloj()

p = Person('Rolo',21,175,reloj)
#s = NBAPerson('Santiago',20,171)
#r = NBAPerson('Rodrigo',21,191)

#s.say_hi()
#s.saltar()
p.say_hi()
p.saltar()
#r.say_hi()
#r.saltar()


# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
