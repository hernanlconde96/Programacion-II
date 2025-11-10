```mermaid
classDiagram
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

  
    Prestamo --> Estudiante
    Prestamo --> Libro
