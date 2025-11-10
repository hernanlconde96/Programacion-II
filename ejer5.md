```plantuml
@startuml
' Clases principales
class Biblioteca {
    - nombre: String
    - libros: List<Libro>
    - autores: List<Autor>
    - prestamos: List<Prestamo>
    - horario: Horario
    + agregarLibro(libro: Libro)
    + agregarAutor(autor: Autor)
    + prestarLibro(estudiante: Estudiante, libro: Libro)
    + mostrarEstado()
    + cerrarBiblioteca()
}

class Horario {
    - dias: String
    - horaApertura: String
    - horaCierre: String
    + mostrarHorario()
}

class Libro {
    - titulo: String
    - isbn: String
    - paginas: List<Pagina>
    + leer()
    + getTitulo()
}

class Pagina {
    - numero: int
    - contenido: String
    + mostrarPagina()
}

class Autor {
    - nombre: String
    - nacionalidad: String
    + mostrarInfo()
    + getNombre()
}

class Estudiante {
    - codigo: String
    - nombre: String
    + mostrarInfo()
    + getNombre()
}

class Prestamo {
    - fechaPrestamo: LocalDate
    - fechaDevolucion: LocalDate
    - estudiante: Estudiante
    - libro: Libro
    + mostrarInfo()
}

' Relaciones
Biblioteca *-- Horario : composición
Libro *-- Pagina : composición
Biblioteca o-- Libro : agregación
Biblioteca o-- Autor : agregación
Prestamo --> Estudiante : asociación
Prestamo --> Libro : asociación
@enduml
