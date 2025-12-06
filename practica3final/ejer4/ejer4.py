import json

class estudiante:
    def __init__(self, ru, nombre, paterno, materno, edad):
        self.ru = ru
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad

    def to_dict(self):
        return {
            "ru": self.ru,
            "nombre": self.nombre,
            "paterno": self.paterno,
            "materno": self.materno,
            "edad": self.edad
        }

    @staticmethod
    def from_dict(data):
        return estudiante(data["ru"], data["nombre"], data["paterno"], data["materno"], data["edad"])

    def __str__(self):
        return f"{self.ru} - {self.nombre} {self.paterno} {self.materno} - {self.edad} años"


class nota:
    def __init__(self, materia, notafinal, est):
        self.materia = materia
        self.notafinal = notafinal
        self.estudiante = est

    def to_dict(self):
        return {
            "materia": self.materia,
            "notafinal": self.notafinal,
            "estudiante": self.estudiante.to_dict()
        }

    @staticmethod
    def from_dict(data):
        est = estudiante.from_dict(data["estudiante"])
        return nota(data["materia"], data["notafinal"], est)

    def __str__(self):
        return f"{self.estudiante.nombre} - {self.materia}: {self.notafinal}"


class archnota:
    def __init__(self, nombrearchi="notas.json"):
        self.nombrearchi = nombrearchi
        self.notas = []

    def crearchivo(self):
        try:
            with open(self.nombrearchi, "w") as f:
                json.dump([], f)
            print("listo")
        except:
            print("fallo")

    def cargardatos(self):
        try:
            with open(self.nombrearchi, "r") as f:
                datos = json.load(f)
                self.notas = [nota.from_dict(d) for d in datos]
            print(f"hay {len(self.notas)} notas")
        except:
            print("no hay archivo")
            self.notas = []

    def guardartodo(self):
        try:
            with open(self.nombrearchi, "w") as f:
                datos = [n.to_dict() for n in self.notas]
                json.dump(datos, f, indent=2)
        except:
            print("error guardando")

    # b) agregar varios estudiantes
    def agregarvarios(self):
        print("agregar estudiantes")
        while True:
            try:
                ru = int(input("ru (0 para terminar): "))
                if ru == 0:
                    break
                nom = input("nombre: ")
                pat = input("paterno: ")
                mat = input("materno: ")
                edad = int(input("edad: "))
                materia = input("materia: ")
                notaf = float(input("nota final: "))
            except:
                print("dato mal")
                continue

            est = estudiante(ru, nom, pat, mat, edad)
            n = nota(materia, notaf, est)
            self.notas.append(n)
            print("agregado")
        self.guardartodo()

    # c) promedio de notas
    def promedionotas(self):
        if not self.notas:
            return 0
        total = sum(n.notafinal for n in self.notas)
        return total / len(self.notas)

    # d) mejores notas
    def mejoresnotas(self):
        if not self.notas:
            return []
        
        maxnota = max(n.notafinal for n in self.notas)
        mejores = [n for n in self.notas if n.notafinal == maxnota]
        return mejores

    # e) eliminar por materia
    def eliminarmateria(self, materia):
        original = len(self.notas)
        self.notas = [n for n in self.notas if n.materia.lower() != materia.lower()]
        eliminados = original - len(self.notas)
        if eliminados > 0:
            self.guardartodo()
            print(f"eliminados {eliminados} de {materia}")
        else:
            print(f"no hay en {materia}")

    def vernotas(self):
        if not self.notas:
            print("nada")
        for i, n in enumerate(self.notas, 1):
            print(f"{i}. {n}")


def main():
    arch = archnota()
    arch.cargardatos()

    while True:
        print("\n-- menu notas --")
        print("1. agregar varios")
        print("2. ver todas")
        print("3. promedio notas")
        print("4. mejores notas")
        print("5. eliminar por materia")
        print("6. salir")

        op = input("que: ")

        if op == "1":
            arch.agregarvarios()

        elif op == "2":
            arch.vernotas()

        elif op == "3":
            prom = arch.promedionotas()
            print(f"promedio general: {prom:.2f}")

        elif op == "4":
            mejores = arch.mejoresnotas()
            if mejores:
                print("mejores notas:")
                for m in mejores:
                    print(m)
            else:
                print("no hay")

        elif op == "5":
            mat = input("materia a eliminar: ")
            arch.eliminarmateria(mat)

        elif op == "6":
            print("adios")
            break

        else:
            print("esa no")


if __name__ == "__main__":
    main()