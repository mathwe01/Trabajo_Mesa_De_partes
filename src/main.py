from archivos import cargar_archivo
from expedientes import registrar_expediente, listar_expedientes
from busqueda import buscar_expediente

def mostrar_menu():
    print("=== Menú Principal ===")
    print("1. Registrar ")
    print("2. Buscar por código")
    print("3. Listar")
    print("4. Salir")

def main():
    codigos, dnis, nombres, direcciones, tramites, asuntos, fechas = cargar_archivo()
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Elija una opción: ")
        print()
    
        if opcion == "1":
            registrar_expediente(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas)
        elif opcion == "2":
            print("Aquí ira buscar_expediente()")
        elif opcion == "3":
            print("Aquí ira listar_expedientes()")
        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opcion no valida, por favor elija una opción del 1 al 4.")
if __name__ == "__main__": 
    main()