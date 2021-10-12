# operator bitwise, operator binary, operator biner

a = 9
b = 5

# bitwise OR (|)
print("\n==========OR============")
c = a | b
print("nilai:",a,", binary:",format(a,'08b'))
print("nilai:",b,", binary:",format(b,'08b'))
print("----------------------------(|)")
print("nilai:",c,", binary:",format(c,'08b'))

# bitwise AND (&)
print("\n============AND===========")
c = a & b
print("nilai:",a,", binary:",format(a,'08b'))
print("nilai:",b,", binary:",format(b,'08b'))
print("----------------------------(&)")
print("nilai:",c,", binary:",format(c,'08b'))

# bitwise XOR (^)
print("\n============XOR===========")
c = a ^ b
print("nilai:",a,", binary:",format(a,'08b'))
print("nilai:",b,", binary:",format(b,'08b'))
print("----------------------------(^)")
print("nilai:",c,", binary:",format(c,'08b'))

# bitwise NOT(~)
print("\n============NOT===========")
c = ~a
print("nilai:",a,", binary:",format(a,'08b'))
print("----------------------------(~)")
print("nilai:",c,", binary:",format(c,'08b'))
print("---------------------------(^)") #gunain XOR kalo mau persis kebalikan
d = 0b00001001
e = 0b11111111
print("nilai:",e^d,",binary:",format(d^e,'08b'))

# shifting right (>>)
print("\n=============>>================")
c = a >> 2
print("nilai:", a,",binary:",format(a,'08b'))
print("----------------------------->>")
print("nilai:", c,",binary:",format(c,'08b'))

# shifting left (<<)
print("\n=============<<================")
c = a << 2
print("nilai:", a,",binary:",format(a,'08b'))
print("-----------------------------<<")
print("nilai:", c,",binary:",format(c,'08b'))





