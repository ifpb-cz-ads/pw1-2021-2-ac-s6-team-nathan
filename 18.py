numero1=int(input("Digite o numero dividido"))
numero2=int(input("Digite o numero divisor"))
while numero2 <= numero1:
    numero1=numero1-numero2
print("O resto da divisao e igual a %d" % (numero1))