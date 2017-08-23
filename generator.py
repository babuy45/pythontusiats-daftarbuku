# generators are iterators

def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)

# EXAMPLE GENERATOR which calculates fibonacci number

def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
        return result

# generator next

def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#iterable digunakan di string

#my_string = "Yasoob"
#my_iter = iter(my_string)
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))
