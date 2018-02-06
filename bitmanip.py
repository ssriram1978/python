#you are given two 32 bit numbers n and m and two bit positions i and j.
#write a method to insert m into n such that m starts at bit j and ends at bit i.
#you can assume that bits j to i have enough space to fit all of m.
#if m is 10011 there are atleast 5 bits between j and i.
#example: input N = 10000000000, M = 10011, i=2 and j=6
#output: N = 10001001100

def insert_m_into_n(n,m,i,j):
    if m<=0 or n<=0 or j-i <=0:
        return None
    #move m in such a way to align it between i and j.
    print("Before left shift:"+str(bin(m)))
    m = m << i
    print("after left shift"+ str(bin(m)))
    print("input n before =" + str(bin(n)))
    output=n | m
    print("n after ="+str(bin(output)))

insert_m_into_n(int(0b10000000000),int(0b10011),2,6)

