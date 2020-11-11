#Tabla de multiplicar eficiente

print("////GENERADOR DE TABLAS DE MULTIPLICAR/////")
print("********************************************\n")

num = int(input("Digita el numero del que deseas obtener la tabla: "))
limite= int(input("¿Hasta que numero deseas multiplicarlo?: "))

contador = 1
                  
while contador <= limite:
    resultado = contador * num
    print("{} x {} = {}".format( num, contador, resultado))
    
    contador = contador + 1

