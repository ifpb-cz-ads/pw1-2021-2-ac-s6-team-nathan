menu=0
entre=1
while menu != 0 or entre == 1:
    entre=0
    validador=0
    print('Digite o numero escolhido para a tabuada')
    numero=int(input())
    print('Digite 1 para adição')
    print('Digite 2 para subtração')
    print('Digite 3 para multiplicação')
    print('Digite 4 para divisão')
    print('Digite 0 para sair')
    menu=int(input())
    if menu == 1:
        contador=1
        validador = 1
        while contador <= 10:
            resultado = numero+contador
            string='{} + {}={}'
            print(string.format(numero,contador,resultado))
            contador=contador+1
    if menu == 2:
        contador=1
        validador = 1
        while contador <= 10:
            resultado = numero-contador
            string='{} - {}={}'
            print(string.format(numero,contador,resultado))
            contador=contador+1
    if menu == 3:
        contador=1
        validador = 1
        while contador <= 10:
            resultado = numero*contador
            string='{} x {}={}'
            print(string.format(numero,contador,resultado))
            contador=contador+1
    if menu == 4:
        contador=1
        validador = 1
        while contador <= 10:
            resultado = numero/contador
            string='{} / {}={}'
            print(string.format(numero,contador,resultado))
            contador=contador+1
    if menu == 0:
        validador = 1
        print('Saida com sucesso')
    if validador != 1:
        print('Numero de Opereção invalído')
