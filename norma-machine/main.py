from objectos import normaMachine
from enum import Enum, auto


class no:
    def __init__(self, dexema, tipo):
        self.conteudo = dexema
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
                print("valor não identificado: " + i)
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
                except(ValueError):
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

            if (lista[index].getTipo() == Tipos.OPERACAO
                    and type(lista[index - 1]) is normaMachine.Registador
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


            elif lista[index].getTipo() == Tipos.ERRO:
                print("Caracter não aceito pela maquina: {}".format(lista[index].getConteudo()))
                erro = []
                return erro


norma = normaMachine.NormaMachine()
entrada = input("Digite a operação: ")
lista = inicializaRegistador(token(entrada))


while len(lista) > 1:
    lista = readLista(lista)

if len(lista) != 0:
    print(lista[0].getToString())
    print(lista[0].getValor())