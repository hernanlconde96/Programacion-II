package Examen;

public class Main {
    public static void main(String[] args) {

        MiTeleferico mt = new MiTeleferico();

        //agregar líneas
        mt.agregarLinea("Amarillo");
        mt.agregarLinea("Rojo");
        mt.agregarLinea("Verde");

        //agregar cabinas
        mt.agregarCabina("Amarillo", 1);
        mt.agregarCabina("Amarillo", 2);
        mt.agregarCabina("Rojo", 1);
        mt.agregarCabina("Rojo", 2);
        mt.agregarCabina("Verde", 1);

        
        Persona p1 = new Persona("Juan", 20, 60);   
        Persona p2 = new Persona("Ana", 30, 65);    
        Persona p3 = new Persona("Pedro", 70, 70);  
        Persona p4 = new Persona("Lucia", 40, 55); 
        Persona p5 = new Persona("Carlos", 24, 80); 
        Persona p6 = new Persona("Maria", 50, 90);  

       
//a
        System.out.println("\nprimera per-");
        mt.agregarPrimeraPersona(p1, 1, "Amarillo");
        mt.agregarPrimeraPersona(p2, 1, "Amarillo");
        mt.agregarPrimeraPersona(p3, 2, "Amarillo");
        mt.agregarPrimeraPersona(p4, 1, "Rojo");

       
        System.out.println("\n--- agregando per ---");
        for (Linea l : mt.lineas) {
            if (l.color.equals("Amarillo")) {
                for (Cabina c : l.cabinas) {
                    if (c.nroCabina == 1) {
                        c.agregarPersona(p2);
                        c.agregarPersona(p5);
                        System.out.println("Se agregaron 2 personas a Cabina Amarillo-1");
                    }
                    if (c.nroCabina == 2) {
                        c.agregarPersona(p6);
                        System.out.println("Se agregó 1 persona a Cabina Amarillo-2");
                    }
                }
            }
            if (l.color.equals("Rojo")) {
                for (Cabina c : l.cabinas) {
                    if (c.nroCabina == 1) {
                        Persona p7 = new Persona("Luis", 25, 75);
                        Persona p8 = new Persona("Elena", 61, 65);
                        c.agregarPersona(p7);
                        c.agregarPersona(p8);
                        System.out.println("Se agregaron 2 personas a Cabina Rojo-1");
                    }
                }
            }
        }

        //b
        System.out.println("\n--- reglaaaa ---");
        boolean reglas = mt.verificarReglas();
        System.out.println("resultado de verificacion: " + (reglas ? "CUMPLE" : "NO CUMPLE"));

      //c
        System.out.println("\n--- CALCULO DE INGRESOS ---");
        float ingresoTotal = mt.calcularIngreso();
        System.out.println("Ingreso total del sistema: " + ingresoTotal + " Bs.");

        System.out.println("\nDetalle de tarifas aplicadas:");
        System.out.println("- Tarifa preferencial (menores de 25 o mayores de 60): 1.5 Bs");
        System.out.println("- Tarifa regular (entre 25 y 60 años): 3.0 Bs");

       //d
        System.out.println("\n--- LINEA CON MAYOR INGRESO REGULAR ---");
        mt.mostrarLineaMayorIngreso();

        //inf
        System.out.println("\n--- REPORTE DETALLADO DEL SISTEMA ---");
        System.out.println("Total de lineas registradas: " + mt.lineas.length);
        
        for (Linea l : mt.lineas) {
            int totalPersonasLinea = 0;
            float ingresoLinea = 0;
            float ingresoRegularLinea = 0;
            
            System.out.println("\nLINEA: " + l.color);
            System.out.println("  Numero de cabinas: " + l.cabinas.length);
            
            for (Cabina c : l.cabinas) {
                System.out.println("  Cabina " + c.nroCabina + " - Personas: " + c.personasAbordo.length);
                
                float pesoTotalCabina = 0;
                for (Persona p : c.personasAbordo) {
                    String tipoTarifa = (p.edad < 25 || p.edad > 60) ? "Preferencial" : "Regular";
                    float tarifa = (p.edad < 25 || p.edad > 60) ? 1.5f : 3.0f;
                    
                    System.out.println("    - " + p.nombre + " | Edad: " + p.edad + 
                                     " | Peso: " + p.pesoPersona + "kg | Tarifa: " + tipoTarifa);
                    
                    pesoTotalCabina += p.pesoPersona;
                    ingresoLinea += tarifa;
                    if (p.edad >= 25 && p.edad <= 60) {
                        ingresoRegularLinea += 3.0f;
                    }
                }
                totalPersonasLinea += c.personasAbordo.length;
                System.out.println("    Peso total de la cabina: " + pesoTotalCabina + " kg");
                System.out.println("    Limite de peso: 850 kg");
                System.out.println("    Estado: " + (pesoTotalCabina <= 850 ? "DENTRO DEL LIMITE" : "EXCEDE LIMITE"));
            }
            
            System.out.println("  RESUMEN LINEA " + l.color + ":");
            System.out.println("    - Total de personas: " + totalPersonasLinea);
            System.out.println("    - Ingreso total: " + ingresoLinea + " Bs");
            System.out.println("    - Ingreso por tarifa regular: " + ingresoRegularLinea + " Bs");
        }

    }
}