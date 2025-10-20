class Chinela:
    def __init__(self):
        self.__size = 0



    def getSize(self):
        return self.__size 

    def setSize(self, valor):
        if valor < 20 or valor > 50:
            print("fail: tamanho fora do intervalo (20 a 50)")
            return 
        if valor % 2 != 0:
            print("fail: tamanho deve ser par")
            return
        self.__size =  valor

        print(f"chinela tamanho {valor} comprada com sucesso!")




def main():
    chinela: Chinela = Chinela()

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")


        if args[0] == "end":
            break

        elif args[0] == "init":
            chinela = Chinela()

        elif partes[0] == "set":
            if len(partes) < 2:
                print("fail: informe o tamanho depois de 'set'")
                continue
            try:
                valor = int(partes[1])
                chinela.setSize(valor)
            except:
                print("fail: valor inválido")

        elif args[0] == "show":
            print("chinela:", chinela.getSize())

        else:
            print("fail: comando não encontrado")



main()

