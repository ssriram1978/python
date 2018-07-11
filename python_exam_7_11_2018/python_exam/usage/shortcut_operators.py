print("***********Demonstrating shortcut operators***********************")
def shortcuts():
    x=0
    y=1
    print("x=0 or y=1 x or y operation returns returns {} if x is false, then y, else x".format(x or y))
    x = 2
    y = 3
    print("x=2 or y=3 x or y operation returns {} if x is false, then y, else x ".format(x or y))
    x = 2
    print("x=2 not x returns {} if x is false, then True, else False".format(not x))
    x=0
    print("x=0 not x operation returns {} if x is false, then True, else False".format(not x))
    x = 2
    y = 3
    print("x=2,y=3 x and y operation returns {} if x is false, then x, else y".format(x and y))

    x = 0
    y = 3
    print("x=0,y=3 x and y operation returns {} if x is false, then x, else y".format(x and y))

shortcuts()
