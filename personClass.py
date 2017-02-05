#!/usr/bin/python

class Person():
    def __init__(self, name):
        self.Name = name

    def ShowData(self):
        for attr, value in self.__dict__.iteritems():
            print "%s: %s" % (attr, value)

class Student(Person):
    def __init__(self, name, education):
        Person.__init__(self, name)
        self.Education = education

class Worker(Person):
    def __init__(self, name, work):
        Person.__init__(self, name)
        self.WorkPlace = work

class Academy():
    def __init__(self):
        self.academy = []

    def ShowAll(self):
        for person in self.academy:
            print person.ShowData()

    def AddPerson(self, person):
        self.academy.append(person)

