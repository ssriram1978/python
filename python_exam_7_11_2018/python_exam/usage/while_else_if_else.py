print("***********Demonstrating while else ***********************")
n = 5
while n != 0:
    print(n)
    n -= 1
else:
    print("what the...")

print("***********Demonstrating for else ***********************")
n = 5
for n in range(5, -1, -1):
    print(n)
else:
    print("what the...")