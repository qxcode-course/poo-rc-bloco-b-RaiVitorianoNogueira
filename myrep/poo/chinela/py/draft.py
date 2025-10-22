class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        if valor < 20 or valor > 50:
            print("fail: tamanho fora do intervalo (20 a 50)")
            return
        if valor % 2 != 0:
            print("fail: tamanho deve ser par")
            return
        self.__tamanho = valor
        print(f"chinela tamanho {valor} comprada com sucesso!")


def main():
    chinela = Chinela()

    while chinela.getTamanho() == 0:
        print("Digite seu tamanho de chinela:")
        try:
            tamanho = int(input())
            chinela.setTamanho(tamanho)
        except:
            print("fail: valor inválido, digite um número inteiro")

    print("Parabéns, você comprou uma chinela tamanho", chinela.getTamanho())


main()
