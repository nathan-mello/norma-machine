from .registador import Registador


class NormaMachine:
    def __init__(self):
        self.contador = 1
        self.conteudo = []

    def inicializarRegistadores(self, valor):
        reg = Registador("Reg_{}".format(self.contador))
        self.contador += 1

        self.conteudo.append("Inicializando {} com o valor {}:".format(reg.getName(), valor))
        if valor < 0:
            for i in range(valor * -1):
                reg.decrementa()
                self.conteudo.append(reg.toString())
        else:
            for i in range(valor):
                reg.encrementa()
                self.conteudo.append(reg.toString())
        return reg

    ##  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def adicao(self, registador1, registador2):

        self.conteudo.append("adicionando {}[{}] ao {}[{}]:"
                             .format(registador1.getName(),
                                     registador1.getValor(),
                                     registador2.getName(),
                                     registador2.getValor()))

        if registador1.ePositivo() and registador2.ePositivo():
            while registador2.getValor() != 0:
                registador1.encrementa()
                self.conteudo.append(registador1.toString())
                registador2.decrementa()
                self.conteudo.append(registador2.toString())
            return registador1

        elif not registador1.ePositivo() and not registador2.ePositivo():
            while registador2.getValor() != 0:
                registador1.decrementa()
                self.conteudo.append(registador1.toString())
                registador2.encrementa()
                self.conteudo.append(registador2.toString())
            return registador1

        else:
            if registador1.getValorAbsoluto() < registador2.getValorAbsoluto() and registador1.ePositivo():
                while registador1.getValor() != 0:
                    registador2.encrementa()
                    self.conteudo.append(registador2.toString())
                    registador1.decrementa()
                    self.conteudo.append(registador1.toString())
                return registador2
            elif registador1.getValorAbsoluto() < registador2.getValorAbsoluto() and not registador1.ePositivo():
                while registador1.getValor() != 0:
                    registador2.decrementa()
                    self.conteudo.append(registador2.toString())
                    registador1.encrementa()
                    self.conteudo.append(registador1.toString())
                return registador2
            elif registador1.getValorAbsoluto() > registador2.getValorAbsoluto() and registador1.ePositivo():
                while registador2.getValor() != 0:
                    registador2.encrementa()
                    self.conteudo.append(registador2.toString())
                    registador1.decrementa()
                    self.conteudo.append(registador1.toString())
                return registador1
            elif registador1.getValorAbsoluto() > registador2.getValorAbsoluto() and not registador1.ePositivo():
                while registador2.getValor() != 0:
                    registador2.decrementa()
                    self.conteudo.append(registador2.toString())
                    registador1.encrementa()
                    self.conteudo.append(registador1.toString())
                return registador1
            else:
                if registador1.ePositivo():
                    while registador1.getValor() != 0:
                        registador1.decrementa()
                        self.conteudo.append(registador1.toString())
                        registador2.encrementa()
                        self.conteudo.append(registador2.toString())
                    return registador1
                else:
                    while registador1.getValor() != 0:
                        registador1.encrementa()
                        self.conteudo.append(registador1.toString())
                        registador2.decrementa()
                        self.conteudo.append(registador2.toString())
                    return registador1

    def adicaoC(self, registadorA, registadorB, registadorC):

        while registadorB.getValor() != 0:
            registadorA.encrementa()
            self.conteudo.append(registadorA.toString())
            registadorC.encrementa()
            self.conteudo.append(registadorC.toString())
            registadorB.decrementa()
            self.conteudo.append(registadorB.toString())

        while registadorC.getValor() != 0:
            registadorB.encrementa()
            self.conteudo.append(registadorB.toString())
            registadorC.decrementa()
            self.conteudo.append(registadorC.toString())

    def sub(self, registador1, registador2):
        print("subtraindo {}[{}] ao {}[{}]:"
              .format(registador1.getName(),
                      registador1.getValor(),
                      registador2.getName(),
                      registador2.getValor()))

        if not registador1.ePositivo() and not registador2.ePositivo():
            while registador2.getValor() != 0:
                registador1.decrementa()
                self.conteudo.append(registador1.toString())
                registador2.encrementa()
                self.conteudo.append(registador2.toString())
            return registador1

        elif registador1.ePositivo() and registador2.ePositivo():
            while registador2.getValor() != 0:
                registador1.decrementa()
                self.conteudo.append(registador1.toString())
                registador2.decrementa()
                self.conteudo.append(registador2.toString())
            return registador1

        else:
            if registador1.getValor() > registador2.getValor():
                while registador2.getValor() != 0:
                    registador1.decrementa()
                    self.conteudo.append(registador1.toString())
                    registador2.encrementa()
                    self.conteudo.append(registador2.toString())
                return registador1
            else:
                while registador2.getValor() != 0:
                    registador1.decrementa()
                    self.conteudo.append(registador1.toString())
                    registador2.decrementa()
                    self.conteudo.append(registador2.toString())
                return registador1

    def multi(self, registadorA, registadorB):
        sinal = 0
        if registadorA._valor[0] != registadorB._valor[0]:
            sinal = 1

        registadorA._valor[0] = 0
        registadorB._valor[0] = 0

        registadorC = Registador("Reg_AuxiliarC")
        registadorD = Registador("Reg_AuxiliarD")

        self.conteudo.append("multiplicando {}[{}] ao {}[{}]:"
              .format(registadorA.getName(),
                      registadorA.getValor(),
                      registadorB.getName(),
                      registadorB.getValor()))

        while (registadorA.getValor() != 0):
            registadorC.encrementa()
            self.conteudo.append(registadorC.toString())
            registadorA.decrementa()
            self.conteudo.append(registadorA.toString())

        while (registadorC.getValor() != 0):
            self.adicaoC(registadorA, registadorB, registadorD)
            registadorC.decrementa()
            self.conteudo.append(registadorC.toString())

        registadorA._valor[0] = sinal
        return registadorA
