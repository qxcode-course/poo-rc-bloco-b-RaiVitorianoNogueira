class Pessoa:
    def __init__(self, nome: str, age: int):
        self.__nome = nome
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__nome

    def __str__(self):
        return f"{self.__nome}:{self.__age}"

    def toString(self) -> str:
        return str(self)


class Moto:
    def __init__(self, potencia: int = 1):
        self.__potencia = potencia
        self.__tempo = 0
        self.__pessoa = None  # Pode ser uma Pessoa ou None

    # Adicionar pessoa
    def add_pessoa(self, pessoa: Pessoa) -> bool:
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True

    # Remover pessoa
    def remover(self) -> Pessoa | None:
        if self.__pessoa is None:
            return None
        aux = self.__pessoa
        self.__pessoa = None
        return aux

    # Comprar tempo
    def comprar_tempo(self, tempo: int):
        self.__tempo += tempo

    # Dirigir
    def dirigir(self, tempo: int):
        if self.__tempo == 0:
            print("fail: buy time first")
        elif self.__pessoa is None:
            print("fail: empty motorcycle")
        elif self.__pessoa.getAge() > 10:
            print("fail: too old to drive")
        elif self.__tempo < tempo:
            print(f"fail: time finished after {self.__tempo} minutes")
            self.__tempo = 0
        else:
            self.__tempo -= tempo

    # Buzinar
    def buzinar(self) -> str:
        return "P" + "e" * self.__potencia + "m"

    # Mostrar estado
    def __str__(self):
        pessoa = "empty" if self.__pessoa is None else str(self.__pessoa)
        return f"power:{self.__potencia}, time:{self.__tempo}, person:({pessoa})"


def main():
    moto = Moto()

    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "":
            continue

        # Print do comando
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(moto)

        elif args[0] == "init":
            pot = int(args[1])
            moto = Moto(pot)

        elif args[0] == "enter":
            nome = args[1]
            idade = int(args[2])
            pessoa = Pessoa(nome, idade)
            moto.add_pessoa(pessoa)

        elif args[0] == "leave":
            pessoa = moto.remover()
            if pessoa is None:
                print("fail: empty motorcycle")
            else:
                print(pessoa.toString())

        elif args[0] == "buy":
            tempo = int(args[1])
            moto.comprar_tempo(tempo)

        elif args[0] == "drive":
            tempo = int(args[1])
            moto.dirigir(tempo)

        elif args[0] == "honk":
            print(moto.buzinar())


main()
