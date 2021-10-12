# >,<,>=,<=,==,!=,is,is not

a = 4
b = 3

# kurang dari <
print("======== KURANG DARI <")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = a < 4
print(a,'<',4,'=',hasil)
hasil = a < b 
print(a,'<',b,'=',hasil)

# lebih dari >
print("======== LEBIH DARI DARI >")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = a > 4
print(a,'>',4,'=',hasil)
hasil = a > b 
print(a,'>',b,'=',hasil)

# Kurang dari sama dengan >=
print("======= KURANG DARI SAMA DENGAN >=")
hasil = a <= 5
print(a,'<=',5,'=',hasil)
hasil = a <= 4
print(a,'<=',4,'=',hasil)
hasil = a <= b 
print(a,'<=',b,'=',hasil)

# Lebih dari sama dengan >=
print("======= LEBIH DARI SAMA DENGAN >=")
hasil = a >= 5
print(a,'>=',5,'=',hasil)
hasil = a >= 4
print(a,'>=',4,'=',hasil)
hasil = a >= b 
print(a,'>=',b,'=',hasil)

# Sama Dengan ==
print("======= SAMA DENGAN ==")
hasil = a == 5
print(a,'==',5,'=',hasil)
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = a == b 
print(a,'==',b,'=',hasil)

# tidak Sama Dengan !=
print("======= TIDAK SAMA DENGAN !=")
hasil = a != 5
print(a,'!=',5,'=',hasil)
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = a != b 
print(a,'!=',b,'=',hasil)

# Komparasi menggunakan is (Hanya untuk membandingkan objek saja, BUKAN value)
print("======== SAMA DENGAN OBJEK is ") 
hasil = a is b 
print(a,'is',b,'=',hasil)
# a itu literal, makanya bisa di komparasi dengan objek, sedangkan value bukan literal

#Komparasi menggunakan is not (hanya untuk objek)
print("========= is not")
hasil = a is not b 
print(a,'is not',b,'=',hasil)

