#---------0+++++++5--------8++++++11--------   
user_input = float(input("Masukkan angka lebih dari 0 dan kurang dari 5\natau \nlebih dari 8 dan kurang dari 11:"))

lebih_0 = user_input > 0 
kurang_5 = user_input < 5

is_correct = lebih_0 and kurang_5  

lebih_8 = user_input > 8
kurang_11 = user_input < 11

is_correct2 = lebih_8 and kurang_11

all_is_correct = is_correct or is_correct2

print("Jawaban anda:", all_is_correct)

#print("Jawaban anda:", is_correct)
#print("Jawaban anda:", is_correct2)

print(18*'=')


# ++++++++0-------5++++++8-----11+++++++++
user_input = float(input("Masukkan angka kurang dari 0\natau \nlebih dari 5 dan kurang dari 8\natau \nlebih dari 11 :"))

kurang_0 = user_input < 0

lebih_5 = user_input > 5
kurang_8 = user_input < 8

lebih_11 = user_input > 11

apa_benar = lebih_5 and kurang_8

apa_semua_benar = kurang_0 or apa_benar or lebih_11

print("Jawaban kamu:", apa_semua_benar)




