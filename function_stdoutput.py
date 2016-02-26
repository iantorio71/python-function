#! /usr/bin/python

def MyFunc(name, age):
    print "Hi! My Name is, ", name + " and my age is", age
    print "Hi! My Name is %s, and  my age is %d"%(name, age)
    print "Hi! My name is {} and my age is {}".format(name, age)

MyFunc("Mary", 19)
