#latihan perhitungan suhu

celcius = float(input('Masukkan suhu dalam celcius:'))
print("Suhu adalah:",celcius,"C")

reamur = (4/5) * celcius
print("Suhu Reamur= ", reamur , "R")

fahrenheit = ((9/5)*celcius) + 32
print("Suhu Fahrenheit= ",fahrenheit, "F")

kelvin = celcius + 273
print("Suhu Kelvin= ",kelvin, "K")


#fahrenheit ke kelvin
rumusFahrenheit = float(input('Masukkan suhu dalam Fahrenheit:'))
print("suhu adalah:",rumusFahrenheit,"F")

FKelvin = ((rumusFahrenheit - 32) * 5/9) + 273
print("Suhu kelvin:", FKelvin,"K")


#kelvin ke fahrenheit
rumusKelvin = float(input("Masukkan suhu dalam kelvin:"))
print("Suhu adalah:", rumusKelvin,"K")

KFahrenheit = ((rumusKelvin - 273)*9/5) + 32
print("Suhu adalah:",KFahrenheit,"F")
