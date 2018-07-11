print("***********accuracy of floating-point numbers************")
x = 2
y = 3
print("x=1,y=10 x/y=%.1f" % (x / y))
print("x=1,y=10 x/y=%.10f" % (x / y))

x, y = 0.1, 0.1
z = x + y
print(z)
print("x,y,z=0.1,0.1,x+y round(z,10)={}".format(round(z, 10)))
print("repr(0.1+0.1+0.1==0.3) returned {}".format(repr(0.1 + 0.1 + 0.1 == 0.3)))
print("repr(round(0.1 + 0.1 + 0.1,10) == round(0.3,10)) returned {}".format(
    repr(round(0.1 + 0.1 + 0.1, 10) == round(0.3, 10))))
