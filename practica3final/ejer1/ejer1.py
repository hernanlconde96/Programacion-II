import json

class charango:
    def __init__(self, material, nrocuerdas, cuerdas):
        self.material = material
        self.nrocuerdas = nrocuerdas
        self.cuerdas = cuerdas

    def to_dict(self):
        return {
            "material": self.material,
            "nrocuerdas": self.nrocuerdas,
            "cuerdas": self.cuerdas
        }

    @staticmethod
    def from_dict(data):
        return charango(data["material"], data["nrocuerdas"], data["cuerdas"])

    def __str__(self):
        return f"{self.material} - {self.nrocuerdas} cuerdas: {self.cuerdas}"


def guardar(lista, archivo="charangos.json"):
    try:
        with open(archivo, "w") as f:
            json.dump([c.to_dict() for c in lista], f)
    except:
        pass

def cargar(archivo="charangos.json"):
    try:
        with open(archivo, "r") as f:
            data = json.load(f)
            return [charango.from_dict(x) for x in data]
    except:
        return []


def eliminar_falsos(lista):
    nueva = []
    for c in lista:
        if sum(1 for x in c.cuerdas if not x) <= 6:
            nueva.append(c)
    return nueva

def buscar_material(lista, material):
    return [c for c in lista if c.material.lower() == material.lower()]

def buscar_10_cuerdas(lista):
    return [c for c in lista if c.nrocuerdas == 10]

def ordenar_material(lista):
    return sorted(lista, key=lambda x: x.material.lower())

def main():
    datos = cargar()
    
    while True:
        print("\n****menu del charango****")
        print("1-- agregar")
        print("2-- ver todo")
        print("3-- eliminar con >6 cuerdas falsas")
        print("4-- buscar por material")
        print("5-- buscar de 10 cuerdas")
        print("6-- ordenar por material")
        print("7-- salir")
        
        op = input("elije una opcion: ")
        
        if op == "1":
            m = input("material: ")
            try:
                n = int(input("cuantas cuerdas: "))
            except:
                print("numero invalido")
                continue
                
            estados = []
            for i in range(n):
                e = input(f"cuerda {i+1} (1=true, 0=false): ")
                estados.append(e == "1")
            
            datos.append(charango(m, n, estados))
            print("ok")
            
        elif op == "2":
            if not datos:
                print("vacio no ay charangos")
            for c in datos:
                print(c)
                
        elif op == "3":
            datos = eliminar_falsos(datos)
            print("hecho")
            
        elif op == "4":
            m = input("material: ")
            r = buscar_material(datos, m)
            if r:
                for c in r:
                    print(c)
            else:
                print("no encontrado")
                
        elif op == "5":
            r = buscar_10_cuerdas(datos)
            if r:
                for c in r:
                    print(c)
            else:
                print("no hay")
                
        elif op == "6":
            datos = ordenar_material(datos)
            print("ordenado")
            
        elif op == "7":
            guardar(datos)
            print("******chaito*******")
            break
            
        else:
            print("error")

if __name__ == "__main__":
    main()