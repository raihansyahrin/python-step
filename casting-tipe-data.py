#casting data atau merubah data

#INT
print("====INTEGER====")
dataInt = 9
print("Data=", dataInt, "type:", type(dataInt))

dataFloat = float(dataInt)
dataString = str(dataInt)
dataBoolean = bool(dataInt) #akan bernilai False jika Int = 0
print("Data=", dataFloat, "type:", type(dataFloat))
print("Data=", dataString, "type:", type(dataString))
print("Data=", dataBoolean, "type:", type(dataBoolean))

#FLOAT
print("====FLOAT====")
dataFloat = 9.9
print("Data=", dataFloat, "type:", type(dataFloat))

dataInt = int(dataFloat) #akan membulatkan ke bawah
dataString = str(dataFloat)
dataBoolean = bool(dataFloat) #akan bernilai Falsa jika Float = 0
print("Data=", dataInt, "type:", type(dataInt))
print("Data=", dataString, "type:", type(dataString))
print("Data=", dataBoolean, "type:", type(dataBoolean))

#BOOLEAN
print("====BOOLEAN====")
dataBoolean = False
print("Data=", dataBoolean, "type:", type(dataBoolean))

dataInt = int(dataBoolean) 
dataFloat = float(dataBoolean)
dataString = str(dataBoolean) 
print("Data=", dataInt, "type:", type(dataInt))
print("Data=", dataFloat, "type:", type(dataFloat))
print("Data=", dataString, "type:", type(dataString))

#STRING
print("====STRING====")
dataString = "314"
print("Data=", dataString, "type:", type(dataString))

dataInt = int(dataString) #harus masukin angka
dataFloat = float(dataString) #harus masukin angka
dataBoolean = bool(dataString) #akan False jika str Kosong
print("Data=", dataInt, "type:", type(dataInt))
print("Data=", dataFloat, "type:", type(dataFloat))
print("Data=", dataBoolean, "type:", type(dataBoolean))
