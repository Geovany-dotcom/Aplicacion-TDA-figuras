
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_resultados(self, area, perimetro):
        return f"Resultados de {self.nombre}:\nÁrea: {round(area, 2)}\nPerímetro: {round(perimetro, 2)}"

class Rectangulo(Figura):
    def __init__(self, altura, base):
        super().__init__("Rectángulo")
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base

    def calcular_perimetro(self):
        return 2 * (self.altura + self.base)

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.1416 * self.radio

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Triangulo(Figura):
    def __init__(self, lado_a, lado_b, lado_c):
        super().__init__("Triángulo")
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def tipo_triangulo(self):
        if self.lado_a == self.lado_b == self.lado_c:
            return "Equilátero"
        elif self.lado_a == self.lado_b or self.lado_a == self.lado_c or self.lado_b == self.lado_c:
            return "Isósceles"
        else:
            return "Escaleno"

    def calcular_area(self):
        s = (self.lado_a + self.lado_b + self.lado_c) / 2
        area = (s * (s - self.lado_a) * (s - self.lado_b) * (s - self.lado_c)) ** 0.5
        return area

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

