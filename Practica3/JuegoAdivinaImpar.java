package Lab3;

public class JuegoAdivinaImpar extends JuegoAdivinaNumero {

    public JuegoAdivinaImpar(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    @Override
    public boolean validaNumero(int n) {
       
        if (n < 0 || n > 10) {
            System.out.println("ingrese numeros del 0 al 10!!!!!!!!!!!!!");
            return false;
        }
       
        if (n % 2 == 0) {
            System.out.println("solo se permiten numero IMPARES");
            return false;
        }
        return true;
    }
}
