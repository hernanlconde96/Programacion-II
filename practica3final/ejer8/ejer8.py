import json
from datetime import datetime

class alimento:
    def __init__(self, nombre, fechavencimiento, cantidad):
        self.nombre = nombre
        self.fechavencimiento = fechavencimiento  # formato: "2024-12-31"
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "fechavencimiento": self.fechavencimiento,
            "cantidad": self.cantidad
        }

    @staticmethod
    def from_dict(data):
        return alimento(data["nombre"], data["fechavencimiento"], data["cantidad"])

    def __str__(self):
        return f"{self.nombre} - vence: {self.fechavencimiento} - cant: {self.cantidad}"

    def esta_vencido(self):
        hoy = datetime.now().strftime("%Y-%m-%d")
        return self.fechavencimiento < hoy

    def vence_antes_de(self, fecha):
        return self.fechavencimiento < fecha


class archrefri:
    def __init__(self, nombre="refri.json"):
        self.nombre = nombre
        self.alimentos = []

    def crear(self):
        try:
            with open(self.nombre, "w") as f:
                json.dump([], f)
            print("archivo creado")
        except:
            print("no se pudo")

    def cargar(self):
        try:
            with open(self.nombre, "r") as f:
                datos = json.load(f)
                self.alimentos = [alimento.from_dict(d) for d in datos]
            print(f"cargados {len(self.alimentos)} alimentos")
        except:
            self.alimentos = []

    def guardar(self):
        try:
            with open(self.nombre, "w") as f:
                datos = [a.to_dict() for a in self.alimentos]
                json.dump(datos, f)
        except:
            print("error guardando")

    # a) crear ya está, modificar por nombre y eliminar por nombre
    def modificar_nombre(self, nombre_viejo, nombre_nuevo):
        for a in self.alimentos:
            if a.nombre.lower() == nombre_viejo.lower():
                a.nombre = nombre_nuevo
                self.guardar()
                print("modificado")
                return True
        print("no se encontro")
        return False

    def eliminar_nombre(self, nombre):
        inicio = len(self.alimentos)
        self.alimentos = [a for a in self.alimentos if a.nombre.lower() != nombre.lower()]
        eliminados = inicio - len(self.alimentos)
        if eliminados > 0:
            self.guardar()
            print(f"eliminados {eliminados}")
        else:
            print("no hay con ese nombre")

    def agregar(self):
        print("nuevo alimento")
        nom = input("nombre: ")
        fecha = input("fecha vencimiento (aaaa-mm-dd): ")
        try:
            cant = int(input("cantidad: "))
        except:
            print("cantidad invalida")
            return
        
        nuevo = alimento(nom, fecha, cant)
        self.alimentos.append(nuevo)
        self.guardar()
        print("agregado")

    def listar(self):
        if not self.alimentos:
            print("refri vacio")
        for i, a in enumerate(self.alimentos, 1):
            print(f"{i}. {a}")

    # b) alimentos que caducan antes de fecha X
    def caducan_antes(self, fecha):
        return [a for a in self.alimentos if a.vence_antes_de(fecha)]

    # c) eliminar cantidad 0
    def eliminar_cero(self):
        inicio = len(self.alimentos)
        self.alimentos = [a for a in self.alimentos if a.cantidad > 0]
        eliminados = inicio - len(self.alimentos)
        if eliminados > 0:
            self.guardar()
            print(f"eliminados {eliminados} con cantidad 0")
        else:
            print("no hay con cantidad 0")

    # d) alimentos vencidos
    def vencidos(self):
        return [a for a in self.alimentos if a.esta_vencido()]

    # e) alimento con mas cantidad
    def mas_cantidad(self):
        if not self.alimentos:
            return None
        mayor = self.alimentos[0]
        for a in self.alimentos:
            if a.cantidad > mayor.cantidad:
                mayor = a
        return mayor


def main():
    refri = archrefri()
    refri.cargar()

    while True:
        print("\n-- menu refrigerador --")
        print("1. crear nuevo archivo")
        print("2. agregar alimento")
        print("3. ver alimentos")
        print("4. modificar por nombre")
        print("5. eliminar por nombre")
        print("6. caducan antes de fecha")
        print("7. eliminar cantidad 0")
        print("8. ver vencidos")
        print("9. alimento con mas cantidad")
        print("10. salir")

        op = input("opcion: ")

        if op == "1":
            refri.crear()

        elif op == "2":
            refri.agregar()

        elif op == "3":
            refri.listar()

        elif op == "4":
            viejo = input("nombre a modificar: ")
            nuevo = input("nuevo nombre: ")
            refri.modificar_nombre(viejo, nuevo)

        elif op == "5":
            nom = input("nombre a eliminar: ")
            refri.eliminar_nombre(nom)

        elif op == "6":
            fecha = input("fecha limite (aaaa-mm-dd): ")
            caducan = refri.caducan_antes(fecha)
            if caducan:
                print(f"caducan antes de {fecha}:")
                for a in caducan:
                    print(f"  - {a}")
            else:
                print("ninguno caduca antes")

        elif op == "7":
            refri.eliminar_cero()

        elif op == "8":
            vencidos = refri.vencidos()
            if vencidos:
                print("alimentos vencidos:")
                for a in vencidos:
                    print(f"  - {a}")
            else:
                print("no hay vencidos")

        elif op == "9":
            mayor = refri.mas_cantidad()
            if mayor:
                print("alimento con mas cantidad:")
                print(mayor)
            else:
                print("refri vacio")

        elif op == "10":
            print("chao")
            break

        else:
            print("opcion no")


if __name__ == "__main__":
    main()