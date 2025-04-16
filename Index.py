#EL DIRECTOR  de una revista para adultos, contacta para realizar la interfaz de bienvenida para el sitio web
#1. preguntar su user, 2. clave, 3. de no tener debe registrarse (user, nombre, edad (de no tener 18, chao, si es mayor pasa y es registrado))

print ("\---Bienvenido PajinXXX---")

user = input("\n Porfavor, ingrese su usuario: ")
clave = int(input("Ingrese su clave: "))

if user == "Jenn" and clave == 12345:
   print (f"Bienvenid@ {user}, Disfrute del contenido ;)")

else:
   print ("\nNo esta registrado, ¿Desea registrarse? S/N")

   respuesta = input().strip
   if respuesta == "S":
      Nuevo_nom = input("\nIngrese su nombre")
      user_nuevo = (input("\nIngrese su user nuevo"))
      edad_nueva = int(input("¿cual es su edad?"))
      clave_nueva = input("\nIngrese una clave")
      user[user_nuevo] = clave_nueva
if user_nuevo not in user:
            user[user_nuevo] = clave_nueva
            if edad_nueva <= 18:
                print(f"Usuario {user_nuevo} se registró exitosamente!!")
            else:
                print(f"Usuario {user_nuevo} se registró exitosamente!!")
else:
            print("El nombre de usuario ya está registrado.")


print(f"Usuarios registrados: {user.keys()}")

            
 

 
