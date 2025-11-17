package Examen;

public class Cabina {
    public int nroCabina;
    public Persona[] personasAbordo;

    public Cabina(int nroCabina) {
        this.nroCabina = nroCabina;
        this.personasAbordo = new Persona[0];
    }

    public void agregarPersona(Persona p) {
        Persona[] nuevo = new Persona[personasAbordo.length + 1];
        for (int i = 0; i < personasAbordo.length; i++)
            nuevo[i] = personasAbordo[i];
        nuevo[nuevo.length - 1] = p;
        personasAbordo = nuevo;
    }
}