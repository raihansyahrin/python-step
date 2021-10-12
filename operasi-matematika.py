#operasi matematika
a = 10
b = 3

#operasi pertambahan +
hasil = a + b
print(a,'+',b,'=',hasil)

#operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

#operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

#operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

#operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

#operasi modulus (sisa bagi) %
hasil = a % b
print(a,'%',b,'=',hasil)

#operasi floor division (dibulatkan kebawah) //
hasil = a // b
print(a,'//',b,'=',hasil)

#prioritas perhitungan
'''
    1.()
    2.Eksponen **
    3.Perkalian dkk, * / ** % //
    4.Pertambahan dan Pengurangan
'''
x = 2
y = 3
z = 1

hasil = x ** z + y / z % x * x - y 
print(x,'**',z,'+',y,'/',z,'%',x,'*',x,'-',y,'//',z,'=',hasil) 

