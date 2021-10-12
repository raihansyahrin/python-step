# operasi logika atau boolean

# not, or, and, xor

#not
print("==== NOT ====")
a = True
c = not a
print("data a:",a)
print("============NOT")
print("data c:",c)

#or
#jika salah satu ada yang True, makan hasilnya True.
print("==== OR ====")
a = True
b = True
c = a or b
print(a,'or',b,'=',c)

a = True
b = False
c = a or b
print(a,'or',b,'=',c)

a = False
b = True
c = a or b
print(a,'or',b,'=',c)

a = False
b = False
c = a or b
print(a,'or',b,'=',c)

# and
# jika salah satu ada yang False, maka jawabannya False.
print("==== AND ====")
a = True
b = True
c = a and b
print(a,'and',b,'=',c)

a = True
b = False
c = a and b
print(a,'and',b,'=',c)

a = False
b = True
c = a and b
print(a,'and',b,'=',c)

a = False
b = False
c = a and b
print(a,'and',b,'=',c)

# xor
# akan True, jika salah satu ada yang True. Sisanya False

print("==== XOR ====")
a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)

a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)

