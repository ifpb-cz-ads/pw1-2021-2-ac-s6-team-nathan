numero=int(input("Digite um numero"))
e_impar=numero % 2
resultado=1
contador=0
if numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 2 != 7:
    print('O numero é impar e primo')
else:
    print('O numero é par e não primo')
