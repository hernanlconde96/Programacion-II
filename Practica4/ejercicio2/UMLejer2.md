
---

# 📂 `figuras_uml.md`
```markdown
# Diagrama UML - Figuras

```mermaid
classDiagram
    class Coloreado {
        <<interface>>
        + comoColorear() String
    }

    class Figura {
        - color : String
        + Figura(String color)
        + setColor(String) void
        + getColor() String
        + area() double*
        + perimetro() double*
        + toString() String
    }

    class Cuadrado {
        - lado : double
        + Cuadrado(double lado, String color)
        + area() double
        + perimetro() double
        + comoColorear() String
        + toString() String
    }

    class Circulo {
        - radio : double
        + Circulo(double radio, String color)
        + area() double
        + perimetro() double
        + toString() String
    }

    Figura <|-- Cuadrado
    Figura <|-- Circulo
    Coloreado <|.. Cuadrado
