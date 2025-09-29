package Lab4ejer2;

public class Circulo extends Figura {
    private double radio;

    public Circulo(double r, String c) {
        super(c);
        radio = r;
    }

    public double area() {
        return Math.PI * radio * radio;
    }

    public double perimetro() {
        return 2 * Math.PI * radio;
    }

    public String toString() {
        return "circulo(radio=" + radio + ", " + super.toString() + ")";
    }
}
