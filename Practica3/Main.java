	package Lab3;
	
	public class Main {
	    public static void main(String[] args) {
	        JuegoAdivinaNumero juego1 = new JuegoAdivinaNumero(3);
	        JuegoAdivinaPar juego2 = new JuegoAdivinaPar(3);
	        JuegoAdivinaImpar juego3 = new JuegoAdivinaImpar(3);
	
	        System.out.println("\n--- juego adivina numero ---");
	        juego1.juega();
	
	        System.out.println("\n--- juego adivina numero PAR ---");
	        juego2.juega();
	
	        System.out.println("\n--- juego adivina numero IMPAR ---");
	        juego3.juega();
	    }
	}
