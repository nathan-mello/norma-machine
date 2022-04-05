from .registador import Registador

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

    def adicao(self, registador1, registador2):

        print("adicionando {}[{}] ao {}[{}]:"
              .format(registador1.getName(),
                      registador1.getValor(),
                      registador2.getName(),
                      registador2.getValor()))

        if registador1.ePositivo() and registador2.ePositivo():
            while registador2.getValor() != 0:
                registador1.encrementa()
                registador2.decrementa()
            return registador1

        elif not registador1.ePositivo() and not registador2.ePositivo():
            while registador2.getValor() != 0:
                registador1.decrementa()
                registador2.encrementa()
            return registador1

        else:
            if registador1.getValorAbsoluto() < registador2.getValorAbsoluto() and registador1.ePositivo():
                while registador1.getValor() != 0:
                    registador2.encrementa()
                    registador1.decrementa()
                return registador2
            elif registador1.getValorAbsoluto() < registador2.getValorAbsoluto() and not registador1.ePositivo():
                while registador1.getValor() != 0:
                    registador2.decrementa()
                    registador1.encrementa()
                return registador2
            elif registador1.getValorAbsoluto() > registador2.getValorAbsoluto() and registador1.ePositivo():
                while registador2.getValor() != 0:
                    registador2.encrementa()
                    registador1.decrementa()
                return registador1
            elif registador1.getValorAbsoluto() > registador2.getValorAbsoluto() and not registador1.ePositivo():
                while registador2.getValor() != 0:
                    registador2.decrementa()
                    registador1.encrementa()
                return registador1
            else:
                if registador1.ePositivo():
                    while registador1.getValor() != 0:
                        registador1.decrementa()
                        registador2.encrementa()
                    return registador1
                else:
                    while registador1.getValor() != 0:
                        registador1.encrementa()
                        registador2.decrementa()
                    return registador1

    def adicaoC(self, registadorA, registadorB, registadorC):

        while registadorB.getValor() != 0:
            registadorA.encrementa()
            registadorC.encrementa()
            registadorB.decrementa()

        while registadorC.getValor() != 0:
            registadorB.encrementa()
            registadorC.decrementa()

    def sub(self, registador1, registador2):
        print("subtraindo {}[{}] ao {}[{}]:"
              .format(registador1.getName(),
                      registador1.getValor(),
                      registador2.getName(),
                      registador2.getValor()))

        if not registador1.ePositivo() and not registador2.ePositivo():
            while registador2.getValor() != 0:
                registador1.decrementa()
                registador2.encrementa()
            return registador1

        elif registador1.ePositivo() and registador2.ePositivo():
            while registador2.getValor() != 0:
                registador1.decrementa()
                registador2.decrementa()
            return registador1

        else:
            if registador1.getValor() > registador2.getValor():
                while registador2.getValor() != 0:
                    registador1.decrementa()
                    registador2.encrementa()
                return registador1
            else:
                while registador2.getValor() != 0:
                    registador1.decrementa()
                    registador2.decrementa()
                return registador1

    def multi(self, registadorA, registadorB):
        sinal = 0
        if registadorA._valor[0] != registadorB._valor[0]:
            sinal = 1

        registadorA._valor[0] = 0
        registadorB._valor[0] = 0

        registadorC = Registador("Reg_AuxiliarC")
        registadorD = Registador("Reg_AuxiliarD")


        print("multiplicando {}[{}] ao {}[{}]:"
              .format(registadorA.getName(),
                      registadorA.getValor(),
                      registadorB.getName(),
                      registadorB.getValor()))

        while(registadorA.getValor() != 0):
            registadorC.encrementa()
            registadorA.decrementa()

        while(registadorC.getValor() != 0):
            self.adicaoC(registadorA, registadorB, registadorD)
            registadorC.decrementa()

        registadorA._valor[0] = sinal
        return registadorA

