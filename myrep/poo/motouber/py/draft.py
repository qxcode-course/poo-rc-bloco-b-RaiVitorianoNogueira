class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self) -> str:
        return self.__nome


    def getDinheiro(self) -> int:
        return self.__dinheiro

    def pagar(self, valor: int) -> int:
        """Retorna quanto a pessoa conseguiu pagar e reduz seu dinheiro."""
        if self.__dinheiro >= valor:
            self.__dinheiro -= valor
            return valor
        restante = self.__dinheiro
        self.__dinheiro = 0
        return restante

    def receber(self, valor: int):
        """Recebe dinheiro (incrementa o saldo)."""
        self.__dinheiro += valor


class Moto:
    def __init__(self):
        self.__custo = 0
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def setDriver(self, nome: str, dinheiro: int):
        self.__motorista = Pessoa(nome, dinheiro)

    def setPass(self, nome: str, dinheiro: int):
        if self.__motorista is None:
            print("fail: no driver in the moto")
            return
        self.__passageiro = Pessoa(nome, dinheiro)

    def drive(self, km: int):
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
        if falta > 0:
            print("fail: Passenger does not have enough money")
        if self.__motorista is not None:
            self.__motorista.receber(pago + falta)  # motorista recebe tudo
        print(f"{self.__passageiro.getNome()}:{self.__passageiro.getDinheiro()} left")
        self.__custo = 0
        self.__passageiro = None

    def show(self):
        driver = f"{self.__motorista.getNome()}:{self.__motorista.getDinheiro()}" if self.__motorista else "None"
        passenger = f"{self.__passageiro.getNome()}:{self.__passageiro.getDinheiro()}" if self.__passageiro else "None"
        print(f"Cost: {self.__custo}, Driver: {driver}, Passenger: {passenger}")


def main():
    moto = Moto()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if not args:
            continue

        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "show":
            moto.show()
        elif cmd == "setDriver":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setDriver(nome, dinheiro)
        elif cmd == "setPass":
            nome = args[1]
            dinheiro = int(args[2])
            moto.setPass(nome, dinheiro)
        elif cmd == "drive":
            km = int(args[1])
            moto.drive(km)
        elif cmd == "leavePass":
            moto.leavePass()
        else:
            print("fail: comando invalido")


main()
