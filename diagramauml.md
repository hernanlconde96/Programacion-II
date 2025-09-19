## Diagrama UML - Juego Adivina Número

```mermaid
classDiagram
    class Juego {
        - numeroDeVidas : int
        - record : int
        + Juego(int numeroDeVidas)
        + reiniciaPartida(int numeroDeVidas) : void
        + actualizaRecord(int vidasRestantes) : void
        + quitaVida() : boolean
    }

    class JuegoAdivinaNumero {
        - numeroAAdivinar : int
        - intentosMaximos : int
        + JuegoAdivinaNumero(int intentosMaximos)
        + juega() : void
        + validaNumero(int n) : boolean
        # generaNumeroAAdivinar() : int
    }

    class JuegoAdivinaPar {
        + JuegoAdivinaPar(int intentosMaximos)
        + validaNumero(int n) : boolean
        # generaNumeroAAdivinar() : int
    }

    class JuegoAdivinaImpar {
        + JuegoAdivinaImpar(int intentosMaximos)
        + validaNumero(int n) : boolean
        # generaNumeroAAdivinar() : int
    }

    class Aplicacion {
        + main(String[] args) : void
    }

    Juego <|-- JuegoAdivinaNumero
    JuegoAdivinaNumero <|-- JuegoAdivinaPar
    JuegoAdivinaNumero <|-- JuegoAdivinaImpar
    Aplicacion ..> JuegoAdivinaNumero : "crea / usa"
