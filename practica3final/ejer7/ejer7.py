import json

class persona:
    def __init__(self, nombre, paterno, materno, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.ci = ci

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "paterno": self.paterno,
            "materno": self.materno,
            "ci": self.ci
        }

    @staticmethod
    def from_dict(data):
        return persona(data["nombre"], data["paterno"], data["materno"], data["ci"])

    def __str__(self):
        return f"{self.nombre} {self.paterno} {self.materno} - CI: {self.ci}"


class nino(persona):
    def __init__(self, nombre, paterno, materno, ci, edad, peso, talla):
        super().__init__(nombre, paterno, materno, ci)
        self.edad = edad
        self.peso = peso
        self.talla = talla

    def to_dict(self):
        datos = super().to_dict()
        datos.update({
            "edad": self.edad,
            "peso": self.peso,
            "talla": self.talla
        })
        return datos

    @staticmethod
    def from_dict(data):
        return nino(
            data["nombre"], data["paterno"], data["materno"],
            data["ci"], data["edad"], data["peso"], data["talla"]
        )

    def __str__(self):
        base = super().__str__()
        return f"{base} - {self.edad}años - {self.peso}kg - {self.talla}cm"

    def peso_adecuado(self):
        if self.edad < 5:
            return self.peso >= 12 and self.peso <= 20
        elif self.edad < 10:
            return self.peso >= 20 and self.peso <= 35
        else:
            return self.peso >= 35 and self.peso <= 50

    def talla_adecuada(self):
        if self.edad < 5:
            return self.talla >= 90 and self.talla <= 110
        elif self.edad < 10:
            return self.talla >= 110 and self.talla <= 140
        else:
            return self.talla >= 140 and self.talla <= 160


class archnino:
    def __init__(self, archivo="ninos.json"):
        self.archivo = archivo
        self.ninos = []

    def crear(self):
        try:
            with open(self.archivo, "w") as f:
                json.dump([], f)
            print("archivo creado")
        except:
            print("error")

    def leer(self):
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.ninos = [nino.from_dict(d) for d in datos]
            print(f"cargados {len(self.ninos)} ninos")
        except:
            self.ninos = []

    def guardar(self):
        try:
            with open(self.archivo, "w") as f:
                datos = [n.to_dict() for n in self.ninos]
                json.dump(datos, f)
        except:
            print("error guardando")

    def agregar(self):
        print("nuevo nino")
        nom = input("nombre: ")
        pat = input("paterno: ")
        mat = input("materno: ")
        try:
            ci = int(input("ci: "))
            edad = int(input("edad: "))
            peso = float(input("peso kg: "))
            talla = float(input("talla cm: "))
        except:
            print("datos mal")
            return
        
        nuevo = nino(nom, pat, mat, ci, edad, peso, talla)
        self.ninos.append(nuevo)
        self.guardar()
        print("agregado")

    def listar(self):
        if not self.ninos:
            print("no hay ninos")
            return
        for i, n in enumerate(self.ninos, 1):
            print(f"{i}. {n}")

    def mostrar(self, idx):
        if 0 <= idx < len(self.ninos):
            print(self.ninos[idx])
        else:
            print("indice invalido")

    def contar_peso_adecuado(self):
        cont = 0
        for n in self.ninos:
            if n.peso_adecuado():
                cont += 1
        return cont

    def ninos_inadecuados(self):
        res = []
        for n in self.ninos:
            if not n.peso_adecuado() or not n.talla_adecuada():
                res.append(n)
        return res

    def promedio_edad(self):
        if not self.ninos:
            return 0
        total = sum(n.edad for n in self.ninos)
        return total / len(self.ninos)

    def buscar_ci(self, ci):
        for n in self.ninos:
            if n.ci == ci:
                return n
        return None

    def ninos_talla_alta(self):
        if not self.ninos:
            return []
        max_talla = max(n.talla for n in self.ninos)
        return [n for n in self.ninos if n.talla == max_talla]


def main():
    arch = archnino()
    arch.leer()

    while True:
        print("\n**** menu ninios ****")
        print("1- crear archivo")
        print("2- agregar nino")
        print("3- listar todos")
        print("4- mostrar uno")
        print("5-. contar peso adecuado")
        print("6- ninos inadecuados")
        print("7- promedio edad")
        print("8- buscar por ci")
        print("9- ninos talla alta")
        print("10--- salir----")

        op = input("elige: ")

        if op == "1":
            arch.crear()

        elif op == "2":
            arch.agregar()

        elif op == "3":
            arch.listar()

        elif op == "4":
            try:
                idx = int(input("numero de lista: ")) - 1
                arch.mostrar(idx)
            except:
                print("numero invalido")

        elif op == "5":
            cont = arch.contar_peso_adecuado()
            print(f"{cont} ninos tienen peso adecuado")

        elif op == "6":
            inadecuados = arch.ninos_inadecuados()
            if inadecuados:
                print("ninos con peso y talla inadecuada:")
                for n in inadecuados:
                    print(f"  - {n}")
            else:
                print("todos estan bien")

        elif op == "7":
            prom = arch.promedio_edad()
            print(f"promedio de edad: {prom:.1f} años")

        elif op == "8":
            try:
                ci = int(input("ci a buscar: "))
                encontrado = arch.buscar_ci(ci)
                if encontrado:
                    print("encontrado:")
                    print(encontrado)
                else:
                    print("no esta")
            except:
                print("ci invalido")

        elif op == "9":
            altos = arch.ninos_talla_alta()
            if altos:
                print("ninos con talla mas alta:")
                for n in altos:
                    print(f"  - {n}")
            else:
                print("no hay")

        elif op == "10":
            print("adios")
            break

        else:
            print("esa no")


if __name__ == "__main__":
    main()