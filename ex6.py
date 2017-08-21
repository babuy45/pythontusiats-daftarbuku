## TRY to learn string and text

x = ("There are %d types of people." % 10)
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s."  % (binary, do_not)

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of ..."
e = "a string with a right side."

print (w + e)

##ex 8 printing, printing, printing

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
    "I had this thing."
    "That you could type up right"
    "BUt it didn'tsing."
    "So I said goodnight."
))