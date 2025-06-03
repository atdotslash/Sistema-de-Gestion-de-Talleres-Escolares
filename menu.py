import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import style

# Suponiendo que luego crearás módulos como: usuarios.py, herramientas.py, mantenimientos.py, asignaciones.py
import sistema.usuarios as usuarios
import sistema.herramientas as herramientas
import sistema.mantenimientos as mantenimientos
import sistema.asignaciones as asignaciones


def menu():
    style.header("Sistema de Gestión de Talleres Escolares")
    print()
    print(f"{style.Colors.magenta}   >>> Seleccione una opción\n{style.Colors.reset}")
    option = input(
        "    1 - Gestión de Usuarios\n"
        "    2 - Gestión de Herramientas y Máquinas\n"
        "    3 - Gestión de Mantenimientos\n"
        "    4 - Gestión de Asignaciones / Préstamos\n"
        "\n    0 - Salir\n\n")

    match option:
        case '1':
            print('\n\n')
            menuUsuarios()
            menu()
        case '2':
            print('\n\n')
            menuHerramientas()
            menu()
        case '3':
            print('\n\n')
            menuMantenimientos()
            menu()
        case '4':
            print('\n\n')
            menuAsignaciones()
            menu()
        case '0':
            print()
            style.footer()
            sys.exit(0)
        case _:
            print()
            print(f"{style.Colors.yellow}Opción no disponible, elija otra opción{style.Colors.reset}")
            print()
            menu()


def menuUsuarios():
    style.header("Gestión de Usuarios")
    print()
    option = input(
        "    1 - Crear Usuario\n"
        "    2 - Editar Usuario\n"
        "    3 - Eliminar Usuario\n"
        "    4 - Listar / Buscar Usuarios\n"
        "\n    0 - Volver al menú principal\n\n")

    match option:
        case '1': usuarios.crear_usuario(); menuUsuarios()
        case '2': usuarios.editar_usuario(); menuUsuarios()
        case '3': usuarios.eliminar_usuario(); menuUsuarios()
        case '4': usuarios.listar_usuarios(); menuUsuarios()
        case '0': return
        case _: print(f"{style.Colors.yellow}Opción no disponible{style.Colors.reset}"); menuUsuarios()


def menuHerramientas():
    style.header("Gestión de Herramientas y Máquinas")
    print()
    option = input(
        "    1 - Registrar Herramienta/Máquina\n"
        "    2 - Editar\n"
        "    3 - Eliminar\n"
        "    4 - Cambiar Estado\n"
        "    5 - Buscar/Listar\n"
        "\n    0 - Volver\n\n")

    match option:
        case '1': herramientas.crear(); menuHerramientas()
        case '2': herramientas.editar(); menuHerramientas()
        case '3': herramientas.eliminar(); menuHerramientas()
        case '4': herramientas.cambiar_estado(); menuHerramientas()
        case '5': herramientas.listar(); menuHerramientas()
        case '0': return
        case _: print(f"{style.Colors.yellow}Opción no disponible{style.Colors.reset}"); menuHerramientas()


def menuMantenimientos():
    style.header("Gestión de Mantenimientos")
    print()
    option = input(
        "    1 - Registrar Mantenimiento\n"
        "    2 - Ver Historial\n"
        "\n    0 - Volver\n\n")

    match option:
        case '1': mantenimientos.registrar(); menuMantenimientos()
        case '2': mantenimientos.historial(); menuMantenimientos()
        case '0': return
        case _: print(f"{style.Colors.yellow}Opción no disponible{style.Colors.reset}"); menuMantenimientos()


def menuAsignaciones():
    style.header("Gestión de Asignaciones / Préstamos")
    print()
    option = input(
        "    1 - Registrar Préstamo\n"
        "    2 - Registrar Devolución\n"
        "    3 - Historial por Usuario\n"
        "    4 - Historial por Herramienta\n"
        "\n    0 - Volver\n\n")

    match option:
        case '1': asignaciones.prestar(); menuAsignaciones()
        case '2': asignaciones.devolver(); menuAsignaciones()
        case '3': asignaciones.historial_usuario(); menuAsignaciones()
        case '4': asignaciones.historial_herramienta(); menuAsignaciones()
        case '0': return
        case _: print(f"{style.Colors.yellow}Opción no disponible{style.Colors.reset}"); menuAsignaciones()


# Inicio del programa
style.start()
menu()
