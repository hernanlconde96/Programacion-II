package Lab4;

public class EmpleadoTiempoCompleto extends Empleado {
    private double salarioAnual;

    public EmpleadoTiempoCompleto(String n, double sAnual) {
        super(n);
        salarioAnual = sAnual;
    }

    public double CalcularSalarioMensual() {
        return salarioAnual / 12;
    }

    public String toString() {
        return super.toString() + " - tiempo completo, salario anual=" + salarioAnual;
    }
}
