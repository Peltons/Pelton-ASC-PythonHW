#!/usr/bin/python

from sys import argv

script, name, age, birthMonth = argv

file = open("customer.txt", "w")

file.truncate()

line1 = "Your name is %s" % name + "\n"
line2 = "You are %s years old" % age + "\n"
line3 = "Your birth month is %s" % birthMonth + "\n"

file.write(line1)
file.write(line2)
file.write(line3)

file.close()

file_input = open("customer.txt")

print file_input.read()

