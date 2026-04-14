# Presentacion y ejemplo de for
# #Ejemplo simple
# for i in range(3):
#     print("repeticion N", i+1)

# # Repeticiones dadas por el usuario
# # Pida al usuariio un numero 
# # y mustre un saludo esa cant 
# # de veces.

# num=int(input("Ingrese un num: "))
# for i in range(num):
#     print(i+1, "Hola usuario")

# # Pida al usuariio un numero 
# # muestre la tabla de multiplicar
# # de ese numero hasta el 10.

# num=int(input("Ingrese un num: "))
# for i in range(10):
#     print(num ,"x",i+1, "=", num*(i+1))

# # Pedir al usuario la cantidad de notas
# # sacar el promedio para esa cantidad de notas
# # insertar notas con decimales

# num=int(input("Ingrese la cant de notas: "))
# suma=0
# for i in range(num):
#     nota=float(input("Ingresa la nota: "))
#     suma=suma+nota
# prom=suma/num
# print("El promedio es", prom)
# if prom >=4:
#     print("El alumno aprobó")
# else:
#     print("El alumno reprobó")
# cantLetra=0
# for i in "Diego":
#     print(i) 
# #Pida al usuario su nombre y mustre la cant
# # de caracteres del mismo

# nombre=input("Ingrese su nombre")
# cantLetra=nombre
# for i in nombre:
#     print(i) 
#     cantLetra+=1
# print("La cant de caracteres es", cantLetra)

# solo cuenta vocales

nombre=input("Ingrese su nombre: ")
cantLetra=0
for i in nombre:
    if i in "aeiouAEIOU":
        cantLetra+=1
print("La cant de vocales es", cantLetra)