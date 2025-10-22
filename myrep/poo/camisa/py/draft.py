class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:

        return self.__tamanho

    def setTamanho(self, valor: str):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor in tamanhos_validos:
            self.__tamanho = valor
        else:
            print("fail: tamanho inválido! Valores permitidos:", ", ".join(tamanhos_validos))








def main()

    camisa = Camisa()

    while camisa.getTamanho() == "":
        print("Digite o tamanho da camisa (PP, P , M, , G, GG, XG):")
        tamanho = input().strip().upper()
        camisa.setTamanho(tamanho)

    print("Parabéns, você comprou uma camisa tamanho", camisa.getTamanho()))





main()
