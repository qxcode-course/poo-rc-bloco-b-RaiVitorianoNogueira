class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self) -> int:
        """Retorna o desgaste do grafite por folha de acordo com a dureza."""
        desgaste = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6
        }
        return desgaste.get(self.hardness, 1)

    def __str__(self) -> str:
        return f"[{self.thickness}:{self.hardness}:{self.size}]"


class Pencil:
    def __init__(self):
        self.thickness: float = 0.0
        self.tip: Lead | None = None

    def insert(self, lead: Lead):
        if self.tip is not None:
            print("fail: ja existe grafite")
            return
        if abs(lead.thickness - self.thickness) > 1e-6:
            print("fail: calibre incompativel")
            return
        self.tip = lead

    def remove(self):
        if self.tip is None:
            print("fail: nao existe grafite")
            return
        self.tip = None

    def writePage(self):
        if self.tip is None:
            print("fail: nao existe grafite")
            return
        desgaste = self.tip.usagePerSheet()
        if self.tip.size <= 10:
            print("fail: tamanho insuficiente")
            self.tip.size = 10
            return
        if self.tip.size - desgaste < 10:
            self.tip.size = 10
            print("fail: folha incompleta")
            return
        self.tip.size -= desgaste

    def __str__(self):
        grafite_str = str(self.tip) if self.tip else "null"
        return f"calibre: {self.thickness}, grafite: {grafite_str}"


def main():
    pencil = Pencil()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if not args:
            continue

        cmd = args[0]

        if cmd == "end":
            break
        elif cmd == "init":
            pencil.thickness = float(args[1])
        elif cmd == "insert":
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            lead = Lead(thickness, hardness, size)
            pencil.insert(lead)
        elif cmd == "remove":
            pencil.remove()
        elif cmd == "write":
            pencil.writePage()
        elif cmd == "show":
            print(pencil)
        else:
            print("fail: comando invalido")


main()
