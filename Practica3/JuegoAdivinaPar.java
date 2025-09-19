package Lab3;

public class JuegoAdivinaPar extends JuegoAdivinaNumero {

    public JuegoAdivinaPar(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    @Override
    public boolean validaNumero(int n) {
      
        if (n < 0 || n > 10) {
            System.out.println("ingrese numero del 0 al 10!!!!!!!!!!!!!");
            return false;
        }
      
        if (n % 2 != 0) {
            System.out.println("solo se permiten numero PARES");
            return false;
        }
        return true;
    }
}
