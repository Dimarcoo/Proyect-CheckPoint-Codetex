import random

print ('===================')
print ('== MISTERY SPACE ==')
print ('===================')


opcion = str (input('Deseas iniciar esta aventura: '))
gas = 10
#while opcion != 'Y' or opcion != 'N':
if opcion == 'Y':
    print('Hola, Bienvenido a una gran aventura en el espacio')
    name = str (input('Dinos tú nombre: '))
    print('Bienvenido ', name + ', desde hoy haces parte de la misión para colonizar marte')
    print (name + 'desde hoy eres subteniente')
    
    while gas >= 1:
        print ('La misión T314 esta ha empezado \n'
        'Estás a cargo!!')

        print('Elige una de las siguientes opciones: \n' \
        '1) Cruzar Galaxia Andromeda \n' \
        '2) Rodear Galaxia Andromeda')
        mision1 = int (input('Elige tu opcion. '))

        if mision1 == 1:
            gas = gas + +1
        elif mision1 == 2:
            gas = gas -2

        break
        
    

elif opcion == 'N':
    print ('Bye')
else:
    print('Digite una opcion valida: "Y" o "N"')
