from tabulate import tabulate
from datetime import datetime
from datetime import timedelta

libros = []
socios = []
prestamos = []
multas = []

#funciones generales
def menu():
    while(True):
        cadena = '''
            1. (L)ibros
            2. (S)ocios
            3. (P)restamos
            4. (M)ultas
            5. (O)salir
        '''
        print(cadena)
        opcion = input("Ingresa una opción: ").lower().strip()
        if (opcion == "l"):
            menuLibros()
        elif (opcion == "s"):
            menuSocios()
        elif (opcion == "p"):
            generarPrestamo()

            print(prestamos)
        elif (opcion == "m"):
            pass
        elif (opcion == "o"):
            print("Saliendo del sistema...")
            exit(0)
        else:
            print("No es una opción correcta, intenta de nuevo...\n")
            continue

def menuLibros():
    while(True):
        cadena = '''
            1. (R)egistrar libro
            2. (B)uscar libro
            3. (A)ctualizar libro
            4. (E)liminar libro
            5. (I)nforme libros
            6. (D)evolver al menú anterior
        '''
        print(cadena)
        opcion = input("Ingresa una opción: ").lower().strip()
        if (opcion == "r"):
            registrarLibro()
        elif (opcion == "b"):
            libro = buscarLibroID()
            if (libro != None ):
                imprimirLibro(libro)
            else:
                print("El identificador del libro no pertenece a ninguno registrado.")
        elif (opcion == "a"):
            pass
        elif (opcion == "e"):
            pass
        elif (opcion == "i"):
            listarLibros()
        elif (opcion == "d"):
            break
        else:
            print("No es una opción correcta, intenta de nuevo...\n")
            continue

#funciones libros
def registrarLibro():
    newLibro={}
    print("Registro de libro nuevo al sistema\n")
    ID = int(input("Ingrese el codigo del libro: "))
    titulo=input("Ingresa el titulo del libro: ").capitalize()
    autor=input("Ingresa el autor del libro: ").capitalize()
    anioedicion=int(input("Ingresa el año de edición del libro: "))
    ejemplares = int(input("Ingresa la cantidad de ejemplares disponibles: "))
    newLibro["codigo"] = ID
    newLibro["titulo"] = titulo
    newLibro["autor"] = autor
    newLibro["anioedicion"] = anioedicion
    newLibro["ejemplares"] = ejemplares
    newLibro["prestados"] = 0
    libros.append(newLibro)
    print(libros)
    print("El libro fue registrado exitosamente...\n")
    tab = input("Presione enter para continuar...\n")
    #print(libros)


#Función para listar los libros registrados en el sistema...
def listarLibros():
    listaLibros= []
    print("Listado de libros registrados\n")
    for i in libros:
        valores = i.values()
        listaLibros.append(valores)
    print(tabulate(listaLibros, headers=["Codigo", "Titulo", "Autor", "Edición", "Ejemplares", "Prestados"]))
    tab = input("\nPresione enter para continuar...\n")

#Función para buscar un libro y retornarlo
def buscarLibroID():
    print("\nBusqueda de libro en el sistema por su identificación:")
    id = int(input("Ingrese el indentificador del libro que desea buscar: "))
    for i in libros:
        if (i["codigo"]) == id:
            return i
    return None

def buscarLibroporID(id):
    for i in libros:
        if (i["codigo"]) == id:
            return i
    return None

#Función para ver los datos de un libro
def imprimirLibro(datosLibro):
    libro = []
    print("Datos del libro buscado\n")
    valores = datosLibro.values()
    libro.append(valores)
    print(tabulate(libro, headers=["Codigo", "Titulo", "Autor", "Edición", "Ejemplares", "Prestados"]))
    tab = input("\nPresione enter para continuar...\n")

#Función para actualizar datos de un libro
def actualizarLibro():
    pass

#Función para eliminar un libro, si ninguno de sus ejemplares se encuentra prestado.
def eliminarLibroID(id):
    pass


#Funciones referentes al socio
def menuSocios():
    while(True):
        cadena = '''
            1. (R)egistrar socio
            2. (B)uscar socio
            3. (A)ctualizar socio
            4. (E)liminar socio
            5. (I)nforme socios
            6. (D)evolver al menú anterior
        '''
        print(cadena)
        opcion = input("Ingresa una opción: ").lower().strip()
        if (opcion == "r"):
            registrarSocio()
        elif (opcion == "b"):
            socio = buscarSocioCedula()
            if (socio != None ):
                imprimirSocio(socio)
            else:
                print("El identificador del socio no pertenece a ninguno registrado.")
        elif (opcion == "a"):
            pass
        elif (opcion == "e"):
            pass
        elif (opcion == "i"):
            listarSocios()
        elif (opcion == "d"):
            break
        else:
            print("\nNo es una opción correcta, intenta de nuevo...\n")
            continue

#Función para registrar un socio
def registrarSocio():
    newSocio={}
    print("Registro de un socio nuevo al sistema\n")
    cedula = input("Ingrese la identificación del socio: ")
    nombre = input("Ingresa el nombre del socio: ").capitalize()
    direccion = input("Ingresa la dirección del socio: ").capitalize()
    telefono = input("Ingresa el telefono del socio: ")
    newSocio["cedula"] = cedula
    newSocio["nombre"] = nombre
    newSocio["direccion"] = direccion
    newSocio["telefono"] = telefono
    newSocio["librosenprestamo"] = 0
    socios.append(newSocio)
    print("El socio fue registrado exitosamente...")
    tab = input("\nPresione enter para continuar...\n")

#Función para listar los socios registrados
def listarSocios():
    listaSocios= []
    print("Listado de socios registrados\n")
    for i in socios:
        valores = i.values()
        listaSocios.append(valores)
    print(tabulate(listaSocios, headers=["Identificación", "Nombre", "Dirección", "Telefono", "Libros en prestamo"]))
    tab = input("\nPresione enter para continuar...\n")

#Función para buscar un socio y retornarlo
def buscarSocioCedula():
    print("\nBusqueda de socio en el sistema por su identificación:")
    id = int(input("Ingrese el indentificador del socio que desea buscar: "))
    for i in socios:
        if (i["cedula"]) == id:
            return i
    return None

def buscarSocioCedulaParametro(cedula):
    print("\nBusqueda de socio en el sistema por su identificación:")
    for i in socios:
        if (i["cedula"]) == cedula:
            return i
    return None

def imprimirSocio(datosSocio):
    socio = []
    print("Datos del socio buscado\n")
    valores = datosSocio.values()
    socio.append(valores)
    print(tabulate(socio, headers=["Identificación", "Nombre", "Dirección", "Telefono", "Libros en prestamo"]))
    tab = input("\nPresione enter para continuar...\n")

#Función para actualizar datos de un socio
def actualizarSocio():
    pass

#Función para eliminar un socio, si no tiene libros en prestamo.
def eliminarSocio(cedula):
    pass

#Funciones para prestamos de libros por socios - Maximo 3 libros por socio
def generarPrestamo():
    prestamo = {}
    print("Modulo de prestamos de libros")
    cedulaUsuario = input("Ingresa la identificación del usuario: ")
    socio = buscarSocioCedulaParametro(cedulaUsuario)
    print(socio)
    if (socio != None ):
        IDlibro = int(input("Ingrese el codigo del libro a prestar: "))   
        libro = buscarLibroporID(IDlibro)
        if (libro != None):
            prestamo["cedula"] = cedulaUsuario
            prestamo["codigo"] = IDlibro
            ahora = datetime.now()
            prestamo["fecha_prestamo"] = ahora
            prestamo["fecha_devolucion"] = ahora + timedelta(days=10)
            prestamos.append(prestamo)
            actualizarPrestamoSocio(cedulaUsuario)
            actualizarPrestamosLibro(IDlibro)
            print("El prestamos se realizo satisfactoriamente...")
            tab = input("\nPresione enter para continuar...\n")
        else:
            print("El codigo del libro no coincide con ninguno registrado.")
            tab = input("\nPresione enter para continuar...\n")
    else:
            print("El identificador del socio no pertenece a ninguno registrado.")
            tab = input("\nPresione enter para continuar...\n")

def actualizarPrestamoSocio(cedula):
    for i in socios:
        if (i["cedula"] == cedula):
            i["librosenprestamo"] += 1


def actualizarPrestamosLibro(IDlibro):
    for i in libros:
        if (i["codigo"] == IDlibro):
            i["ejemplares"] -= 1
            i["prestados"] += 1
    