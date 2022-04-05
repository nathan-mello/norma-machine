class Registador():
    def __init__(self, name):
        ''' 1 = negativo   0 = positivo'''
        self._valor = [0, 0]
        self._name = name

    def getName(self):
        return self._name

    def getValor(self):
        if self._valor[0] == 1:
            return self._valor[1]*-1
        else:
            return self._valor[1]

    def getValorAbsoluto(self):
        return self._valor[1]


    def eZero(self):
        if self._valor[1] == 0:
            return True
        return False

    def ePositivo(self):
        if self._valor[0] == 0:
            return True
        return False

    def encrementa(self):

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

    def getToString(self):
        return self._name + " [ {} , {} ]".format(self._valor[0], self._valor[1])

