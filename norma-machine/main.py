from .objectos import normaMachine
from enum import Enum, auto
from flask import Flask, render_template, request


norma = normaMachine.NormaMachine()
app = Flask(__name__)

class no:
    def __init__(self, lexema, tipo):
        self.conteudo = lexema
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def getConteudo(self):
        return self.conteudo

    def toString(self):
        return "({}, {})".format(self.conteudo, self.tipo)


class Tipos(Enum):
    OPERACAO = "-", "+", "*"
    NUMERO = auto()
    AUXILIARES = "[", "]"
    ERRO = auto()


def token(expresao):
    retorno = []
    lista = []
    for i in expresao:
        if i in Tipos.OPERACAO.value:
            noChar = no(i, Tipos.OPERACAO)
            lista.append(noChar)

        elif i in Tipos.AUXILIARES.value:
            noChar = no(i, Tipos.AUXILIARES)
            lista.append(noChar)

        else:
            try:
                int(i)
                lista.append(no(i, Tipos.NUMERO))
            except(ValueError):
                norma.conteudo.append("valor não identificado: " + i)
                lista.append(no(i, Tipos.ERRO))

    dir = 0
    while len(lista) != 0:
        if lista[dir].getTipo() == Tipos.NUMERO:
            cont = ''
            for i in lista[dir:]:
                if i.getTipo() == Tipos.NUMERO:
                    cont += i.getConteudo()
                    lista.remove(i)
                else:
                    break
            retorno.append(no(cont, Tipos.NUMERO))
        elif lista[dir].getTipo() == Tipos.OPERACAO:
            retorno.append(lista[dir])
            lista.remove(lista[dir])
        elif lista[dir].getTipo() == Tipos.AUXILIARES:
            lista.remove(lista[dir])
            cont = ''
            for i in lista[dir:]:
                if i.getTipo() != Tipos.AUXILIARES:
                    cont += i.getConteudo()
                    lista.remove(i)
                else:
                    lista.remove(i)
                    break
            if cont != "":
                try:
                    int(cont)
                    retorno.append(no(cont, Tipos.NUMERO))
                except ValueError:
                    retorno.append(no(cont, Tipos.OPERACAO))
        elif lista[dir].getTipo() == Tipos.ERRO:
            retorno.append(lista[dir])
            lista.remove(lista[dir])

    return retorno


def inicializaRegistador(lista):
    for index in range(len(lista)):
        if lista[index].getTipo() == Tipos.NUMERO:
            lista[index] = norma.inicializarRegistadores(int(lista[index].getConteudo()))

    return lista


def readLista(lista):
    for index in range(len(lista)):

        if type(lista[index]) is no:

            if lista[index].getTipo() == Tipos.ERRO:
                norma.conteudo.append("Caracter não aceito pela maquina: {}".format(lista[index].getConteudo()))
                return []

            elif (lista[index].getTipo() == Tipos.OPERACAO and index > 0
                    and type(lista[index - 1]) == normaMachine.Registador
                    and type(lista[index + 1]) == normaMachine.Registador):

                operando1 = lista[index - 1]
                operando2 = lista[index + 1]

                if lista[index].getConteudo() == "-":
                    result = norma.sub(operando1, operando2)
                    lista.remove(lista[index])
                    lista.remove(lista[index - 1])
                    lista[index - 1] = result
                    return lista


                elif lista[index].getConteudo() == "+":
                    result = norma.adicao(operando1, operando2)
                    lista.remove(lista[index])
                    lista.remove(lista[index - 1])
                    lista[index - 1] = result
                    return lista

                elif lista[index].getConteudo() == "*":
                    result = norma.multi(operando1, operando2)
                    lista.remove(lista[index])
                    lista.remove(lista[index - 1])
                    lista[index - 1] = result
                    return lista

            elif lista[index].getTipo() == Tipos.OPERACAO and index == 0:
                norma.conteudo.append("Operação invalida. Erro de sinal")
                return []
            elif lista[index].getTipo() == Tipos.OPERACAO:
                norma.conteudo.append("Operação invalida.")
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
    while len(lista) > 1:
        lista = readLista(lista)

    back = ''
    if len(lista) != 0:
        for i in norma.conteudo:
            back += i + "\n"
        back += "Registador: " + lista[0].toString() + "\n"
        back += "Registador: " + str(lista[0].getValor())
    else:
        for i in norma.conteudo:
            back += i + "\n"

    retorno += '<textarea class="textarea" rows="20" cols="60" disabled>' \
               + back + '</textarea> ' + '</div>' + '</div>'

    return render_template('main.html', rpt=retorno)


@app.route('/sobre')
def about():
    return render_template('about.html')
