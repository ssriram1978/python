#How to convert an integer to binary format?
n = -37
print("bin(-37)={}".format(bin(n)))
print("n.bit_length()={}".format(n.bit_length()))
#How to convert an integer to hex bytes format that is big endian or little endian>
n=1024
x=n.to_bytes(2,byteorder='big')
print(x)
#How to decode a byte array into an integer?
y=int.from_bytes(x, byteorder='big')
print(y)

z=eval("5+3-2")
print(z)
exec("zz=5+3-2")
print(zz)
