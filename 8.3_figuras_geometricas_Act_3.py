import math
import tkinter as tk
from tkinter import messagebox


class FiguraGeometrica:
    def calcular_volumen(self):
        pass

    def calcular_superficie(self):
        pass


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio ** 2


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral


class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        return self.lado ** 3

    def calcular_superficie(self):
        return 6 * self.lado ** 2


class PrismaRectangular(FiguraGeometrica):
    def __init__(self, largo, ancho, altura):
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def calcular_volumen(self):
        return self.largo * self.ancho * self.altura

    def calcular_superficie(self):
        return 2 * (
            self.largo * self.ancho +
            self.largo * self.altura +
            self.ancho * self.altura
        )


class VentanaFigura:
    def __init__(self, titulo):
        self.ventana = tk.Toplevel()
        self.ventana.title(titulo)
        self.ventana.geometry("320x310")
        self.ventana.resizable(False, False)

        self.entradas = []

    def crear_entrada(self, texto, fila):
        etiqueta = tk.Label(self.ventana, text=texto)
        etiqueta.grid(row=fila, column=0, padx=10, pady=5, sticky="w")

        entrada = tk.Entry(self.ventana, width=18)
        entrada.grid(row=fila, column=1, padx=10, pady=5, sticky="w")
        self.entradas.append(entrada)

        return entrada

    def obtener_numero(self, entrada):
        try:
            numero = float(entrada.get())
        except ValueError:
            return None

        if numero <= 0:
            return None

        return numero

    def mostrar_resultados(self, volumen, superficie):
        self.resultado_volumen.config(text="Volumen (cm3): " + str(round(volumen, 2)))
        self.resultado_superficie.config(text="Superficie (cm2): " + str(round(superficie, 2)))

    def crear_resultados(self, fila):
        self.resultado_volumen = tk.Label(self.ventana, text="Volumen (cm3): ")
        self.resultado_volumen.grid(row=fila, column=0, columnspan=2, padx=10, pady=8, sticky="w")

        self.resultado_superficie = tk.Label(self.ventana, text="Superficie (cm2): ")
        self.resultado_superficie.grid(row=fila + 1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    def crear_boton(self, fila):
        boton = tk.Button(self.ventana, text="Calcular", width=12, command=self.calcular)
        boton.grid(row=fila, column=1, padx=10, pady=5, sticky="w")

    def crear_canvas(self, fila):
        self.canvas = tk.Canvas(self.ventana, width=110, height=90, bg="white")
        self.canvas.grid(row=fila, column=0, columnspan=2, padx=10, pady=5, sticky="w")

    def limpiar_canvas(self):
        self.canvas.delete("all")


class VentanaCilindro(VentanaFigura):
    def __init__(self):
        super().__init__("Cilindro")

        self.radio = self.crear_entrada("Radio (cms):", 0)
        self.altura = self.crear_entrada("Altura (cms):", 1)
        self.crear_boton(2)
        self.crear_canvas(3)
        self.crear_resultados(4)
        self.dibujar_imagen()

    def dibujar_imagen(self):
        self.limpiar_canvas()
        self.canvas.create_oval(25, 10, 85, 30, outline="blue", width=2)
        self.canvas.create_line(25, 20, 25, 65, fill="blue", width=2)
        self.canvas.create_line(85, 20, 85, 65, fill="blue", width=2)
        self.canvas.create_oval(25, 55, 85, 75, outline="blue", width=2)

    def calcular(self):
        radio = self.obtener_numero(self.radio)
        altura = self.obtener_numero(self.altura)

        if radio is None or altura is None:
            messagebox.showerror("Error", "Todos los datos deben ser numeros mayores que 0.")
            return

        cilindro = Cilindro(radio, altura)
        self.mostrar_resultados(cilindro.calcular_volumen(), cilindro.calcular_superficie())


class VentanaEsfera(VentanaFigura):
    def __init__(self):
        super().__init__("Esfera")

        self.radio = self.crear_entrada("Radio (cms):", 0)
        self.crear_boton(1)
        self.crear_canvas(2)
        self.crear_resultados(3)
        self.dibujar_imagen()

    def dibujar_imagen(self):
        self.limpiar_canvas()
        self.canvas.create_oval(25, 15, 85, 75, outline="green", width=2)
        self.canvas.create_arc(25, 30, 85, 60, start=0, extent=359, outline="green")
        self.canvas.create_line(55, 45, 85, 45, fill="green")

    def calcular(self):
        radio = self.obtener_numero(self.radio)

        if radio is None:
            messagebox.showerror("Error", "Todos los datos deben ser numeros mayores que 0.")
            return

        esfera = Esfera(radio)
        self.mostrar_resultados(esfera.calcular_volumen(), esfera.calcular_superficie())


class VentanaPiramide(VentanaFigura):
    def __init__(self):
        super().__init__("Piramide")

        self.base = self.crear_entrada("Base (cms):", 0)
        self.altura = self.crear_entrada("Altura (cms):", 1)
        self.apotema = self.crear_entrada("Apotema (cms):", 2)
        self.crear_boton(3)
        self.crear_canvas(4)
        self.crear_resultados(5)
        self.dibujar_imagen()

    def dibujar_imagen(self):
        self.limpiar_canvas()
        self.canvas.create_polygon(55, 10, 20, 70, 90, 70, outline="purple", fill="", width=2)
        self.canvas.create_line(55, 10, 55, 70, fill="purple", dash=(3, 2))
        self.canvas.create_line(20, 70, 40, 80, fill="purple", width=2)
        self.canvas.create_line(90, 70, 70, 80, fill="purple", width=2)
        self.canvas.create_line(40, 80, 70, 80, fill="purple", width=2)
        self.canvas.create_line(55, 10, 40, 80, fill="purple", width=2)
        self.canvas.create_line(55, 10, 70, 80, fill="purple", width=2)

    def calcular(self):
        base = self.obtener_numero(self.base)
        altura = self.obtener_numero(self.altura)
        apotema = self.obtener_numero(self.apotema)

        if base is None or altura is None or apotema is None:
            messagebox.showerror("Error", "Todos los datos deben ser numeros mayores que 0.")
            return

        piramide = Piramide(base, altura, apotema)
        self.mostrar_resultados(piramide.calcular_volumen(), piramide.calcular_superficie())


class VentanaCubo(VentanaFigura):
    def __init__(self):
        super().__init__("Cubo")

        self.lado = self.crear_entrada("Lado (cms):", 0)
        self.crear_boton(1)
        self.crear_canvas(2)
        self.crear_resultados(3)
        self.dibujar_imagen()

    def dibujar_imagen(self):
        self.limpiar_canvas()
        self.canvas.create_rectangle(25, 35, 70, 80, outline="orange", width=2)
        self.canvas.create_rectangle(40, 20, 85, 65, outline="orange", width=2)
        self.canvas.create_line(25, 35, 40, 20, fill="orange", width=2)
        self.canvas.create_line(70, 35, 85, 20, fill="orange", width=2)
        self.canvas.create_line(70, 80, 85, 65, fill="orange", width=2)

    def calcular(self):
        lado = self.obtener_numero(self.lado)

        if lado is None:
            messagebox.showerror("Error", "Todos los datos deben ser numeros mayores que 0.")
            return

        cubo = Cubo(lado)
        self.mostrar_resultados(cubo.calcular_volumen(), cubo.calcular_superficie())


class VentanaPrisma(VentanaFigura):
    def __init__(self):
        super().__init__("Prisma rectangular")

        self.largo = self.crear_entrada("Largo (cms):", 0)
        self.ancho = self.crear_entrada("Ancho (cms):", 1)
        self.altura = self.crear_entrada("Altura (cms):", 2)
        self.crear_boton(3)
        self.crear_canvas(4)
        self.crear_resultados(5)
        self.dibujar_imagen()

    def dibujar_imagen(self):
        self.limpiar_canvas()
        self.canvas.create_rectangle(20, 35, 75, 75, outline="red", width=2)
        self.canvas.create_rectangle(40, 15, 95, 55, outline="red", width=2)
        self.canvas.create_line(20, 35, 40, 15, fill="red", width=2)
        self.canvas.create_line(75, 35, 95, 15, fill="red", width=2)
        self.canvas.create_line(75, 75, 95, 55, fill="red", width=2)

    def calcular(self):
        largo = self.obtener_numero(self.largo)
        ancho = self.obtener_numero(self.ancho)
        altura = self.obtener_numero(self.altura)

        if largo is None or ancho is None or altura is None:
            messagebox.showerror("Error", "Todos los datos deben ser numeros mayores que 0.")
            return

        prisma = PrismaRectangular(largo, ancho, altura)
        self.mostrar_resultados(prisma.calcular_volumen(), prisma.calcular_superficie())


class AplicacionPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Figuras")
        self.ventana.geometry("430x170")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.ventana,
            font=("Arial", 12, "bold")
        )
        titulo.pack(pady=15)

        contenedor = tk.Frame(self.ventana)
        contenedor.pack(pady=15)

        tk.Button(contenedor, text="Cilindro", width=10, command=VentanaCilindro).grid(row=0, column=0, padx=5)
        tk.Button(contenedor, text="Esfera", width=10, command=VentanaEsfera).grid(row=0, column=1, padx=5)
        tk.Button(contenedor, text="Piramide", width=10, command=VentanaPiramide).grid(row=0, column=2, padx=5)
        tk.Button(contenedor, text="Cubo", width=10, command=VentanaCubo).grid(row=1, column=0, padx=5, pady=10)
        tk.Button(contenedor, text="Prisma", width=10, command=VentanaPrisma).grid(row=1, column=1, padx=5, pady=10)

    def iniciar(self):
        self.ventana.mainloop()


programa = AplicacionPrincipal()
programa.iniciar()