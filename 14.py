entre=1
codigo=0
total=0
while codigo != 0 or entre == 1:
    validacao=0
    entre=0
    codigo=int(input("Digite o codigo do produto:"))
    if codigo == 0:
        validacao = 1
    if codigo == 1:
        total=total+0.5
        validacao = 1
    if codigo == 2:
        total=total+1
        validacao = 1
    if codigo == 3:
        total=total+4
        validacao = 1
    if codigo == 5:
        total=total+7
        validacao = 1
    if codigo == 9:
        total=total+8
        validacao = 1
    if validacao == 0:
       print("Codigo invalido")
string="O valor total e igual a {}"
print(string.format(total))