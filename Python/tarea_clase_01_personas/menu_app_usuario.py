from usuario import Usuario
from usuario_dao import UsuarioDao

class MenuAppUsuario:
    """Clase que muestra y maneja el menú de usuarios"""
    
    @staticmethod
    def mostrar_menu():
        """Muestra el menú y gestiona las opciones"""
        while True:
            print("\n--- Menú Usuarios ---")
            print("1) Listar usuarios")
            print("2) Agregar usuario")
            print("3) Actualizar usuario")
            print("4) Eliminar usuario")
            print("5) Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                # Listar usuarios
                usuarios = UsuarioDao.seleccionar()
                for usuario in usuarios:
                    print(usuario)

            elif opcion == '2':
                # Agregar usuario
                username = input("Ingrese username: ")
                password = input("Ingrese password: ")
                usuario = Usuario(username=username, password=password)
                UsuarioDao.insertar(usuario)

            elif opcion == '3':
                # Actualizar usuario
                id_usuario = int(input("Ingrese ID del usuario a actualizar: "))
                username = input("Nuevo username: ")
                password = input("Nuevo password: ")
                usuario = Usuario(id_usuario=id_usuario, username=username, password=password)
                UsuarioDao.actualizar(usuario)

            elif opcion == '4':
                # Eliminar usuario
                id_usuario = int(input("Ingrese ID del usuario a eliminar: "))
                usuario = Usuario(id_usuario=id_usuario)
                UsuarioDao.eliminar(usuario)

            elif opcion == '5':
                # Salir del programa
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida")
