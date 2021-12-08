from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/questao1a', methods=['POST'])
def questao1a():
    x = 1
    while x <= 100:
        if x == 1:
            string_numeros = '1'
            x = x + 1
        else:
            string_numeros = string_numeros + " %d" % (x)
            x = x + 1
    return '<h1>%s</h1>' % (string_numeros)


@app.route('/questao1b', methods=['POST'])
def questao1b():
    x = 50
    while x <= 100:
        if x == 50:
            string_numeros = '50'
            x = x + 1
        else:
            string_numeros = string_numeros + " %d" % (x)
            x = x + 1
    return '<h1>%s</h1>' % (string_numeros)


@app.route('/questao2', methods=['POST'])
def questao2():
    x = 10
    while x >= 0:
        if x == 10:
            string_numeros = '10'
            x = x - 1
        else:
            string_numeros = string_numeros + " %d" % (x)
            x = x - 1
    return '<h1>%s Fogo!</h1>' % (string_numeros)


@app.route('/questao3', methods=['POST'])
def questao3():
    numero_parada = request.form['numero']
    numero_parada = int(numero_parada)
    x = 1
    while x <= numero_parada:
        if x == 1:
            string_numeros = '1'
            x = x + 2
        else:
            string_numeros = string_numeros + " %d" % (x)
            x = x + 2
    return '<h1>%s</h1>' % (string_numeros)


@app.route('/questao4', methods=['POST'])
def questao4():
    x = 3
    y = 1
    while y <= 10:
        if x == 3:
            string_numeros = '3'
            y = y + 1
            x = y * 3
        else:
            string_numeros = string_numeros + " %d" % (x)
            y = y + 1
            x = y * 3
    return '<h1>%s</h1>' % (string_numeros)


@app.route('/questao5', methods=['POST'])
def questao5():
    x = request.form['numero']
    x = int(x)
    y = 1
    while y <= 10:
        if y == 1:
            z = y * x
            string_numeros = '%d x 1=%d ;' % (x, z)
            y = y + 1
        else:
            z = y * x
            string_numeros = string_numeros + ' %d x %d = %d  ;' % (x, y, z)
            y = y + 1
    return '<h1>%s</h1>' % (string_numeros)


@app.route('/questao6', methods=['POST'])
def questao6():
    numero_tabuada = request.form['numero1']
    numero_tabuada = int(numero_tabuada)
    numero_comeco = request.form['numero2']
    numero_comeco = int(numero_comeco)
    numero_parada = request.form['numero3']
    numero_parada = int(numero_parada)
    y = numero_comeco
    x = numero_tabuada
    while y <= numero_parada:
        if y == numero_comeco:
            z = y * x
            string_numeros = '%d x %d=%d ' % (x, y, z)
            y = y + 1
        else:
            z = y * x
            string_numeros = string_numeros + '%d x %d = %d  ;' % (x, y, z)
            y = y + 1
    return '<h1>%s</h1>' % (string_numeros)


@app.route('/questao7', methods=['POST'])
def questao7():
    numero_tabuada = request.form['numero1']
    numero_tabuada = int(numero_tabuada)
    numero_vezes = request.form['numero2']
    numero_vezes = int(numero_vezes)
    y = 1
    x = numero_tabuada
    z = x
    while y < numero_vezes:
        x = x + z
        y = y + 1
    return '<h1>%d</h1>' % (x)


@app.route('/questao8', methods=['POST'])
def questao8():
    numero_tabuada = request.form['numero1']
    numero_tabuada = int(numero_tabuada)
    numero_vezes = request.form['numero2']
    numero_vezes = int(numero_vezes)
    y = 0
    x = numero_tabuada
    z = numero_vezes
    while x >= z:
        x = x - z
        y = y + 1
    r = x
    return '<h1>%d quociente %d resto</h1>' % (y, r)


@app.route('/questao9', methods=['POST'])
def questao9():
    resposta1 = request.form['questao01']
    resposta2 = request.form['questao02']
    resposta3 = request.form['questao03']
    pontos = 0
    questao = 1
    while questao <= 3:
        if questao == 1:
            if resposta1 == "B" or resposta1 == "b":
                pontos = pontos + 1
        if questao == 2:
            if resposta2 == "A" or resposta2 == "a":
                pontos = pontos + 1
        if questao == 3:
            if resposta3 == "D" or resposta3 == "d":
                pontos = pontos + 1
        questao = questao + 1
    return '<h1>%d</h1>' % (pontos)

@app.route('/questao10',  methods=['POST'])
def questao10():
    deposito=request.form['deposito']
    deposito=int(deposito)
    juros=request.form['juros']
    juros=float(juros)
    juros=juros/100
    meses=0
    poupanca=deposito
    string_numeros='Os valores da sua poupança são: '
    while meses < 12:
        deposito=deposito+deposito * juros
        string_numeros= string_numeros + '  %.2f  ;' % (deposito)
        meses=meses + 1
    juros_valor=deposito-poupanca
    return '<h1>%s e o valor total dos juros acumulados é igual a %.2f</h1>' % (string_numeros,juros_valor)

@app.route('/questao11',  methods=['POST'])
def questao11():
    deposito=request.form['deposito']
    deposito=int(deposito)
    juros=request.form['juros']
    juros=float(juros)
    juros=juros/100
    salario=request.form['salario']
    salario=float(salario)
    meses=0
    poupanca=deposito
    string_numeros='Os valores da sua poupança são: '
    while meses < 12:
        deposito=salario+deposito+deposito * juros
        string_numeros= string_numeros + '  %.2f  ;' % (deposito)
        meses=meses + 1
    juros_valor=deposito-poupanca
    return '<h1>%s e o valor total dos juros acumulados é igual a %.2f</h1>' % (string_numeros,juros_valor)

@app.route('/questao12',  methods=['POST'])
def questao12():
    divida = request.form['divida']
    divida = int(divida)
    juros = request.form['juros']
    juros = float(juros)
    juros = juros / 100
    valor_pago_mes = request.form['valor_pago_mes']
    valor_pago_mes = float(valor_pago_mes)
    string_numeros = 'Os valor total pago é de:'
    valor_pago=0
    meses=0
    divida_inicial=divida
    divida_descontada=divida
    while valor_pago < divida_descontada:
        valor_pago=valor_pago+valor_pago_mes
        divida=divida+divida*juros
        divida_descontada=divida-valor_pago
        meses=meses + 1
    string_numeros=string_numeros + '%.2f' % (divida)
    juros_valor=divida-divida_inicial
    return '<h1>%s e o valor total dos juros acumulados é igual a %.2f e a quantidade de meses é igual a %d</h1>' % (string_numeros, juros_valor,meses)
