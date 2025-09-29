package Lab4ejer2;


public abstract class Figura {
    protected String color;

    public Figura(String c) {
        color = c;
    }

    public void setColor(String c) {
        color = c;
    }

    public String getColor() {
        return color;
    }

    public abstract double area();
    public abstract double perimetro();

    public String toString() {
        return "color=" + color;
    }
}

