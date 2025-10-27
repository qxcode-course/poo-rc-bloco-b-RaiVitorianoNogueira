class Pessoa:
    def __init__(self, nome, dinheiro):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self):
        return self.__nome

    def getDinheiro(self):
        return self.__dinheiro

    def pagar(self, valor):
        if self.__dinheiro >= valor:
            self.__dinheiro -= valor
            return valor
        else:
            restante = self.__dinheiro
            self.__dinheiro = 0
            return restante

    def receber(self, valor):
        self.__dinheiro += valor


class Moto:
    def __init__(self):
        self.__custo = 0
        self.__motorista = None
        self.__passageiro = None

    def setDriver(self, nome, dinheiro):
        self.__motorista = Pessoa(nome, dinheiro)

    def setPass(self, nome, dinheiro):
        if self.__motorista is None:
            print("fail: no driver in the moto")
            return
        self.__passageiro = Pessoa(nome, dinheiro)

    def drive(self, km):
        if self.__passageiro is None:
            print("fail: no passenger in the moto")
            return
        self.__custo += km

    def leavePass(self):
        if self.__passageiro is None:
            print("fail: no passenger to leave")
            return
        pago = self.__passageiro.pagar(self.__custo)
        falta = self.__custo - pago
        if self.__motorista:
            self.__motorista.receber(self.__custo - pago)  # motorista recebe o que falta
        print(f"{self.__passageiro.getNome()}:{pago} left")
        self.__custo = 0
        self.__passageiro = None

    def show(self):
        driver = (
            f"{self.__motorista.getNome()}:{self.__motorista.getDinheiro()}"
            if self.__motorista
            else "None"
        )
        passenger = (
            f"{self.__passageiro.getNome()}:{self.__passageiro.getDinheiro()}"
            if self.__passageiro
            else "None"
        )
        print(f"Cost: {self.__custo}, Driver: {driver}, Passenger: {passenger}")


def main():
    moto = Moto()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            moto.show()
        elif args[0] == "setDriver":
            if len(args) < 3:
                print("fail: parâmetros insuficientes")
                continue
            nome = args[1]
            dinheiro = int(args[2])
            moto.setDriver(nome, dinheiro)
        elif args[0] == "setPass":
            if len(args) < 3:
                print("fail: parâmetros insuficientes")
                continue
            nome = args[1]
            dinheiro = int(args[2])
            moto.setPass(nome, dinheiro)
        elif args[0] == "drive":
            if len(args) < 2:
                print("fail: parâmetro km ausente")
                continue
            km = int(args[1])
            moto.drive(km)
        elif args[0] == "leavePass":
            moto.leavePass()
        else:
            print("fail: comando invalido")


main()
