import json

class trabajador:
    def __init__(self, nombre, carnet, salario):
        self.nombre = nombre
        self.carnet = carnet
        self.salario = salario

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "carnet": self.carnet,
            "salario": self.salario
        }

    @staticmethod
    def from_dict(data):
        return trabajador(data["nombre"], data["carnet"], data["salario"])

    def __str__(self):
        return f"{self.nombre} - ci:{self.carnet} - Bs. {self.salario:.2f}"


class archivostrabajo:
    def __init__(self, archivo="trabajadores.json"):
        self.archivo = archivo
        self.lista = []

    def crearchivo(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump([], f)
            print("archivo creado")
            return True
        except:
            print("no se pudo crear")
            return False

    def cargadatos(self):
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.lista = [trabajador.from_dict(d) for d in datos]
            print(f"se cargaron {len(self.lista)} trabajadores")
        except:
            print("no hay archivo o error")
            self.lista = []

    def guardartrab(self, t):
        self.lista.append(t)
        self.guardartodo()
        print("guardado")

    def guardartodo(self):
        try:
            with open(self.archivo, "w") as f:
                datos = [tr.to_dict() for tr in self.lista]
                json.dump(datos, f, indent=4)
        except:
            print("error al guardar")

    def aumentasal(self, porc, t):
        for trab in self.lista:
            if trab.carnet == t.carnet:
                aumento = trab.salario * (porc / 100)
                trab.salario += aumento
                self.guardartodo()
                print(f"aumento del {porc}% aplicado")
                print(f"nuevo salario: Bs. {trab.salario:.2f}")
                return True
        print("no se encontro")
        return False

    def mayorsalario(self):
        if not self.lista:
            return None
        mayor = self.lista[0]
        for t in self.lista:
            if t.salario > mayor.salario:
                mayor = t
        return mayor

    def ordenasalario(self):
        self.lista.sort(key=lambda x: x.salario)
        self.guardartodo()
        return self.lista

    def verlista(self):
        if not self.lista:
            print("lista vacia")
        for i, t in enumerate(self.lista, 1):
            print(f"{i}. {t}")


def main():
    arch = archivostrabajo()
    arch.cargadatos()

    while True:
        print("\n-- menu trabajadores --")
        print("1* nuevo archivo")
        print("2* agregar trabajador")
        print("3* ver lista")
        print("4* aumentar salario")
        print("5* ver mayor salario")
        print("6* ordenar por salario")
        print("7* salir")

        op = input("elige opcion: ")

        if op == "1":
            arch.crearchivo()

        elif op == "2":
            nom = input("nombre: ")
            try:
                ci = int(input("carnet: "))
                sal = float(input("salario en Bs: "))
            except:
                print("dato invalido")
                continue

            nuevo = trabajador(nom, ci, sal)
            arch.guardartrab(nuevo)

        elif op == "3":
            arch.verlista()

        elif op == "4":
            try:
                buscaci = int(input("carnet del trabajador: "))
                porc = float(input("porcentaje de aumento: "))
            except:
                print("numero invalido")
                continue

            encontrado = None
            for t in arch.lista:
                if t.carnet == buscaci:
                    encontrado = t
                    break

            if encontrado:
                arch.aumentasal(porc, encontrado)
            else:
                print("no existe ese carnet")

        elif op == "5":
            mayor = arch.mayorsalario()
            if mayor:
                print("trabajador con mayor salario:")
                print(mayor)
            else:
                print("no hay trabajadores")

        elif op == "6":
            arch.ordenasalario()
            print("lista ordenada por salario:")
            arch.verlista()

        elif op == "7":
            print("chauuuuu.....")
            break

        else:
            print("opcion invalida mmm")


if __name__ == "__main__":
    main()