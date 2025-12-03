import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime, timedelta

class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido




class Libro:
    def __init__(self, titulo, isbn, contenido_paginas=None):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = []
        if contenido_paginas:
            for i, cont in enumerate(contenido_paginas, 1):
                self.paginas.append(Pagina(i, cont))
    def agregar_pagina(self, contenido):
        self.paginas.append(Pagina(len(self.paginas)+1, contenido))




class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def mostrar_info(self):
        return f"{self.nombre} ({self.nacionalidad})"






class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    def mostrar_info(self):
        return f"{self.nombre} - Cód: {self.codigo}"





class Horario:
    def __init__(self):
        self.dias = "Lunes a Viernes"
        self.apertura = "08:00"
        self.cierre = "20:00"




    def mostrar(self):
        return f"{self.dias} de {self.apertura} a {self.cierre}"




class Prestamo:
    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = datetime.now().strftime("%d/%m/%Y")
        self.fecha_devolucion = (datetime.now() + timedelta(days=15)).strftime("%d/%m/%Y")
    def mostrar_info(self):
        return f"{self.estudiante.nombre} -> {self.libro.titulo} | Dev: {self.fecha_devolucion}"





class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horario = Horario()
        self.libros = []
        self.autores = []
        self.estudiantes = []
        self.prestamos = []
        self.cargar_datos()
    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.guardar_datos()
    def agregar_autor(self, autor):
        self.autores.append(autor)
        self.guardar_datos()
    def registrar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        self.guardar_datos()
    def prestar_libro(self, codigo_est, isbn_libro):
        estudiante = self.buscar_estudiante(codigo_est)
        libro = self.buscar_libro(isbn_libro)
        if not estudiante or not libro:
            return False, "Estudiante o libro no encontrado"
        for p in self.prestamos:
            if p.libro.isbn == isbn_libro:
                return False, "Libro ya prestado"
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        self.guardar_datos()
        return True, "Préstamo exitoso"
    def devolver_libro(self, isbn):
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == isbn:
                self.prestamos.remove(prestamo)
                self.guardar_datos()
                return True, "Libro devuelto"
        return False, "Préstamo no encontrado"
    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None
    def buscar_estudiante(self, codigo):
        for estudiante in self.estudiantes:
            if estudiante.codigo == codigo:
                return estudiante
        return None
    def mostrar_estado(self):
        texto = f"=== {self.nombre} ===\n"
        texto += f"Horario: {self.horario.mostrar()}\n\n"
        texto += f"Libros ({len(self.libros)}):\n"
        for libro in self.libros:
            disponible = "Disponible" if not any(p.libro.isbn == libro.isbn for p in self.prestamos) else "Prestado"
            texto += f"  {disponible} - {libro.titulo} (ISBN: {libro.isbn})\n"
        texto += f"\nPréstamos activos ({len(self.prestamos)}):\n"
        for prestamo in self.prestamos:
            texto += f"  {prestamo.mostrar_info()}\n"
        return texto





    def guardar_datos(self):
        datos = {
            'libros': [{'titulo': l.titulo, 'isbn': l.isbn, 'paginas': [p.contenido for p in l.paginas]} for l in self.libros],
            'autores': [{'nombre': a.nombre, 'nacionalidad': a.nacionalidad} for a in self.autores],
            'estudiantes': [{'codigo': e.codigo, 'nombre': e.nombre} for e in self.estudiantes],
            'prestamos': [{'codigo': p.estudiante.codigo, 'isbn': p.libro.isbn, 'fecha': p.fecha_prestamo} for p in self.prestamos]
        }
        try:
            with open('datos_biblioteca.json', 'w') as f:
                json.dump(datos, f, indent=2)
        except:
            pass
    def cargar_datos(self):
        try:
            with open('datos_biblioteca.json', 'r') as f:
                datos = json.load(f)
            for l in datos['libros']:
                libro = Libro(l['titulo'], l['isbn'], l['paginas'])
                self.libros.append(libro)
            for a in datos['autores']:
                autor = Autor(a['nombre'], a['nacionalidad'])
                self.autores.append(autor)
            for e in datos['estudiantes']:
                estudiante = Estudiante(e['codigo'], e['nombre'])
                self.estudiantes.append(estudiante)
            for p in datos['prestamos']:
                estudiante = self.buscar_estudiante(p['codigo'])
                libro = self.buscar_libro(p['isbn'])
                if estudiante and libro:
                    prestamo = Prestamo(estudiante, libro)
                    prestamo.fecha_prestamo = p['fecha']
                    self.prestamos.append(prestamo)
        except FileNotFoundError:
            self.crear_datos_ejemplo()
 
 
 
    def crear_datos_ejemplo(self):
        libro1 = Libro("cien años d soledad", "1234", ["muchos años despues...", "el coronel...", "final..."])
        libro2 = Libro("El principito", "0987654321", ["dibujo 1", "dibujo 2", "la rosa"])
        self.agregar_libro(libro1)
        self.agregar_libro(libro2)
        autor1 = Autor("gabriel garcia marquez", "colombiano")
        autor2 = Autor("antoine de aaint-exupéry", "frances")
        self.agregar_autor(autor1)
        self.agregar_autor(autor2)
        est1 = Estudiante("123798", "ana garcia")
        est2 = Estudiante("951253", "carlos lopez")
        self.registrar_estudiante(est1)
        self.registrar_estudiante(est2)





class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca UMSA INF - 121")
        self.root.geometry("800x750")
        self.root.configure(bg="#1A1A1A")
        self.biblioteca = Biblioteca("Biblioteca Central")
        self.crear_interfaz()
    def crear_interfaz(self):
        main_frame = tk.Frame(self.root, bg="#1A1A1A", padx=15, pady=15)
        main_frame.pack(fill='both', expand=True)
        tk.Label(main_frame, text="SISTEMA DE BIBLIOTECA UMSA", font=("Arial", 20, "bold"), bg="#1A1A1A", fg="#F1C40F").pack(pady=(0,20))
        btn_frame = tk.Frame(main_frame, bg="#1A1A1A")
        btn_frame.pack(pady=5, fill='x')
        btn_opts = [("Agregar Libro", self.agregar_libro, "#34495E"),
                    ("Registrar Estudiante", self.registrar_estudiante, "#27AE60"),
                    ("Realizar Préstamo", self.realizar_prestamo, "#E74C3C"),
                    ("Devolver Libro", self.devolver_libro, "#F39C12")]
        for i, (text, cmd, color) in enumerate(btn_opts):
            tk.Button(btn_frame, text=text, bg=color, fg="white", font=("Arial", 11), width=20, height=2, bd=0, cursor="hand2", command=cmd).grid(row=i//2, column=i%2, padx=5, pady=5)
        status_frame = tk.Frame(main_frame, bg="#1A1A1A")
        status_frame.pack(pady=10, fill='both', expand=True)
        left_frame = tk.Frame(status_frame, bg="#2C3E50", bd=2, relief=tk.RIDGE)
        left_frame.pack(side='left', padx=5, pady=5, fill='both', expand=True)
        tk.Label(left_frame, text="Estado Biblioteca", bg="#2C3E50", fg="#F1C40F", font=("Arial", 14, "bold")).pack(pady=5)
        self.texto_estado = tk.Text(left_frame, height=20, bg="#1C2833", fg="#ECF0F1", font=("Consolas", 10))
        self.texto_estado.pack(fill='both', expand=True, padx=5, pady=5)
        tk.Scrollbar(left_frame, command=self.texto_estado.yview).pack(side='right', fill='y')
        self.texto_estado.config(yscrollcommand=self.texto_estado.yview)
        right_frame = tk.Frame(status_frame, bg="#2C3E50", bd=2, relief=tk.RIDGE)
        right_frame.pack(side='left', padx=5, pady=5, fill='both', expand=True)
        tk.Label(right_frame, text="Estudiantes Registrados", bg="#2C3E50", fg="#F1C40F", font=("Arial", 14, "bold")).pack(pady=5)
        self.texto_estudiantes = tk.Text(right_frame, height=20, bg="#1C2833", fg="#ECF0F1", font=("Consolas", 10))
        self.texto_estudiantes.pack(fill='both', expand=True, padx=5, pady=5)
        tk.Scrollbar(right_frame, command=self.texto_estudiantes.yview).pack(side='right', fill='y')
        self.texto_estudiantes.config(yscrollcommand=self.texto_estudiantes.yview)
        tk.Button(main_frame, text="Actualizar Estado", bg="#9B59B6", fg="white", font=("Arial", 12, "bold"), width=25, height=2, bd=0, cursor="hand2", command=self.actualizar_estado).pack(pady=10)
        self.actualizar_estado()
    
    
    
    def agregar_libro(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Libro")
        ventana.geometry("450x400")
        ventana.configure(bg="#2C3E50")
        tk.Label(ventana, text="Título:", bg="#2C3E50", fg="#F1C40F", font=("Arial", 11)).pack(pady=5)
        titulo_entry = tk.Entry(ventana, width=40, font=("Arial", 11))
        titulo_entry.pack(pady=5)
        tk.Label(ventana, text="ISBN:", bg="#2C3E50", fg="#F1C40F", font=("Arial", 11)).pack(pady=5)
        isbn_entry = tk.Entry(ventana, width=40, font=("Arial", 11))
        isbn_entry.pack(pady=5)
        tk.Label(ventana, text="Contenido (una página por línea):", bg="#2C3E50", fg="#F1C40F", font=("Arial", 11)).pack(pady=5)
        contenido_text = tk.Text(ventana, width=40, height=8, font=("Arial", 10))
        contenido_text.pack(pady=5)
        def guardar():
            titulo = titulo_entry.get()
            isbn = isbn_entry.get()
            contenido = contenido_text.get("1.0", tk.END).strip().split('\n')
            if titulo and isbn:
                libro = Libro(titulo, isbn, contenido)
                self.biblioteca.agregar_libro(libro)
                messagebox.showinfo("Éxito", f"Libro '{titulo}' agregado")
                ventana.destroy()
                self.actualizar_estado()
            else:
                messagebox.showwarning("Error", "Complete título e ISBN")
        tk.Button(ventana, text="Guardar", bg="#27AE60", fg="white", font=("Arial", 11), command=guardar, width=15, height=2).pack(pady=10)
    def registrar_estudiante(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Registrar Estudiante")
        ventana.geometry("350x250")
        ventana.configure(bg="#34495E")
        tk.Label(ventana, text="Código:", bg="#34495E", fg="#F1C40F", font=("Arial", 11)).pack(pady=10)
        codigo_entry = tk.Entry(ventana, width=30, font=("Arial", 11))
        codigo_entry.pack(pady=5)
        tk.Label(ventana, text="Nombre:", bg="#34495E", fg="#F1C40F", font=("Arial", 11)).pack(pady=10)
        nombre_entry = tk.Entry(ventana, width=30, font=("Arial", 11))
        nombre_entry.pack(pady=5)
        def guardar():
            codigo = codigo_entry.get()
            nombre = nombre_entry.get()
            if codigo and nombre:
                estudiante = Estudiante(codigo, nombre)
                self.biblioteca.registrar_estudiante(estudiante)
                messagebox.showinfo("Éxito", f"Estudiante '{nombre}' registrado")
                ventana.destroy()
                self.actualizar_estado()
            else:
                messagebox.showwarning("Error", "Complete todos los campos")
        tk.Button(ventana, text="Registrar", bg="#2980B9", fg="white", font=("Arial", 11), command=guardar, width=15, height=2).pack(pady=20)
    def realizar_prestamo(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Realizar Préstamo")
        ventana.geometry("350x250")
        ventana.configure(bg="#34495E")
        tk.Label(ventana, text="Código del Estudiante:", bg="#34495E", fg="#F1C40F", font=("Arial", 11)).pack(pady=10)
        codigo_entry = tk.Entry(ventana, width=30, font=("Arial", 11))
        codigo_entry.pack(pady=5)
        tk.Label(ventana, text="ISBN del Libro:", bg="#34495E", fg="#F1C40F", font=("Arial", 11)).pack(pady=10)
        isbn_entry = tk.Entry(ventana, width=30, font=("Arial", 11))
        isbn_entry.pack(pady=5)
        def procesar():
            codigo = codigo_entry.get()
            isbn = isbn_entry.get()
            if codigo and isbn:
                exito, mensaje = self.biblioteca.prestar_libro(codigo, isbn)
                if exito:
                    messagebox.showinfo("Éxito", mensaje)
                    ventana.destroy()
                    self.actualizar_estado()
                else:
                    messagebox.showerror("Error", mensaje)
            else:
                messagebox.showwarning("Error", "Complete todos los campos")
        tk.Button(ventana, text="Prestar Libro", bg="#E67E22", fg="white", font=("Arial", 11), command=procesar, width=15, height=2).pack(pady=20)
    def devolver_libro(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Devolver Libro")
        ventana.geometry("350x200")
        ventana.configure(bg="#34495E")
        tk.Label(ventana, text="ISBN del Libro a devolver:", bg="#34495E", fg="#F1C40F", font=("Arial", 11)).pack(pady=20)
        isbn_entry = tk.Entry(ventana, width=30, font=("Arial", 11))
        isbn_entry.pack(pady=5)
        def procesar():
            isbn = isbn_entry.get()
            if isbn:
                exito, mensaje = self.biblioteca.devolver_libro(isbn)
                if exito:
                    messagebox.showinfo("Éxito", mensaje)
                    ventana.destroy()
                    self.actualizar_estado()
                else:
                    messagebox.showerror("Error", mensaje)
            else:
                messagebox.showwarning("Error", "Ingrese el ISBN")
        tk.Button(ventana, text="Devolver", bg="#C0392B", fg="white", font=("Arial", 11), command=procesar, width=15, height=2).pack(pady=20)
    def actualizar_estado(self):
        estado = self.biblioteca.mostrar_estado()
        self.texto_estado.delete(1.0, tk.END)
        self.texto_estado.insert(1.0, estado)
        self.actualizar_estudiantes()
    def actualizar_estudiantes(self):
        self.texto_estudiantes.delete(1.0, tk.END)
        texto = ""
        for e in self.biblioteca.estudiantes:
            texto += f"  {e.mostrar_info()}\n"
        self.texto_estudiantes.insert(1.0, texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
