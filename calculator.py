import math

print ('===============')
print ('AREA CALCULATOR')
print ('===============')

print ('1) Triangle')
print ('2) Rectangle')
print ('3) Square')
print ('4) Circle')
print ('5) Quit')

op = int (input('Por favor seleccione la opción de la figura a calcular: '))

if op == 1:
    altura = float (input('Ingrese la altura del triangulo: '))
    base = float (input ('Ingrese la base del triangulo: '))
    area =  float (altura * base)/2
elif op == 2:
    longitud = float (input('Ingrese la longitud del rectangulo: '))
    ancho = float (input('Ingrese el ancho del rectangulo: '))
    area = float (longitud * ancho)
elif op == 3:
    lado = float (input('Ingrese el lado del cuadrado: '))
    area = math.pow(lado, 2)
elif op == 4:
    radio = float (input('Ingrese el radio del circúlo: '))
    area = math.pi * math.pow(radio, 2)
elif op == 5:
        print ('See You Later!!')
        area = ('No hay información disponible')
else:
    print ('Seleccione una opción correcta')

print ('El área de la figura seleccionada es: ' , area)