package ejercicio2;

public class EcuacionCuadratica {
	
	  
	    private double a, b, c;


	    public EcuacionCuadratica(double a, double b, double c) {
	        this.a = a;
	        this.b = b;
	        this.c = c;
	    }

	    
	    public double getDiscriminante() {
	        return b * b - 4 * a * c;
	    }

	    
	    public double getRaiz1() {
	        double discriminante = getDiscriminante();
	        if (discriminante >= 0) {
	            return (-b + Math.sqrt(discriminante)) / (2 * a);
	        } else {
	            return 0;
	        }
	    }

	
	    public double getRaiz2() {
	        double discriminante = getDiscriminante();
	        if (discriminante >= 0) {
	            return (-b - Math.sqrt(discriminante)) / (2 * a);
	        } else {
	            return 0; 
	        }
	    }
	}
