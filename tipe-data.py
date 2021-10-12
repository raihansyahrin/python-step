#data Integer, data yang satuan tidak ada koma
dataInt = 100 
print("data:", dataInt, "Bertipe:" , type(dataInt)) 

#data Float, data yang bernilai desimal
dataFloat = 1.34 
print("data:", dataFloat, "Bertipe:" , type(dataFloat)) 

#data String, data yang berisi kumpulan karakter dan memakai ""
dataString = "Raihan" 
print("data:", dataString, "Bertipe:", type(dataString)) 

#data Boolean, data True/False (Boolean)
dataBiner = True
print("data:", dataBiner, "Bertipe:", type(dataBiner))

## tipe data khusus

#bilangan complex,
dataComplex = complex(4,5)
print("data:", dataComplex, "Bertipe:", type(dataComplex))

#data dari bahasa C
from ctypes import c_double #bisa c_char. c_long, c_boole, dll.
dataCDouble = c_double(10.5)
print("data:", dataCDouble , "bertipe:" , type(dataCDouble))
