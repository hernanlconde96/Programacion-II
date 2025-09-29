package Lab4ejer2;

public class Cuadrado extends Figura implements Coloreado {
    private double lado;

    public Cuadrado(double l, String c) {
        super(c);
        lado = l;
    }

    public double area() {
        return lado * lado;
    }

    public double perimetro() {
        return lado * 4;
    }

    public String comoColorear() {
        return "colorear 4 lados";
    }

    public String toString() {
        return "cuadrado(lado=" + lado + ", " + super.toString() + ")";
    }
}
