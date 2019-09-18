# agregar contacto
# remover contacto
# actualizar contacto
# ver un contacto
# ver todos los contactos
Agenda = dict()


def agregarContacto():
    nombre = input('Escribe el nombre: ')
    numero = input('Escribe el numero: ')
    Agenda[nombre] = numero
    print()
    print('Se ha agregado el contacto')


def eliminarContacto():
    eliminar = input('Escribe el contacto a eliminar:')
    del Agenda[eliminar]
    print('Se ha eliminado el contacto')


def actualizarContacto():
    nombre = input('escribe el contacto a actualizar: ')
    numero = input('Escribe el nuevo numero: ')
    Agenda[nombre] = numero
    print('Se actualizo el contacto')


def verUncontacto():
    contacto = input('Escribe el contacto a ver: ')
    print(contacto + ' - ' + Agenda[contacto])


def verContacto():
    for a in Agenda:
        print(a + ' - ' + Agenda)


print('Bienvenido a la agenda de contactos')
while True:
    print('Elige una opcion: ')
    print()
    print('1 - Agregar contacto')
    print('2 - Eliminar contacto')
    print('3 - Actualizar contacto')
    print('4 - Ver un contacto')
    print('5 - Salir')
    opcion = int(input(': '))
    print()

    if opcion == 1:
        agregarContacto()
    elif opcion == 2:
        eliminarContacto()
    elif opcion == 3:
        actualizarContacto()
    elif opcion == 4:
        verUncontacto()
    elif opcion == 5:
        verContacto()
    else:
        print('Gracias')
        break;
