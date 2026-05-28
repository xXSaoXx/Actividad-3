import math
import tkinter as tk
from tkinter import messagebox


class CalculadoraNotas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculo de notas")
        self.ventana.geometry("300x400")
        self.ventana.resizable(False, False)

        self.notas = []
        self.entradas = []

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(
            self.ventana,
            text="Ingrese cinco notas del estudiante",
            font=("Arial", 12, "bold"),
            wraplength=250,
            justify="left"
        )
        titulo.pack(pady=15, padx=10, anchor="w")

        contenedor_entradas = tk.Frame(self.ventana)
        contenedor_entradas.pack(padx=10, anchor="w")

        for i in range(5):
            etiqueta = tk.Label(contenedor_entradas, text="Nota " + str(i + 1) + ":")
            etiqueta.grid(row=i, column=0, padx=8, pady=6, sticky="w")

            entrada = tk.Entry(contenedor_entradas, width=18)
            entrada.grid(row=i, column=1, padx=8, pady=6)
            self.entradas.append(entrada)

        contenedor_botones = tk.Frame(self.ventana)
        contenedor_botones.pack(pady=15, padx=10, anchor="w")

        boton_calcular = tk.Button(
            contenedor_botones,
            text="Calcular",
            width=12,
            command=self.calcular
        )
        boton_calcular.grid(row=0, column=0, padx=5)

        boton_limpiar = tk.Button(
            contenedor_botones,
            text="Limpiar",
            width=12,
            command=self.limpiar
        )
        boton_limpiar.grid(row=0, column=1, padx=5)

        contenedor_resultados = tk.Frame(self.ventana)
        contenedor_resultados.pack(pady=5, padx=10, anchor="w")

        self.resultado_promedio = tk.Label(contenedor_resultados, text="Promedio: ")
        self.resultado_promedio.pack(anchor="w")

        self.resultado_desviacion = tk.Label(contenedor_resultados, text="Desviacion estandar: ")
        self.resultado_desviacion.pack(anchor="w")

        self.resultado_mayor = tk.Label(contenedor_resultados, text="Mayor nota: ")
        self.resultado_mayor.pack(anchor="w")

        self.resultado_menor = tk.Label(contenedor_resultados, text="Menor nota: ")
        self.resultado_menor.pack(anchor="w")

    def calcular(self):
        self.notas = []

        for i in range(5):
            texto = self.entradas[i].get()

            if texto == "":
                messagebox.showerror("Error", "Debe ingresar las cinco notas.")
                return

            try:
                nota = float(texto)
            except ValueError:
                messagebox.showerror("Error", "Las notas deben ser datos numericos.")
                return

            self.notas.append(nota)

        promedio = sum(self.notas) / len(self.notas)

        varianza = 0
        for nota in self.notas:
            varianza = varianza + (nota - promedio) ** 2

        varianza = varianza / (len(self.notas) - 1)
        desviacion = math.sqrt(varianza)
        mayor = max(self.notas)
        menor = min(self.notas)

        self.resultado_promedio.config(text="Promedio: " + str(round(promedio, 2)))
        self.resultado_desviacion.config(text="Desviacion estandar: " + str(round(desviacion, 2)))
        self.resultado_mayor.config(text="Mayor nota: " + str(round(mayor, 2)))
        self.resultado_menor.config(text="Menor nota: " + str(round(menor, 2)))

    def limpiar(self):
        for entrada in self.entradas:
            entrada.delete(0, tk.END)

        self.notas = []
        self.resultado_promedio.config(text="Promedio: ")
        self.resultado_desviacion.config(text="Desviacion estandar: ")
        self.resultado_mayor.config(text="Mayor nota: ")
        self.resultado_menor.config(text="Menor nota: ")

    def iniciar(self):
        self.ventana.mainloop()


programa = CalculadoraNotas()
programa.iniciar()
