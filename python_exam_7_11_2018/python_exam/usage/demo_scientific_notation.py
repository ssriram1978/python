print("****************Demonstrating scientific notation**************")
x = 1.1e-10
print("x={} and x*10={}".format(x, x * 10))

from decimal import Decimal

x = Decimal('40800000000.00000000000000')
print('{:.2e}'.format(x))
