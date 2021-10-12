
#++++++++++3---------10++++++
#menggabungkan menggunakan atau (OR)

user_input = float(input("Masukkan angka\nkurang dari 3\natau\nlebih dari 10\n:"))
print(user_input)

is_kurang_dari = user_input < 3
print("Kurang dari 3:",is_kurang_dari)

is_lebih_dari = user_input > 10
print("Lebih dari 10:", is_lebih_dari)

is_correct = is_kurang_dari or is_lebih_dari
print("Jawaban anda:", is_correct)


print("=========KASUS IRISAN=======")
#-------------------3++++++++++++10------------
# irisan menggunakan and
user_input = float(input("Masukkan angka\nlebih dari 3\ndan\nkurang dari 10\n:"))
print(user_input)

is_kurang_dari = user_input < 10
print("Kurang dari 10:",is_kurang_dari)

is_lebih_dari = user_input > 3
print("Lebih dari 3:", is_lebih_dari)

is_correct = is_kurang_dari and is_lebih_dari
print("Jawaban anda:", is_correct)



#------0+++++5-----8++++++11--------
