from enum import Enum, auto


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


def tokenNumber(lista):
    listaSaida = []
    lista.reverse()
    while len(lista) != 0:
        item = lista.pop()

        if item.getTipo() == Tipos.NUMERO:
            cont = item.getConteudo()
            bool = True
            while (bool and len(lista) > 0):
                item = lista.pop()
                if item == Tipos.NUMERO:
                    cont += item.getConteudo()
                else:
                    bool = False
                    lista.append(item)
            listaSaida.append(no(cont, Tipos.NUMERO))

        elif item.getTipo() == Tipos.OPERACAO:
            listaSaida.append(item)

        elif item.getTipo() == Tipos.AUXILIARES:
            cont = ''
            bool = True
            while bool:
                item = lista.pop()
                if item.getTipo() != Tipos.AUXILIARES:
                    cont += item.getConteudo()
                else:
                    bool = False
            if cont != "":
                try:
                    int(cont)
                    listaSaida.append(no(cont, Tipos.NUMERO))
                except ValueError:
                    listaSaida.append(no(cont, Tipos.ERRO))

        elif item.getTipo() == Tipos.ERRO:
            listaSaida.append(item)

    return listaSaida


def token(expresao):
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
            except ValueError:
                lista.append(no(i, Tipos.ERRO))

    return tokenNumber(lista)
