class Registador:
    def __init__(self, name):
        # 1 = negativo   0 = positivo
        self._valor = [0, 0]
        self._name = name

    def getName(self):
        return self._name

    def getValor(self):
        if self._valor[0] == 1:
            return self._valor[1] * -1
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

            self.__encrementa()
            self._valor[0] = 0
        elif not self.ePositivo():
            self.__decrementa()
        else:
            self.__encrementa()

    def decrementa(self):

        if self.eZero() and self.ePositivo():
            self._valor[0] = 1
            self.__encrementa()
        elif self.ePositivo():
            self.__decrementa()
        else:
            self.__encrementa()

    def __encrementa(self):
        self._valor[1] += 1

    def __decrementa(self):
        self._valor[1] -= 1

    def toString(self):
        return "     " + self._name + ":  [ {} , {} ]".format(self._valor[0], self._valor[1])
