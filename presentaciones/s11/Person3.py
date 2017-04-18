import datetime
class Person:
    poblacion = 0

    def __init__(self, name,edad):
        self.name = name
        self.edad = edad
        Person.poblacion += 1
        self.getpob()

    def say_hi(self):
        print('Hello, my name is', self.name, " y tengo ",self.edad, "años")

    def getpob(self):
        print("la poblacion es: ", Person.poblacion)


class Reloj:

    def gettime(self):
        time = datetime.datetime.now()
        print(time)

reloj = Reloj()
reloj.gettime()
p = Person('Rolo',21)
s = Person('Santiago',20)

s.say_hi()
p.say_hi()



# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()
