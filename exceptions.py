# There are many types of exceptions, value, index, type, etc.  You can even raise your own exception
# simpliest
# if x < 0:
#    raise Exception('x should not be less than 1')
x = -6
# or assert()
assert(x <= 0), 'x is not positive'

try:
     a = 5/0
except Exception as e:
    print('an exception occured', e)

# except ZeroDivisionError as e:
# except TypeError as e:  # specific errors
else:
    print('everything is fine')
finally:
    print('cleaning up...') # runs, no matter if there are exceptions.. cleanup operations

# improved define our own Class exceptiuons
class ValueTooHighError(Exception): # Exception is the base class
    pass
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high', x)
    if x < 5:
        raise ValueTooLowError('value is too low', x)


# more advanced
class ValueTooLowError(Exception):
    def _init_(self, message, value):
     self.message = message
     self.value = value

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)