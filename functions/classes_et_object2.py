class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =age
        

    def nickname_giver(self, hint):
        self.nickname = hint + self.name[0:5]


felix = Person('Felix', 45)
yomi =Person("Abayomi", 98)

felix.nickname_giver('BOOK')
yomi.nickname_giver('FOOD')

print(felix.nickname)
print(yomi.nickname)