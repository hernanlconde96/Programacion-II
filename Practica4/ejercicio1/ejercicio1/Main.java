package Lab4;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Empleado empleados[] = new Empleado[5];

        for (int i = 0; i < 3; i++) {
            System.out.println("empleado completo " + (i+1));
            System.out.print("nombre: ");
            String nombre = sc.nextLine();
            System.out.print("salario anual: ");
            double anual = sc.nextDouble();
            sc.nextLine();
            empleados[i] = new EmpleadoTiempoCompleto(nombre, anual);
        }

        for (int i = 3; i < 5; i++) {
            System.out.println("empleado por horas " + (i-2));
            System.out.print("nombre: ");
            String nombre = sc.nextLine();
            System.out.print("horas: ");
            double h = sc.nextDouble();
            System.out.print("tarifa: ");
            double t = sc.nextDouble();
            sc.nextLine();
            empleados[i] = new EmpleadoTiempoHorario(nombre, h, t);
        }

        System.out.println("\n--- lista de empleados ---");
        for (Empleado e : empleados) {
            System.out.println(e.toString());
            System.out.println("salario mensual: " + e.CalcularSalarioMensual());
            System.out.println("-------------------");
        }

        
    }
}
