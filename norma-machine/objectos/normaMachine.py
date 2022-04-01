class Registador():
    def __init__(self, name):
        ''' 1 = negativo   0 = positivo'''
        self._valor = [0, 0]
        self._name = name

    def getName(self):
        return self._name

    def getValor(self):
        if self._valor[0] == 1:
            return self._valor*-1
        else:
            return self._valor

    def eZero(self):
        if self._valor[1] == 0:
            return True
        return False

    def ePositivo(self):
        if self._valor[0] == 0:
            return True
        return False

    def encrementa(self):
        '''if self.eZero() and self.ePositivo():
            self._encrementa()'''

        if self.eZero() and not self.ePositivo():
            self._encrementa()
            self._valor[0] = 0
        elif not self.ePositivo():
            self._decrementa()
        else:
            self._encrementa()

    def decrementa(self):

        if self.eZero() and self.ePositivo():
            self._encrementa()
            self._valor[0] = 1
        elif self.ePositivo():
            self._decrementa()
        else:
            self._encrementa()

    def _encrementa(self):
        self._valor[1] += 1
        self.toString()

    def _decrementa(self):
        self._valor[1] -= 1
        self.toString()

    def toString(self):
        print("     " + self._name + ":  [ {} , {} ]".format(self._valor[0], self._valor[1]))

class NormaMachine:
    def __init__(self):
        self.contador = 1

    def inicializarRegistadores(self, valor):
        reg = Registador("Reg_{}".format(self.contador))
        self.contador += 1

        print("Inicializando {} com o valor {}:".format(reg.getName(), valor))
        if valor < 0:
            for i in range(valor * -1):
                reg.decrementa()
        else:
            for i in range(valor):
                reg.encrementa()
        return reg

    def adicao(self, regsitador1, registador2):
        pass

    def sub(self, regitador1, registador2):
        pass

    def div(self, registador1, registador2):
        pass

    def multi(self, restador1, registador2):
        pass
