from sys import argv
script, text = argv
txt = open(text)
print "here is your file %r:" % text
print txt.read()