import json

class animal:
    def __init__(self, especie, nombre, cantidad):
        self.especie = especie
        self.nombre = nombre
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "especie": self.especie,
            "nombre": self.nombre,
            "cantidad": self.cantidad
        }

    @staticmethod
    def from_dict(data):
        return animal(data["especie"], data["nombre"], data["cantidad"])

    def __str__(self):
        return f"{self.especie} - {self.nombre} ({self.cantidad})"


class zoologico:
    def __init__(self, cod, nombre, municipio):
        self.cod = cod
        self.nombre = nombre
        self.municipio = municipio
        self.animales = []

    def agregar_animal(self, animal):
        if len(self.animales) < 30:
            self.animales.append(animal)
            return True
        return False

    def to_dict(self):
        return {
            "cod": self.cod,
            "nombre": self.nombre,
            "municipio": self.municipio,
            "animales": [a.to_dict() for a in self.animales]
        }

    @staticmethod
    def from_dict(data):
        z = zoologico(data["cod"], data["nombre"], data["municipio"])
        z.animales = [animal.from_dict(a) for a in data["animales"]]
        return z

    def __str__(self):
        return f"{self.cod} - {self.nombre} - {len(self.animales)} animales"

    def variedad(self):
        especies = set()
        for a in self.animales:
            especies.add(a.especie)
        return len(especies)

    def vacio(self):
        return len(self.animales) == 0

    def animales_especie(self, especie):
        return [a for a in self.animales if a.especie.lower() == especie.lower()]

    def mover_a(self, otro):
        if len(otro.animales) + len(self.animales) > 30:
            return False
        for a in self.animales:
            otro.animales.append(a)
        self.animales = []
        return True


class archzoo:
    def __init__(self, nombre="zoos.json"):
        self.nombre = nombre
        self.zoos = []

    def crear(self):
        try:
            with open(self.nombre, "w") as f:
                json.dump([], f)
            print("ok")
        except:
            print("error")

    def cargar(self):
        try:
            with open(self.nombre, "r") as f:
                datos = json.load(f)
                self.zoos = [zoologico.from_dict(d) for d in datos]
        except:
            self.zoos = []

    def guardar(self):
        try:
            with open(self.nombre, "w") as f:
                datos = [z.to_dict() for z in self.zoos]
                json.dump(datos, f)
        except:
            print("error guardar")

    def agregar_zoo(self):
        try:
            cod = int(input("codigo: "))
            nom = input("nombre: ")
            mun = input("municipio: ")
        except:
            print("datos mal")
            return
        
        nuevo = zoologico(cod, nom, mun)
        self.zoos.append(nuevo)
        self.guardar()
        print("agregado")

    def modificar_zoo(self, cod):
        for z in self.zoos:
            if z.cod == cod:
                print("modificar zoo", z.cod)
                z.nombre = input("nuevo nombre: ")
                z.municipio = input("nuevo municipio: ")
                self.guardar()
                print("modificado")
                return True
        print("no encontrado")
        return False

    def eliminar_zoo(self, cod):
        inicio = len(self.zoos)
        self.zoos = [z for z in self.zoos if z.cod != cod]
        if inicio != len(self.zoos):
            self.guardar()
            print("eliminado")
        else:
            print("no esta")

    def agregar_animal_zoo(self):
        if not self.zoos:
            print("primero crea zoo")
            return
        
        print("zoos:")
        for i, z in enumerate(self.zoos, 1):
            print(f"{i}. {z}")
        
        try:
            idx = int(input("numero zoo: ")) - 1
            if idx < 0 or idx >= len(self.zoos):
                print("numero invalido")
                return
        except:
            print("numero invalido")
            return
        
        esp = input("especie: ")
        nom = input("nombre animal: ")
        try:
            cant = int(input("cantidad: "))
        except:
            print("cantidad invalida")
            return
        
        ani = animal(esp, nom, cant)
        if self.zoos[idx].agregar_animal(ani):
            self.guardar()
            print("animal agregado")
        else:
            print("no cabe, max 30")

    def listar(self):
        if not self.zoos:
            print("no hay zoos")
        for z in self.zoos:
            print(z)
            if z.animales:
                for a in z.animales:
                    print(f"  - {a}")

    def mayor_variedad(self):
        if not self.zoos:
            return []
        
        max_var = max(z.variedad() for z in self.zoos)
        return [z for z in self.zoos if z.variedad() == max_var]

    def zoos_vacios_eliminar(self):
        vacios = [z for z in self.zoos if z.vacio()]
        for z in vacios:
            self.zoos.remove(z)
        if vacios:
            self.guardar()
            print(f"eliminados {len(vacios)} vacios")
        else:
            print("no hay vacios")
        return vacios

    def animales_especie_x(self, especie):
        resultados = []
        for z in self.zoos:
            for a in z.animales_especie(especie):
                resultados.append((z, a))
        return resultados

    def mover_animales_zoo(self, cod_origen, cod_destino):
        zoo_origen = None
        zoo_destino = None
        
        for z in self.zoos:
            if z.cod == cod_origen:
                zoo_origen = z
            if z.cod == cod_destino:
                zoo_destino = z
        
        if not zoo_origen or not zoo_destino:
            print("zoos no encontrados")
            return False
        
        if zoo_origen.mover_a(zoo_destino):
            self.guardar()
            print("movidos")
            return True
        else:
            print("no cabe en destino")
            return False


def main():
    arch = archzoo()
    arch.cargar()

    while True:
        print("\n-- menu zoos --")
        print("1. crear archivo")
        print("2. agregar zoo")
        print("3. modificar zoo")
        print("4. eliminar zoo")
        print("5. agregar animal")
        print("6. ver todo")
        print("7. zoos con mas variedad")
        print("8. eliminar zoos vacios")
        print("9. animales por especie")
        print("10. mover animales entre zoos")
        print("11. salir")

        op = input("que: ")

        if op == "1":
            arch.crear()

        elif op == "2":
            arch.agregar_zoo()

        elif op == "3":
            try:
                cod = int(input("codigo a modificar: "))
                arch.modificar_zoo(cod)
            except:
                print("codigo invalido")

        elif op == "4":
            try:
                cod = int(input("codigo a eliminar: "))
                arch.eliminar_zoo(cod)
            except:
                print("codigo invalido")

        elif op == "5":
            arch.agregar_animal_zoo()

        elif op == "6":
            arch.listar()

        elif op == "7":
            variedad = arch.mayor_variedad()
            if variedad:
                print("zoos con mas variedad:")
                for z in variedad:
                    print(f"  - {z} (variedad: {z.variedad()})")
            else:
                print("no hay")

        elif op == "8":
            vacios = arch.zoos_vacios_eliminar()
            if vacios:
                print("eliminados:")
                for z in vacios:
                    print(f"  - {z}")

        elif op == "9":
            esp = input("especie a buscar: ")
            resultados = arch.animales_especie_x(esp)
            if resultados:
                print(f"animales de especie {esp}:")
                for z, a in resultados:
                    print(f"  - {a} en zoo {z.nombre}")
            else:
                print("no hay de esa especie")

        elif op == "10":
            try:
                orig = int(input("codigo zoo origen: "))
                dest = int(input("codigo zoo destino: "))
                arch.mover_animales_zoo(orig, dest)
            except:
                print("codigos invalidos")

        elif op == "11":
            print("adios")
            break

        else:
            print("opcion no")


if __name__ == "__main__":
    main()