package Examen;

public class Linea {
    public String color;
    public Cabina[] cabinas;

    public Linea(String color) {
        this.color = color;
        this.cabinas = new Cabina[0];
    }

    public void agregarCabina(int nro) {
        Cabina[] nuevo = new Cabina[cabinas.length + 1];
        for (int i = 0; i < cabinas.length; i++)
            nuevo[i] = cabinas[i];
        nuevo[nuevo.length - 1] = new Cabina(nro);
        cabinas = nuevo;
    }

    public void agregarPersona(Persona p) {
       
    }
}