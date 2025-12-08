import json

class Consulta:
    def __init__(self, nombre, apellido, medico_id, dia, mes, anio, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.medico_id = medico_id
        self.dia = dia
        self.mes = mes
        self.anio = anio
        self.ci = ci
    
    def to_dict(self):
        return self.__dict__

class Consultorio:
    def __init__(self):
        self.medicos = []
        self.consultas = []
        self.cargar()
    
    def cargar(self):
        try:
            with open('datos.json', 'r') as f:
                datos = json.load(f)
                self.medicos = datos.get('medicos', [])
                self.consultas = datos.get('consultas', [])
        except:
            pass
    
    def guardar(self):
        datos = {'medicos': self.medicos, 'consultas': self.consultas}
        with open('datos.json', 'w') as f:
            json.dump(datos, f, indent=2)
    
    def menu(self):
        while True:
            print("\n*********CONSULTORIO MEDICO**********")
            print("1---- agregar medico")
            print("2---- agregar consulta")
            print("3---- ver medicos")
            print("4---- ver consultas")
            print("5---- buscar por fecha")
            print("6---- dar de baja a medico")
            print("7---- Cambiar fechas festivas navidad y anio nuevo")
            print("8-------------- guardar-------------")
            
            op = input("Opcion: ")
            
            if op == "1":
                self.agregar_medico()
            elif op == "2":
                self.agregar_consulta()
            elif op == "3":
                self.ver_medicos()
            elif op == "4":
                self.ver_consultas()
            elif op == "5":
                self.buscar_fecha()
            elif op == "6":
                self.eliminar_medico()
            elif op == "7":
                self.cambiar_festivos()
            elif op == "8":
                self.guardar()
                print("guardado")
                break
    
    def agregar_medico(self):
        print("\nnuevo medico:")
        nombre = input("nombre: ")
        apellido = input("apellido: ")
        exp = input("anios experiencia: ")
        
        medico = {
            'id': len(self.medicos) + 1,
            'nombre': nombre,
            'apellido': apellido,
            'experiencia': exp
        }
        self.medicos.append(medico)
        print(f"medico {nombre} agregado")
    
    def agregar_consulta(self):
        if not self.medicos:
            print("ingrese algun medicos")
            return
        
        print("\nMedicos:")
        for m in self.medicos:
            print(f"{m['id']}. Dr. {m['nombre']} {m['apellido']}")
        
        try:
            med_id = int(input("ID medico: "))
            if med_id < 1 or med_id > len(self.medicos):
                print("ID invalido")
                return
        except:
            print("Numero invalido")
            return
        
        nombre = input("Nombre paciente: ")
        apellido = input("Apellido paciente: ")
        
        # Solicitar CI
        try:
            ci = int(input("CI del paciente (numero): "))
        except:
            print("CI debe ser numero")
            return
        
        dia = input("Dia: ")
        mes = input("Mes (ej: Diciembre): ")
        anio = input("Anio: ")
        
        nueva = Consulta(nombre, apellido, med_id, dia, mes, anio, ci)
        self.consultas.append(nueva.to_dict())
        print("consulta agregada")
    
    def ver_medicos(self):
        print("\nlista de medicos:")
        if not self.medicos:
            print("no hay medicos")
            return
        
        for m in self.medicos:
            print(f"id: {m['id']} - doctor --- {m['nombre']} {m['apellido']}")
            print(f"   exp:{m['experiencia']} anios")
            print()
    
    def ver_consultas(self):
        print("\nlista de consultas:")
        if not self.consultas:
            print("no hay consultas")
            return
        
        for c in self.consultas:
            print(f"CI: {c.get('ci', 0)}")
            print(f"   Nombre: {c['nombre']}")
            print(f"   Apellido: {c['apellido']}")
            print(f"   ID Medico: {c['medico_id']}")
            print(f"   Fecha: {c['dia']}/{c['mes']}/{c['anio']}")
            print()
    
    def buscar_fecha(self):
        dia = input("ingrese el dia: ")
        mes = input("insgrese el mes: ")
        
        encontradas = []
        for c in self.consultas:
            if str(c['dia']) == dia and c['mes'] == mes:
                encontradas.append(c)
        
        if encontradas:
            print(f"\nConsultas para el {dia} de {mes}:")
            for c in encontradas:
                print(f"  CI:{c.get('ci', 0)} - {c['nombre']} {c['apellido']} - Medico:{c['medico_id']}")
        else:
            print("No hay consultas")
    
    def eliminar_medico(self):
        if not self.medicos:
            print("No hay medicos")
            return
        
        self.ver_medicos()
        try:
            med_id = int(input("\nID del medico a eliminar: "))
        except:
            print("ID invalido")
            return
        
        
        medico = None
        for m in self.medicos:
            if m['id'] == med_id:
                medico = m
                break
        
        if not medico:
            print("medico no encontrado")
            return
        
        
        print(f"\neliminar a Dr. {medico['nombre']} {medico['apellido']}?")
        print("tambien elimine consultas")
        resp = input("s/n: ")
        
        if resp.lower() == 's':
            
            self.medicos = [m for m in self.medicos if m['id'] != med_id]
            
            
            consultas_viejas = len(self.consultas)
            self.consultas = [c for c in self.consultas if c['medico_id'] != med_id]
            eliminadas = consultas_viejas - len(self.consultas)
            
            print(f"medico eliminado. {eliminadas} consultas canceladas")
    
    def cambiar_festivos(self):
        
        print("\ncambiando consultas en dias festivos...........")
        
        cambiadas = 0
        for c in self.consultas:
            
            if c['dia'] == 25 and c['mes'] == "Diciembre":
                print(f"Consulta - CI:{c.get('ci', 0)}: {c['nombre']} - Navidad")
                nuevo = input("Nuevo dia: ")
                if nuevo.isdigit():
                    c['dia'] = int(nuevo)
                    cambiadas += 1
            
            
            elif c['dia'] == 1 and c['mes'] == "Enero":
                print(f"Consulta - CI:{c.get('ci', 0)}: {c['nombre']} - Ano Nuevo")
                nuevo = input("Nuevo dia: ")
                if nuevo.isdigit():
                    c['dia'] = int(nuevo)
                    cambiadas += 1
        
        print(f"{cambiadas} consultas cambiadas")

def main():
    print("sistema de Consultorio")
    consultorio = Consultorio()
    consultorio.menu()

if __name__ == "__main__":
    main()