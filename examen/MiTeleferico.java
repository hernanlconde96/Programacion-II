package Examen;

public class MiTeleferico {
    Linea[] lineas;
    float cantidadIngresos;

    public MiTeleferico() {
        this.lineas = new Linea[0];
        this.cantidadIngresos = 0;
    }

    public void agregarLinea(String color) {
        Linea[] nuevo = new Linea[lineas.length + 1];
        for (int i = 0; i < lineas.length; i++)
            nuevo[i] = lineas[i];
        nuevo[nuevo.length - 1] = new Linea(color);
        lineas = nuevo;
    }

    public void agregarPersonaFila(Persona p, String linea) {
        for (int i = 0; i < lineas.length; i++) {
            if (lineas[i].color.equals(linea)) {
                lineas[i].agregarPersona(p);
                return;
            }
        }
        System.out.println("Línea no encontrada: " + linea);
    }

    public void agregarCabina(String linea, int nro) {
        for (int i = 0; i < lineas.length; i++) {
            if (lineas[i].color.equals(linea)) {
                lineas[i].agregarCabina(nro);
                return;
            }
        }
        System.out.println("Línea no encontrada: " + linea);
    }

    // a) 
    public void agregarPrimeraPersona(Persona p, int nroCab, String linea) {
        boolean lineaEncontrada = false;
        boolean cabinaEncontrada = false;
        
        for (int i = 0; i < lineas.length; i++) {
            if (lineas[i].color.equals(linea)) {
                lineaEncontrada = true;
                Linea l = lineas[i];
                for (int j = 0; j < l.cabinas.length; j++) {
                    Cabina c = l.cabinas[j];
                    if (c.nroCabina == nroCab) {
                        cabinaEncontrada = true;
                        if (c.personasAbordo.length == 0) {
                            if (p.pesoPersona <= 850) {
                                c.agregarPersona(p);
                                System.out.println("Primera persona agregada.");
                            } else {
                                System.out.println("Exceso de peso.");
                            }
                        } else {
                            System.out.println("La cabina ya tiene personas.");
                        }
                        return;
                    }
                }
            }
        }
        
        if (!lineaEncontrada) {
            System.out.println("Línea no encontrada: " + linea);
        } else if (!cabinaEncontrada) {
            System.out.println("Cabina no encontrada: " + nroCab);
        }
    }

    // b) 
    public boolean verificarReglas() {
        for (int i = 0; i < lineas.length; i++) {
            Linea l = lineas[i];
            for (int j = 0; j < l.cabinas.length; j++) {
                Cabina c = l.cabinas[j];

                
                if (c.personasAbordo.length > 10) {
                    System.out.println("Cabina " + c.nroCabina + " excede capacidad máxima");
                    return false;
                }

               
                float peso = 0;
                for (int k = 0; k < c.personasAbordo.length; k++) {
                    Persona p = c.personasAbordo[k];
                    peso += p.pesoPersona;
                }

                if (peso > 850) {
                    System.out.println("Cabina " + c.nroCabina + " excede peso máximo: " + peso + " kg");
                    return false;
                }
            }
        }
        return true;
    }

    // c) 
    public float calcularIngreso() {
        float ingreso = 0;

        for (int i = 0; i < lineas.length; i++) {
            Linea l = lineas[i];
            for (int j = 0; j < l.cabinas.length; j++) {
                Cabina c = l.cabinas[j];
                for (int k = 0; k < c.personasAbordo.length; k++) {
                    Persona p = c.personasAbordo[k];

                    if (p.edad < 25 || p.edad > 60)
                        ingreso += 1.5;
                    else
                        ingreso += 3;
                }
            }
        }

        this.cantidadIngresos = ingreso;
        return ingreso;
    }

    // d) 
    public void mostrarLineaMayorIngreso() {
        float mayor = 0;
        String lineaMayor = "No hay líneas";

        for (int i = 0; i < lineas.length; i++) {
            Linea l = lineas[i];
            float ingreso = 0;

            for (int j = 0; j < l.cabinas.length; j++) {
                Cabina c = l.cabinas[j];
                for (int k = 0; k < c.personasAbordo.length; k++) {
                    Persona p = c.personasAbordo[k];
                    
                    
                    if (p.edad >= 25 && p.edad <= 60) {
                        ingreso += 3;
                    }
                }
            }

            if (ingreso > mayor) {
                mayor = ingreso;
                lineaMayor = l.color;
            }
        }

        System.out.println("Esta es la línea con mayor ingreso regular: " 
                           + lineaMayor + " con " + mayor + " Bs.");
    }
}