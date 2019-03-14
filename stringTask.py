# Simple Python list manipulation - Problems:
# Create a list of numbers from 1 to 100, including 1 and 100.
# Use list comprehension to square every number in the list.
# Create a function to get the square root of a number,
# and use that function to efficiently get the square root of every number in the second list.
# Try to code using your own algorithms as much as possible.

# Invariant
inputList = range(1, 101)
squaredList = [x * x for x in inputList]

# 1st option
def getsqrt1(pvalue):
    return [inputList[squaredList.index(pvalue)]]


for el in squaredList:
    print("sqrt(", el, ")=", getsqrt1(el))


# 2nd option
def getsqrt2(pidx):
    return [inputList[pidx]]


for i in range(0, 100):
    print("sqrt2(", squaredList[i], ")=", getsqrt2(i))