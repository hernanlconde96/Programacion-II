package Lab4;

public class EmpleadoTiempoHorario extends Empleado {
    private double horas;
    private double tarifa;

    public EmpleadoTiempoHorario(String n, double h, double t) {
        super(n);
        horas = h;
        tarifa = t;
    }

    public double CalcularSalarioMensual() {
        return horas * tarifa;
    }

    public String toString() {
        return super.toString() + " - tiempo horario, horas=" + horas + ", tarifa=" + tarifa;
    }
}
