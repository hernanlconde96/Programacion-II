## 🎮 Diagrama UML - Juego Adivina Número

```mermaid
classDiagram
    class JuegoAdivinaNumero {
        - int numeroAAdivinar
        - int intentosMaximos
        + JuegoAdivinaNumero(int intentosMaximos)
        + juega()
        + validaNumero(int n) boolean
        # generaNumeroAAdivinar() int
    }

    class JuegoAdivinaPar {
        + JuegoAdivinaPar(int intentosMaximos)
        + validaNumero(int n) boolean
        # generaNumeroAAdivinar() int
    }

    class JuegoAdivinaImpar {
        + JuegoAdivinaImpar(int intentosMaximos)
        + validaNumero(int n) boolean
        # generaNumeroAAdivinar() int
    }

    JuegoAdivinaNumero <|-- JuegoAdivinaPar
    JuegoAdivinaNumero <|-- JuegoAdivinaImpar
