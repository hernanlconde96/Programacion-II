package Lab4;

abstract class Empleado {
    protected String nombre;

    public Empleado(String nom) {
        this.nombre = nom;
    }

    abstract double CalcularSalarioMensual();

    public String toString() {
        return "empleado: " + nombre;
    }
}
