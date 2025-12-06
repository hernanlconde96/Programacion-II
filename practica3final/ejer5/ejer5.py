import json

class medicamento:
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return medicamento(data["nombre"], data["tipo"], data["precio"])

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Bs. {self.precio}"


class farmacia:
    def __init__(self, nombrefarm, sucursal, direccion):
        self.nombrefarm = nombrefarm
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = []

    def agregar_med(self, med):
        self.medicamentos.append(med)

    def to_dict(self):
        return {
            "nombrefarm": self.nombrefarm,
            "sucursal": self.sucursal,
            "direccion": self.direccion,
            "medicamentos": [m.to_dict() for m in self.medicamentos]
        }

    @staticmethod
    def from_dict(data):
        f = farmacia(data["nombrefarm"], data["sucursal"], data["direccion"])
        f.medicamentos = [medicamento.from_dict(m) for m in data["medicamentos"]]
        return f

    def __str__(self):
        return f"{self.nombrefarm} - Suc.{self.sucursal} - {self.direccion}"


class archivofarmacia:
    def __init__(self, archivo="farmacias.json"):
        self.archivo = archivo
        self.farmacias = []

    def cargardatos(self):
        try:
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                self.farmacias = [farmacia.from_dict(d) for d in datos]
        except:
            self.farmacias = []

    def guardardatos(self):
        try:
            with open(self.archivo, "w") as f:
                datos = [f.to_dict() for f in self.farmacias]
                json.dump(datos, f)
        except:
            print("error")

    def meds_tos_sucursal(self, sucursal):
        for farm in self.farmacias:
            if farm.sucursal == sucursal:
                meds = []
                for m in farm.medicamentos:
                    if m.tipo.lower() == "tos":
                        meds.append(m)
                return meds
        return []

    def sucursales_con_tapsin(self):
        res = []
        for farm in self.farmacias:
            for med in farm.medicamentos:
                if med.nombre.lower() == "tapsin":
                    res.append((farm.sucursal, farm.direccion))
                    break
        return res

    def buscar_por_tipo(self, tipo):
        res = []
        for farm in self.farmacias:
            for med in farm.medicamentos:
                if med.tipo.lower() == tipo.lower():
                    res.append((farm, med))
        return res

    def ordenar_por_direccion(self):
        self.farmacias.sort(key=lambda f: f.direccion.lower())
        self.guardardatos()
        return self.farmacias

    def mover_medicamentos(self, tipo, suc_origen, suc_destino):
        farm_origen = None
        farm_destino = None
        
        for farm in self.farmacias:
            if farm.sucursal == suc_origen:
                farm_origen = farm
            if farm.sucursal == suc_destino:
                farm_destino = farm
        
        if not farm_origen or not farm_destino:
            return False
        
        meds_a_mover = []
        otros_meds = []
        
        for med in farm_origen.medicamentos:
            if med.tipo.lower() == tipo.lower():
                meds_a_mover.append(med)
            else:
                otros_meds.append(med)
        
        farm_origen.medicamentos = otros_meds
        
        for med in meds_a_mover:
            farm_destino.medicamentos.append(med)
        
        self.guardardatos()
        return True

    def ver_farmacias(self):
        if not self.farmacias:
            print("no hay farmacias")
        for f in self.farmacias:
            print(f)
            if f.medicamentos:
                print("  medicamentos:")
                for m in f.medicamentos:
                    print(f"  - {m}")


def main():
    arch = archivofarmacia()
    arch.cargardatos()

    while True:
        print("\n-- menu farmacias --")
        print("1. agregar farmacia")
        print("2. agregar medicamento")
        print("3. ver todo")
        print("4. medicamentos para tos de sucursal")
        print("5. sucursales con Tapsin")
        print("6. buscar por tipo")
        print("7. ordenar por direccion")
        print("8. mover medicamentos")
        print("9. salir")

        op = input("opcion: ")

        if op == "1":
            nom = input("nombre farmacia: ")
            suc = input("sucursal: ")
            dir = input("direccion: ")
            nueva = farmacia(nom, suc, dir)
            arch.farmacias.append(nueva)
            arch.guardardatos()
            print("agregada")

        elif op == "2":
            if not arch.farmacias:
                print("primero agrega farmacia")
                continue
            
            print("farmacias disponibles:")
            for i, f in enumerate(arch.farmacias, 1):
                print(f"{i}. {f.nombrefarm} - {f.sucursal}")
            
            try:
                idx = int(input("numero de farmacia: ")) - 1
                if idx < 0 or idx >= len(arch.farmacias):
                    print("numero invalido")
                    continue
            except:
                print("numero invalido")
                continue
            
            nom = input("nombre medicamento: ")
            tipo = input("tipo (tos, dolor, etc): ")
            try:
                precio = float(input("precio: "))
            except:
                print("precio invalido")
                continue
            
            med = medicamento(nom, tipo, precio)
            arch.farmacias[idx].agregar_med(med)
            arch.guardardatos()
            print("medicamento agregado")

        elif op == "3":
            arch.ver_farmacias()

        elif op == "4":
            suc = input("sucursal a buscar: ")
            meds = arch.meds_tos_sucursal(suc)
            if meds:
                print(f"medicamentos para tos en sucursal {suc}:")
                for m in meds:
                    print(f"  - {m}")
            else:
                print("no hay o no existe")

        elif op == "5":
            res = arch.sucursales_con_tapsin()
            if res:
                print("sucursales con Tapsin:")
                for suc, dir in res:
                    print(f"  Suc.{suc} - {dir}")
            else:
                print("ninguna tiene Tapsin")

        elif op == "6":
            tipo = input("tipo a buscar: ")
            res = arch.buscar_por_tipo(tipo)
            if res:
                print(f"medicamentos tipo {tipo}:")
                for farm, med in res:
                    print(f"  {med} en {farm.nombrefarm}")
            else:
                print("no hay de ese tipo")

        elif op == "7":
            arch.ordenar_por_direccion()
            print("ordenadas por direccion")

        elif op == "8":
            tipo = input("tipo a mover: ")
            suc_origen = input("sucursal origen: ")
            suc_destino = input("sucursal destino: ")
            
            if arch.mover_medicamentos(tipo, suc_origen, suc_destino):
                print("movidos")
            else:
                print("error")

        elif op == "9":
            print("chao")
            break

        else:
            print("opcion no")


if __name__ == "__main__":
    main()