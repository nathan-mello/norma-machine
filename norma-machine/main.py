from .objectos import normaMachine
from flask import Flask, render_template, request
from Token import *

norma = normaMachine.NormaMachine()
app = Flask(__name__)


def inicializaRegistador(lista):
    for index in range(len(lista)):
        item = lista[index]
        if item.getTipo() == Tipos.NUMERO:
            lista[index] = norma.inicializarRegistadores(int(item.getConteudo()))

    return lista


def readList(lista):
    lista.reverse()
    registadores = None

    while len(lista) > 0:

        item = lista.pop()

        if type(item) is no:

            try:
                if item.getTipo() == Tipos.ERRO:
                    norma.conteudo.append("Caracter não aceito pela maquina: {}".format(item.getConteudo()))
                    return []


                elif item.getTipo() == Tipos.OPERACAO and type(lista[-1]) == normaMachine.Registador\
                        and registadores is not None:

                    operador1 = registadores
                    operador2 = lista.pop()

                    if item.getConteudo() == "-":
                        result = norma.sub(operador1, operador2)

                        if len(lista) != 0:
                            lista.append(result)
                        else:
                            norma.conteudo.append("Registador: " + result.toString())
                            norma.conteudo.append("Registador: " + str(result.getValor()))

                    elif item.getConteudo() == "+":
                        result = norma.adicao(operador1, operador2)

                        if len(lista) != 0:
                            lista.append(result)
                        else:
                            norma.conteudo.append("Registador: " + result.toString())
                            norma.conteudo.append("Registador: " + str(result.getValor()))

                    elif item.getConteudo() == "*":
                        result = norma.multi(operador1, operador2)

                        if len(lista) != 0:
                            lista.append(result)
                        else:
                            norma.conteudo.append("Registador: " + result.toString())
                            norma.conteudo.append("Registador: " + str(result.getValor()))

                else:
                    norma.conteudo.append("Operação invalida.")
                    return []
            except(IndexError):
                norma.conteudo.append("Operação invalida.")
                return []

        elif type(item) == normaMachine.Registador:
            registadores = item

    return []


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')


@app.route('/', methods=['POST'])
def result():
    norma.conteudo = []
    retorno = '<div class=" px-4 py-5 my-5 text-center">' \
              + '<div class="container-fluid">'

    exp = request.form['expresao']

    lista = inicializaRegistador(token(exp))
    readList(lista)

    back = ''
    for i in norma.conteudo:
        back += i + "\n"

    retorno += '<textarea class="textarea" rows="20" cols="60" disabled>' \
               + back + '</textarea> ' + '</div>' + '</div>'

    return render_template('main.html', rpt=retorno)


@app.route('/sobre')
def about():
    return render_template('about.html')

