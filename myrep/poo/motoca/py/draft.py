class Pessoa:
    def _init_(self, nome: str, age: int):
        self.__nome = nome
        self.__age = age

    def _str_(self):
        return f"{self._nome}:{self._age}"
        
    def getAge(self):
        return self.__age

    def getName(self):
        return self.__nome

    def toString(self) -> str:
        return f"{self._nome}:{self._age}"


class Moto:
    def _init_(self, potencia: int = 1):
        self.__potencia = potencia
        self.__tempo: int = 0
        self.__pessoa: Pessoa = None #pode ser uma pessoa ou pode ser nulo

    def add_pessoa(self, pessoa: Pessoa) -> bool:
        if self.__pessoa != None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True

    def remover(self) -> Pessoa | None:        #tiro a pessoa da moto
        aux = self.__pessoa
        self.__pessoa = None       #Se for = a nada, então retirou
        return aux          #retorna o auxiliar, que não tem ninguem

    def comprar_tempo(self, tempo: int):
        self.__tempo += tempo

    def dirigir(self, tempo: int):
        if self.__tempo == 0:
            print("fail: buy time first")
            return 

        elif self.__pessoa == None:
            print("fail: empty motorcycle")

        elif self.__tempo == 0:
            print("fail: buy time first")
            return 

        elif self.__pessoa.getAge() > 10:
            print("fail: too old to drive")

        elif self.__tempo < tempo:
            print(f"fail: time finished after {self.__tempo} minutes")
            self.__tempo = 0

        elif self.__tempo >= tempo:
             self.__tempo -= tempo

    def buzinar(self) -> str:            # retorna o som da buzina da moto
        som: str = "P"                   #de acordo com a potencia, vou adicionando um 'e' na variavel som
        for i in range(self.__potencia): #é assim que se faz o "for"
            som += "e"
        som += "m"
        return som

    def _str_(self):
        pessoa = "empty" if self._pessoa is None else str(self._pessoa)
        return f"power:{self._potencia}, time:{self._tempo}, person:({pessoa})"
 

def main():
    moto = Moto()

    while True:
        #entrada do usuario
        line = input()
        #printar oque o usuario escreveu acima com um cifrao na frente
        print("$" + line)
        #divide a variavel line em uma lista separada por espaço
        args = line.split(" ")

        if args[0] == "end":
            break     

        elif args[0] == "show":
            print(moto)

        elif args[0] == "init":
            pot = int(args[1])
            moto = Moto(pot)

        elif args[0] == "enter":
            nome = args[1] # tem as variaveis
            idade = int(args[2]) #tem as pessoa
            pessoa = Pessoa(nome, idade) #manda as pessoas entrarem na moto
            moto.add_pessoa(pessoa)

        elif args[0] == "leave":
            pessoa = moto.remover()
            if pessoa == None:
                print("fail: empty motorcycle")
            else:
                print(f"{pessoa.toString()}")
        
        elif args[0] == "buy":
            minuto = int(args[1])
            moto.comprar_tempo(minuto)

        elif args[0] == "drive":
            tempo = int(args[1])
            moto.dirigir(tempo)

        elif args[0] == "honk":
            print(moto.buzinar())

main()