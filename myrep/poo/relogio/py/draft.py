class Watch:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)

    def getHora(self):
        return self.__hora

    def getMinuto(self):
        return self.__minuto

    def getSegundo(self):
        return self.__segundo

    def setHora(self, valor):
        if 0 <= valor <= 23:
            self.__hora = valor
        else:
            print("fail: hora invalida")

    def setMinuto(self, valor):
        if 0 <= valor <= 59:
            self.__minuto = valor
        else:
            print("fail: minuto invalido")

    def setSegundo(self, valor):
        if 0 <= valor <= 59:
            self.__segundo = valor
        else:
            print("fail: segundo invalido")

    def toString(self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"
 #esse metodo vai retornar o horário, garantindo sempre dois digítos em cada parte
    def set(self, h, m, s):
        self.setHora(h)
        self.setMinuto(m)
        self.setSegundo(s)

    def next(self):
        self.__segundo += 1
        if self.__segundo == 60:
            self.__segundo = 0
            self.__minuto += 1
            if self.__minuto == 60:
                self.__minuto = 0
                self.__hora += 1
                if self.__hora == 24:
                    self.__hora = 0

    def show(self):
        print(self.toString())


def main():
    relogio = Watch()
    while True:
        cmd = input()
        if not cmd:
            continue
        print("$" + cmd)
        parts = cmd.split()
        op = parts[0]

        if op == "end":
            break
        elif op == "init":
            relogio = Watch(int(parts[1]), int(parts[2]), int(parts[3]))
        elif op == "set":
            relogio.set(int(parts[1]), int(parts[2]), int(parts[3]))
        elif op == "show":
            print(relogio.toString())
        elif op == "next":
            relogio.next()
        else:
            print("fail: comando invalido")


main()
