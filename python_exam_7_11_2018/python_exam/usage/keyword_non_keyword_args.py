
def non_keyword_args(*args):
    for index,value in enumerate(args):
        print("index={},value={}".format(index,value))
    for value in args:
        print("value={}".format(value))

def keyword_args(**args):
    for name,value in args.items():
        print("name={},value={}".format(name, value))

def mixed(a,b,c,*args):
    print("a={},b={},c={}".format(a,b,c))
    for value in args:
        print("value={}".format(value))

def fn1(a,b=1):
    print(a,b)

non_keyword_args("abc","xyz","def")
dict1={'abc' : 1 , "345" : 2, "678" : '4'}
keyword_args(**dict1)
mixed("abc","xyz","def","1","2","3")

#keyword argument
fn1(b=1,a=2)
fn1(b=1,*(3,))
fn1(1,b=3)
fn1(a=2,b=3)
fn1(a=100)

