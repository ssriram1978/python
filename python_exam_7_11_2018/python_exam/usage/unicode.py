
x='​abc'.encode()
print(x)


z=x.decode("utf-8", "replace")
print(z)

a = chr(40960) + 'abcd' + chr(1972)
print(a)
v=a.encode('utf-8')
print(v)

e=None
try:
    e=v.decode("utf-8", "strict")
except UnicodeDecodeError:
    print('\'utf-8\' codec can\'t decode byte 0x80 in position 0')

print(e)
