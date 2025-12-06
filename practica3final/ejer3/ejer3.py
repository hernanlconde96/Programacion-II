import json

class producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return producto(data["codigo"], data["nombre"], data["precio"])

    def __str__(self):
        return f"cod:{self.codigo} - {self.nombre} - Bs. {self.precio:.2f}"


class archivoproducto:
    def __init__(self, nomA="productos.json"):
        self.nomA = nomA
        self.productos = []

    def creararchivo(self):
        try:
            with open(self.nomA, "w") as f:
                json.dump([], f)
            print("archivo creado")
            return True
        except:
            print("error")
            return False

    def cargarproductos(self):
        try:
            with open(self.nomA, "r") as f:
                datos = json.load(f)
                self.productos = [producto.from_dict(d) for d in datos]
            print(f"cargados {len(self.productos)} productos")
        except:
            print("no hay archivo")
            self.productos = []

    def guardaproducto(self, p):
        self.productos.append(p)
        self.guardartodo()
        print("producto guardado")

    def guardartodo(self):
        try:
            with open(self.nomA, "w") as f:
                datos = [pr.to_dict() for pr in self.productos]
                json.dump(datos, f, indent=2)
        except:
            print("error al guardar")

    def buscaproducto(self, c):
        for prod in self.productos:
            if prod.codigo == c:
                return prod
        return None

    def promedioprecios(self):
        if not self.productos:
            return 0
        total = sum(p.precio for p in self.productos)
        return total / len(self.productos)

    def productomascaro(self):
        if not self.productos:
            return None
        caro = self.productos[0]
        for p in self.productos:
            if p.precio > caro.precio:
                caro = p
        return caro

    def verproductos(self):
        if not self.productos:
            print("no hay productos")
        for i, p in enumerate(self.productos, 1):
            print(f"{i}. {p}")


def main():
    arch = archivoproducto()
    arch.cargarproductos()

    while True:
        print("\n--- menu productos ---")
        print("1. crear archivo")
        print("2. agregar producto")
        print("3. ver todos")
        print("4. buscar por codigo")
        print("5. promedio de precios")
        print("6. producto mas caro")
        print("7. salir")

        op = input("opcion: ")

        if op == "1":
            arch.creararchivo()

        elif op == "2":
            try:
                cod = int(input("codigo: "))
                nom = input("nombre: ")
                prec = float(input("precio: "))
            except:
                print("datos invalidos")
                continue

            nuevo = producto(cod, nom, prec)
            arch.guardaproducto(nuevo)

        elif op == "3":
            arch.verproductos()

        elif op == "4":
            try:
                buscacod = int(input("codigo a buscar: "))
            except:
                print("codigo invalido")
                continue

            encontrado = arch.buscaproducto(buscacod)
            if encontrado:
                print("producto encontrado:")
                print(encontrado)
            else:
                print("no existe ese codigo")

        elif op == "5":
            prom = arch.promedioprecios()
            print(f"promedio de precios: Bs. {prom:.2f}")

        elif op == "6":
            caro = arch.productomascaro()
            if caro:
                print("producto mas caro:")
                print(caro)
            else:
                print("no hay productos")

        elif op == "7":
            print("chao")
            break

        else:
            print("opcion no valida")


if __name__ == "__main__":
    main()