import random

player = 0
computer = 0

print ('1) Rock ✊')
print ('2) Paper ✋')
print ('3) Scissors ✌️')
print ('4) Spock 🖖')
print ('5) Lizard 🦎')
player = int (input('Seleccione su jugada: '))

computer = random.randint(1,5)
#SENTENCIA QUE EVALUA MIENTRAS EL USUARIO ESCOGE PIEDRA
while player == 1:
    if computer == 1:
        print ('Tu: ✊')
        print ('CPU: ✊')
        print ('DRAW')
    elif computer == 2: # Papel aplasta piedra
        print ('Tu: ✊')
        print ('CPU: ✋')
        print ('YOU LOSE!')
    elif computer == 3: # Piedra aplasta Tijera
        print ('Tú: ✊')
        print ('CPU: ✌️')
        print ('YOU WIN!!')
    elif computer == 4: # Spock vaporiza piedra
        print ('Tu: ✊')
        print ('CPU: 🖖')
        print ('YOU LOSE!')
    elif computer == 5: # Piedra aplasta lagarto
        print ('Tú: ✊')
        print ('CPU: 🦎')
        print ('YOU WIN!!')
    break
#Usuario escoge papel
while player == 2:
    if computer == 1: # Papel cubre piedra
        print ('Tu: ✋')
        print ('CPU: ✊')
        print ('YOU WIN!')
    elif computer == 2: # Empate
        print ('Tu: ✋')
        print ('CPU: ✋')
        print ('DRAW')
    elif computer == 3: # Tijeras cortan papel
        print ('Tú: ✋')
        print ('CPU: ✌️')
        print ('YOU LOSE!')
    elif computer == 4: # Papel desaprueba spock
        print ('Tu: ✋')
        print ('CPU: 🖖')
        print ('YOU WIN!')
    elif computer == 5: # Lagarto come papel
        print ('Tú: ✋')
        print ('CPU: 🦎')
        print ('YOU LOSE!')
    
    break
#Usuario escoge Tijeras
while player == 3:
    if computer == 1: # Piedra aplasta tijera
        print ('Tu: ✌️')
        print ('CPU: ✊')
        print ('YOU LOSE!')
    elif computer == 2: # Tijera corta papel
        print ('Tu: ✌️')
        print ('CPU: ✋')
        print ('YOU WIN!')
    elif computer == 3: # Empate
        print ('Tú: ✌️')
        print ('CPU: ✌️')
        print ('DRAW')
    elif computer == 4: #Spock destruye tijeras
        print ('Tu: ✌️')
        print ('CPU: 🖖')
        print ('YOU LOSE!')
    elif computer == 5: # Tijeras decapitan lagarto
        print ('Tu: ✌️')
        print ('CPU: 🦎')
        print ('YOU WIN!')
    break
#SPOCK
while player == 4:
    if computer == 1: # Spock vaporiza piedra
        print ('Tu: 🖖')
        print ('CPU: ✊')
        print ('YOU win!')
    elif computer == 2: # Papel desaprueba spock
        print ('Tu: 🖖')
        print ('CPU: ✋')
        print ('YOU LOSE!')
    elif computer == 3: # Spock destruye Tijeras
        print ('Tú: 🖖')
        print ('CPU: ✌️')
        print ('YOU WIN')
    elif computer == 4: #Empate
        print ('Tu: 🖖')
        print ('CPU: 🖖')
        print ('DRAW!')
    elif computer == 5: # Lagarto envenena Spock
        print ('Tu: 🖖')
        print ('CPU: 🦎')
        print ('YOU LOSE!')
    break
#LIZZARD
while player == 5:
    if computer == 1: # Piedra aplasta lagarto
        print ('Tu: 🦎')
        print ('CPU: ✊')
        print ('YOU LOSE!')
    elif computer == 2: # lagarto come papel
        print ('Tu: 🦎')
        print ('CPU: ✋')
        print ('YOU WIN!')
    elif computer == 3: # Tijeras decapitan Lagarto
        print ('Tú: 🦎')
        print ('CPU: ✌️')
        print ('YOU LOSE!')
    elif computer == 4: #lagarto envenena Spock
        print ('Tu: 🦎')
        print ('CPU: 🖖')
        print ('YOU WIN!')
    elif computer == 5: # Empate
        print ('Tu: 🦎')
        print ('CPU: 🦎')
        print ('DRAW!')
    break