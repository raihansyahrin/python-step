
#---------0+++++++5--------8++++++11--------   
user_input = float(input("Masukkan angka lebih dari 0 dan kurang dari 5\natau \nlebih dari 8 dan kurang dari 11:"))

x = 0 < user_input < 5 or 8 < user_input < 11
print("Jawaban kamu: ", x)

print(18*'=')


# ++++++++0-------5++++++8-----11+++++++++
user_input = float(input("Masukkan angka kurang dari 0\natau \nlebih dari 5 dan kurang dari 8\natau \nlebih dari 11 :"))

y = user_input < 0 or 5 < user_input < 8 or user_input > 11
print("Jawaban kamu : ",y )