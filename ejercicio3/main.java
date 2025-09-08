package ejercicio3;

import java.util.Scanner;
import java.util.Locale;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.useLocale(Locale.US); 

        double[] datos = new double[10];

        System.out.println("ingrese 10 numeros:");
        for (int i = 0; i < 10; i++) {
            datos[i] = sc.nextDouble();
        }

        double prom = Estadistica.promedio(datos);
        double desvM = Estadistica.desviacionMuestral(datos);
        double desvP = Estadistica.desviacionPoblacional(datos);

        System.out.println("el promedio es: " + prom);
        System.out.println("la desviación estandar muestral es: " + desvM);
        System.out.println("la desviación estandar poblacional es: " + desvP);

     
    }
}
