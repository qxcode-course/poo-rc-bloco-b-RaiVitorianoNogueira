class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def get_carga(self) -> int:
        return self.__carga

    def get_capacidade(self) -> int:
        return self.__capacidade

    def carregar(self, valor: int):
        self.__carga = min(self.__carga + valor, self.__capacidade)

    def descarregar(self, valor: int) -> int:
        carga_usada = min(valor, self.__carga)
        self.__carga -= carga_usada
        return carga_usada

    def __str__(self):
        return f"Bateria {self.__carga}/{self.__capacidade}"


class Carregador:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def get_potencia(self) -> int:
        return self.__potencia

    def __str__(self):
        return f"Carregador {self.__potencia}W"


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None
        self.__tempo_ligado = 0

    def set_bateria(self, capacidade: int):
        self.__bateria = Bateria(capacidade)

    def rm_bateria(self):
        if self.__bateria is None:
            print("fail: Sem bateria")
            return
        print(f"Removido {self.__bateria.get_carga()}/{self.__bateria.get_capacidade()}")
        self.__bateria = None
        if self.__ligado and self.__carregador is None:
            self.__ligado = False
            self.__tempo_ligado = 0

    def set_carregador(self, potencia: int):
        if self.__carregador is not None:
            print("fail: carregador já conectado")
            return
        self.__carregador = Carregador(potencia)

    def rm_carregador(self):
        if self.__carregador is None:
            print("fail: Sem carregador")
            return
        print(f"Removido {self.__carregador.get_potencia()}W")
        self.__carregador = None
        if self.__ligado and (self.__bateria is None or self.__bateria.get_carga() == 0):
            self.__ligado = False
            self.__tempo_ligado = 0

    def turn_on(self):
        if self.__ligado:
            return
        if self.__bateria is None and self.__carregador is None:
            print("fail: não foi possível ligar")
            return
        if self.__bateria is not None and self.__bateria.get_carga() == 0 and self.__carregador is None:
            print("fail: não foi possível ligar")
            return
        self.__ligado = True
        self.__tempo_ligado = 0

    def turn_off(self):
        if self.__ligado:
            self.__ligado = False

    def usar(self, tempo: int):
        if not self.__ligado:
            print("fail: desligado")
            return

        for i in range(tempo):
            if self.__bateria is None and self.__carregador is None:
                print("fail: descarregou")
                self.__ligado = False
                self.__tempo_ligado = 0
                return

            if self.__bateria is not None:
                if self.__carregador is not None:
                    self.__bateria.carregar(self.__carregador.get_potencia())
                else:
                    if self.__bateria.get_carga() == 0:
                        print("fail: descarregou")
                        self.__ligado = False
                        self.__tempo_ligado = 0
                        return
                    self.__bateria.descarregar(1)

        if self.__ligado:
            self.__tempo_ligado += tempo

    def show(self):
        status = "ligado" if self.__ligado else "desligado"
        info = f"Notebook: {status}"
        if self.__ligado:
            info += f" por {self.__tempo_ligado} min"
        if self.__carregador is not None:
            info += f", {self.__carregador}"
        if self.__bateria is not None:
            info += f", {self.__bateria}"
        print(info)


def main():
    nb = Notebook()
    while True:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            continue
        print("$" + line)
        args = line.split()
        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "show":
            nb.show()
        elif cmd == "set_battery":
            nb.set_bateria(int(args[1]))
        elif cmd == "rm_battery":
            nb.rm_bateria()
        elif cmd == "set_charger":
            nb.set_carregador(int(args[1]))
        elif cmd == "rm_charger":
            nb.rm_carregador()
        elif cmd == "turn_on":
            nb.turn_on()
        elif cmd == "turn_off":
            nb.turn_off()
        elif cmd == "use":
            nb.usar(int(args[1]))
        else:
            print("fail: comando invalido")


main()
