# ex17: More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "The input file is %d bytes long" % len(open(from_file).read())

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

open(to_file, 'w').write(open(from_file).read())

print "Alright, all done."