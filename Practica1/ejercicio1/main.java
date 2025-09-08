package ejercicio1;
import java.util.Scanner;
public class main {

	 public static void main(String[] args) {


        Scanner sc = new Scanner(System.in);

        System.out.println("ingrese a, b, c, d, e, f");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        double d = sc.nextDouble();
        double e = sc.nextDouble();
        double f = sc.nextDouble();

       
        EcuacionLineal eq = new EcuacionLineal(a, b, c, d, e, f);

      
        if (eq.tieneSolucion()) {
            System.out.println("la solución es:");
            System.out.println("x = " + eq.getX());
            System.out.println("y = " + eq.getY());
        } else {
            System.out.println("la ecuacion no tiene solucion.");
        }

     
    }
}