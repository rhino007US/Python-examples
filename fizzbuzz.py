#!/bin/python

#def fizzbuzz(n):
#   result = []
#
#    for x in range(1, n+1):   
#    creating an empty list
lst = []
 
# number of elements as input
# number of elements as input
n = int(input("Enter number of elements : "))
#
print("Enter the elements 20,21,34,55,20,37,42,34: ")
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    if  ele % 3 == 0:
        print(ele, ' is divisible by 3')
    elif ele % 5 == 0:
        print(ele,' is divisible by 5')
    elif ele % 2 == 0:
        print(ele,' is even')
    else:
        print(ele,' is odd')


#def main():
#   print(', '.join(fizzbuzz(20)))

#main()

#if __name__ == '__main__':
#   n = int(input().strip())

#   fizzbuzz(n)