from collections import defaultdict

def Fibonacci_recurse(number, cache):
    if number == 0 or number == 1:
        return number
    if cache[number] == 0:
        cache[number] = Fibonacci_recurse(number - 1,cache) + Fibonacci_recurse(number - 2,cache)
    return cache[number]

def Fibonacci_nonrecurse(number):
    if number==0:
        return 0
    if number==1:
        return 1
    a=0
    b=1
    for index in range(2,number,+1):
        temp=a+b
        a=b
        b=temp

    return a+b

def Fibonacci(number):
    cache = defaultdict(int)
    return Fibonacci_recurse(number, cache)

print(Fibonacci(4))
print(Fibonacci_nonrecurse(4))
