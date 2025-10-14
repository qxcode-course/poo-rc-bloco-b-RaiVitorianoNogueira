Class Bateria:
    def __init__(self, capacidade:int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getCapacidade(self):int:
        return self.__capacidade

    def getCarga(self):int:
        return self.__carga


    def descarregar(self, tempo: int):int:
        if self.__carga <= 0:
            returm 0

        if tempo > self.__carga:
            tempo_usado = self.__carga
            self.__carga = 0
            return tempo_usado


    
        else:
            self.__carga -= tempo
            return tempo

    def carregar(self, tempo:int):
        self.__carga = min(self.__carga = tempo, self.__capacidade)



    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")































def main()
















main()