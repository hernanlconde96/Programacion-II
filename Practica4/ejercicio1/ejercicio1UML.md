# Diagrama UML - Empleados

```mermaid
classDiagram
    class Empleado {
        - nombre : String
        + Empleado(String nombre)
        + CalcularSalarioMensual() double*
        + toString() String
    }

    class EmpleadoTiempoCompleto {
        - salarioAnual : double
        + EmpleadoTiempoCompleto(String nombre, double salarioAnual)
        + CalcularSalarioMensual() double
        + toString() String
    }

    class EmpleadoTiempoHorario {
        - horas : double
        - tarifa : double
        + EmpleadoTiempoHorario(String nombre, double horas, double tarifa)
        + CalcularSalarioMensual() double
        + toString() String
    }

    Empleado <|-- EmpleadoTiempoCompleto
    Empleado <|-- EmpleadoTiempoHorario
