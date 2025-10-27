class Roupa:
    def __init__(self):
        self.__tamanho = ""

    def setTamanho(self, valor):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor not in tamanhos_validos:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            return
        self.__tamanho = valor

    def show(self):
        return f"size: ({self.__tamanho})"


def main():
    roupa = Roupa()
    while True:
        comando = input()
        if not comando:
            continue
        print("$" + comando)
        partes = comando.split()
        op = partes[0]

        if op == "end":
            break
        elif op == "init":
            roupa = Roupa()
        elif op == "size":
            if len(partes) < 2:
                print("fail: informe o tamanho após 'size'")
                continue
            roupa.setTamanho(partes[1])
        elif op == "show":
            print(roupa.show())
        else:
            print("fail: comando inválido")


main()
