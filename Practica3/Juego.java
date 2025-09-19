package Lab3;


import java.util.Random;
import java.util.Scanner;

class Juego {
    protected int numeroDeVidas;
    protected int record;

    public Juego(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
        this.record = 0;
    }

    public void reiniciaPartida(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
    }

    public void actualizaRecord(int vidasRestantes) {
        if (vidasRestantes > record) {
            record = vidasRestantes;
            System.out.println("WAOOOOO nuevo record " + record + " vidas restantes.");
        }
    }

    public boolean quitaVida() {
        numeroDeVidas--;
        return numeroDeVidas > 0;
    }
}