## 🎮 Diagrama UML - Juego Adivina Número

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
        + JuegoAdivinaNumero(int numeroDeVidas)
        + juega() : void
        + validaNumero(int n) : boolean
    }

    class JuegoAdivinaPar {
        + JuegoAdivinaPar(int numeroDeVidas)
        + validaNumero(int n) : boolean
    }

    class JuegoAdivinaImpar {
        + JuegoAdivinaImpar(int numeroDeVidas)
        + validaNumero(int n) : boolean
    }

    Juego <|-- JuegoAdivinaNumero
    JuegoAdivinaNumero <|-- JuegoAdivinaPar
    JuegoAdivinaNumero <|-- JuegoAdivinaImpar
