# Strings: ordered, immutable, text representation
# %s, .format(), f-strings
# oldest method
var1 = "Tom"
mystring = "The variable is %s" % var1
print(mystring)
# old method
var2 = 2.12345
# mystring2 = "The variable is %d" % var2
mystring2 = "The variable is %.2f" % var2
print(mystring2)

mystring3 = "the newer format method var is {:.2f} amd {}".format(var2, var1)
print(mystring3)
# new in python 3.6
mystring3 = f"the variables are {var1 * 2} and {var2}"
print(mystring3)

