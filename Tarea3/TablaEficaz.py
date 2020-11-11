#Tabla de multiplicar eficaz

print("////GENERADOR DE TABLAS DE MULTIPLICAR/////")
print("********************************************\n")
num = int(input("Digita el numero del que deseas obtener la tabla: "))

for i in range(11):
    resultado = i*num
    print ("{} x {} = {}".format(num, i, resultado))
