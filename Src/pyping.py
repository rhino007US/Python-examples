import time
from pythonping import ping
true = 1
i = 0
while i < 255:
    i += 1
    print(i)
    a = 0
    while a < 255:

        a += 1
        print(a)
        b = 0
        while b < 255:
            b += 1
            print(b)
            c = 0
            while c < 255:
              def foo():
                  return(print(str(i) + ".", end = ""), print(str(a) + ".", end = ""), print(str(b) + ".", end = ""), print(c))
                  c += 1
                while (True):
                      print(foo())
#                ping(foo, verbose=True)
                      time.sleep(1)