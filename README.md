#Actividad
#el gerente comercial de la tienda de perfume gloria, acaba de decidir mejorar su proceso de venta, eliminando item de su formulario de ventas
#Y para ello lo esta contratando a usted para eliminar varios de ellos.
#El gerente requiere optimizar el tiempo en su fila
#Nro de boleta o factura
#Rut
#Nombre
#Subtotal, IVA, total.
#Perfume M: A que te atrapo, Una excelente noche, Organza, Hugo Red, Amazon
#Perfume H: Lacost, Hugo Boss, Python, JavaSex, C++
#Agregar 50 = 10.000 o 100 Ml = 18.000


perfume_M = ("A que te atrapo, Una excelente noche, Organza, Hugo Red, Amazon")
perfume_H = ("Lacost, Hugo Boss, Python, JavaSex, C++")


Precios_ML = {
    50: 10000,
    100: 18000
}

rut = input("Ingrese su rut del cliente: ")

nombre = input("Ingrese nombre de cliente: ")

nro_boleta = input("Ingrese el Nro. de boleta o factura: ")

print ("\nPerfume para Mujer:")
for i, perfume in enumerate (perfume_M, 1):
 print (f"{i}. {perfume}")1



print ("\nPerfume para Hombre:")
for i, perfume in enumerate (perfume_H, 1):
 print (f"{i}. {perfume}")

Tipo_perfume = input("\nQue tipo de perfume va a desear: Perfume (M) o Perfume (H)").upper()

if Tipo_perfume == "M":
    Tipo_perfume == perfume_M
else: 
 Tipo_perfume == perfume_H

 opcion = int(input("Seleccione el numero de su perfume: "))
 perfume_elegido = Tipo_perfume [opcion - 1]
cantidad = int(input("¿50 Ml o 100 Ml?: "))

precioU = [cantidad]
Subtotal = precioU
Iva = Subtotal * 0.19
Total = Subtotal + Iva

print ("\n---Boleta---")
print (f"Numero de boleta: {nro_boleta}")
print (f"Cliente: {nombre} - Rut: {rut}")
print (f"Perfumes Elegidos: {perfume_elegido} ({cantidad} Ml)")
print (f"Subtotal: {Subtotal}")
print (f"Iva (19%): {Iva}")
print (f"Total: {Total}")
