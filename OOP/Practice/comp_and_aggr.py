class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old.'

class Address(object):

    def __init__(self, city, street, hnumber):
        self.city = city
        self.street = street
        self.hnumber = hnumber

    def __str__(self):
        return f'{self.city}, {self.street}, {self.hnumber}'


class Job(object):

    def __init__(self, position, salary):
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'{self.position}, {self.salary}'


# Composition
class Kid(object):

    def __init__(self, name, age, city, street, hnumber):
        self.person = Person(name, age)
        # self.name = self.person.name
        self.address = Address(city, street, hnumber)


john = Kid('John', 7, 'New York', 'BW51', 15)

print(john.person.name)
print(john.address.street)

#Aggergation
class KidAggregation(object):

    def __init__(self, person, address):
        self.person = person
        self.address = address

wick = Person('Wick', 12)
wick_address = Address('Dallas', 'BW20', 13)

kid = KidAggregation(wick, wick_address)

print(kid.person.name)