# functions that take in generators
def generator_function(number):
    for index in range(1, number + 1):
        yield index


def generator_function2(start, end):
    return [(x, x ** 2) for x in range(start, end) if x != 2]


x = 10
print("factorial of a number {} is =".format(x), end=" ")
for number in generator_function(x):
    print("{}".format(number), end="*")
print('\n')
print("generator_function2(2, 5)={}".format(generator_function2(2, 5)))


def hold_client(name):
    yield "Hello, %s You will be connected soon" %(name)
    yield 'Dear %s, could you please wait a bit.' % name
    yield 'Sorry %s, we will play a nice music for you!' % name
    yield '%s, your call is extremely important to us!' % name

the_fn_pointer=hold_client("sriram")

print(next(the_fn_pointer))
print(next(the_fn_pointer))
print(next(the_fn_pointer))
print(next(the_fn_pointer))

the_fn_pointer=hold_client("sriram2")

for x in the_fn_pointer:
    print(x)

def fibonacci(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        prev, curr = curr, prev + curr
        counter += 1
the_fn_pointer2=fibonacci(3)
print(next(the_fn_pointer2))
print(next(the_fn_pointer2))
print(next(the_fn_pointer2))

print(list(map(sum, zip([1, 2, 3], [4, 5, 6]))))


def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

for char in reverse("sriram1"):
    print(char)
