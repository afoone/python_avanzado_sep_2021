# uso de módulos

from matematica.aritmetica import sumar, restar, multiplicar
from matematica.geometria import hipotenusa
# from aritmetica import *


if __name__ == '__main__':
    print(sumar(3, 6))
    print(restar(3, 6))
    print(multiplicar(4, 4))
    print("hipotenusa", hipotenusa(5, 5))

