# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local-> Enclosed >- Global >- Built-in

#Local: variables declared with in a function have a local scope

""" def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2() """

# ENclosed: a function within a function

""" def func1():
    x = 1
    def func2():
        print(x)
    func2()
func1() """

# Global: outside of the function will givr the value

""" def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2() """

# Buit in -- 
#here in this ex it will take e value as 3 instead of 2.71 because it will check in order global cones first

from math import e
def func1():
    print(e)

e = 3
func1()

