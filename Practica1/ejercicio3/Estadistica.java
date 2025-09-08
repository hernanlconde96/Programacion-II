package ejercicio3;

public class Estadistica {

	
    public static double promedio(double[] datos) {
        double suma = 0;
        for (double x : datos) {
            suma += x;
        }
        return suma / datos.length;
    }


    
    public static double desviacionMuestral(double[] datos) {
        double prom = promedio(datos);
        double suma = 0;
        for (double x : datos) {
            suma += Math.pow(x - prom, 2);
        }
        return Math.sqrt(suma / (datos.length - 1));
    }


    
    public static double desviacionPoblacional(double[] datos) {
        double prom = promedio(datos);
        double suma = 0;
        for (double x : datos) {
            suma += Math.pow(x - prom, 2);
        }
        return Math.sqrt(suma / datos.length);
    }
}
