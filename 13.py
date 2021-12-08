numero = 0
numero_acumulado = 0
entre = 1
quantidade = 0
while numero != 0 or entre == 1:
    entre = 0
    numero = input("Digite um numero")
    numero = int(numero)
    numero_acumulado = numero_acumulado + numero
    if numero != 0:
        quantidade = quantidade + 1
media = numero_acumulado / quantidade
media = float(media)
string = "A quantidade de numero digitada foi igual a {} a soma é igual a {} e a media e igual a {}"
print(string.format(quantidade, numero_acumulado, media))
