#Bienvenido al programa.
print("---------------------------------------------")
print("¡BIENVENIDO AL PROGRAMA DE NÚMEROS NATURALES!")
print("---------------------------------------------")

#Programa de numeros naturales
cantidad_num = int(input("Ingresa la cantidad de números: "))
i = 1
nums = []
positivos = 0
negativos = 0
nulos = 0
#Pidiendo al usuario que ingrese los digitos a evaluar
while i <= cantidad_num:
    while True:
        numero = input(f"Ingrese su {i}° numero: ")
        if numero.isalpha() == True :
           print("!! El valor ingresado no es un numeros, Ingrese un numero !!")
        else:
            if int(numero) < 0:
                nums.append(int(numero))
                break
            nums.append(int(numero))
            break
    i += 1
#evaluando si lo numeros son positivos negativos o nulos
for n in nums:
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        nulos += 1
# Mostrar los resultados
print("================================================================")
print("====================       Resultados      =====================")
print("================================================================")


print(f"La Cantidad de numeros positivos que Ingresastes son: {positivos}")
print(f"La Cantidad de numeros negativos que Ingresastes son: {negativos}")
print(f"La Cantidad de numeros nulos que Ingresastes son: {nulos}")

print('''EL PROGRAMA A TERMINADO
GRACIAS POR UTILIZARLO''')

    