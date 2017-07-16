nombres = ["Sergio", "Samuel", "Antonio", "Felipe"]
edad = ["30", "20", "59", "14"]

for i in range(0,len(edad)+1):
    print("hola {1}, de {0} anhos ").format(nombres[i],edad[i])
