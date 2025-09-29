package Lab4ejer2;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Figura[] figs = new Figura[5];
        Random r = new Random();

        for (int i = 0; i < figs.length; i++) {
            int tipo = r.nextInt(2) + 1;
            if (tipo == 1) {
                double l = r.nextInt(9) + 2;
                figs[i] = new Cuadrado(l, "rojo");
            } else {
                double ra = r.nextInt(9) + 2;
                figs[i] = new Circulo(ra, "azul");
            }
        }

        System.out.println("--- figuras generadas ---");
        for (Figura f : figs) {
            System.out.println(f.toString());
            System.out.println("area: " + f.area());
            System.out.println("perimetro: " + f.perimetro());
            if (f instanceof Coloreado) {
                System.out.println(((Coloreado) f).comoColorear());
            }
            System.out.println("-------------");
        }
    }
}
