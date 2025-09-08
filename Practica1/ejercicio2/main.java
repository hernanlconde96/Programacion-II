package ejercicio2;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("ingrese a, b, c");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        EcuacionCuadratica eq = new EcuacionCuadratica(a, b, c);

        double disc = eq.getDiscriminante();

        if (disc > 0) {
            System.out.println("la ecuacion tiene dos raices " + eq.getRaiz1() + " y " + eq.getRaiz2());
        } else if (disc == 0) {
            System.out.println("la ecuacion tiene una raiz " + eq.getRaiz1());
        } else {
            System.out.println("la ecuación no tiene raices reales");
        }

       
    }
}
