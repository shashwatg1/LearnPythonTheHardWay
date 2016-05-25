# ex13: Parameters, Unpacking, Variables

#here we pass values using argument
#we import the sys module
from sys import argv

script, first_name, age, height, weight = argv

print "The script is called:", script
print "Your first name is:", first_name
print "Your age is:", age
print "Your height is %d inches" % int(height)
print "Your weight is %d kg" % int(weight)

last_name = raw_input("What's your last name? ")

print "Your full name is %s %s." % (first_name, last_name)