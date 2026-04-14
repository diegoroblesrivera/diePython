# print("Ingrese su nombre")
# nombre=input()
# edad=int(input("Ingrese su edad:() ", ))


# print("Hola", nombre, "su edad en 5 años será", edad+5)

# Pedir 23 nuemros y mostrar la
# suma y las resta de ambos

# n1=int(input("ingrese un numero: "))
# n2=int(input("ingrese otro numero: "))

# print("La suma de los numeros es ", n1+n2)
# print("La resta de los numeros es ", n1-n2)

# calcular el iva para cada compra
print(
'''
1.- Pera 1200
2.- Manzana 1400
3.- Piña 2000
''')
select=int(input("Seleccione una fruta: "))
if select==1:
    print("El total a pagar es", 1200*1.19)
elif select==2:
    print("El total a pagar es", 1400*1.19)
elif select==3:
    print("El total a pagar es", 2000*1.19)
else:
    print("Numero no valido")

