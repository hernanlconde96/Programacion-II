package Lab3;
import java.util.*;

class JuegoAdivinaNumero extends Juego {
    private int numeroAAdivinar;

    public JuegoAdivinaNumero(int numeroDeVidas) {
        super(numeroDeVidas);
    }

   
    public boolean validaNumero(int n) {
        return n >= 0 && n <= 10;
    }

    public void juega() {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        reiniciaPartida(numeroDeVidas); 
        numeroAAdivinar = rand.nextInt(11); 

        System.out.println("Ingresa un número del 0 al 10");

        while (true) {
            System.out.print("INGRESE NÚMERO: ");
            int intento = sc.nextInt();

          
            if (!validaNumero(intento)) {
                System.out.println("Número inválido. Debe estar entre 0 y 10.");
                continue;
            }

            if (intento == numeroAAdivinar) {
                System.out.println("!!!!!!!!!!Acertaste!!!!!!!!!!");
                actualizaRecord(numeroDeVidas);
                break;
            } else {
                if (quitaVida()) {
                    if (intento < numeroAAdivinar) {
                        System.out.println("El número que tratas de adivinar es MAYOR");
                    } else {
                        System.out.println("El número que tratas de adivinar es MENOR");
                    }
                    System.out.println("SOLO QUEDAN " + numeroDeVidas + " vidas");
                } else {
                    System.out.println("NO TIENES VIDAS. FIN DEL JUEGO");
                    System.out.println("EL NÚMERO ERA: " + numeroAAdivinar);
                    break;
                }
            }
        }
    }
}
