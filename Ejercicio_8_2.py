import math
import tkinter as tk
from tkinter import messagebox

class NotasEstudiante:
    def __init__(self, lista_notas):
        self.notas = lista_notas

    def calcular_promedio(self):
        suma = sum(self.notas)
        return suma / len(self.notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma_cuadrados = 0
        for nota in self.notas:
            suma_cuadrados += (nota - promedio) ** 2
        varianza = suma_cuadrados / len(self.notas)
        return math.sqrt(varianza)

    def obtener_mayor(self):
        return max(self.notas)

    def obtener_menor(self):
        return min(self.notas)

# CLASE PARA LA INTERFAZ GRÁFICA (Tkinter)

class VentanaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejercicio 8.2 - Notas")
        self.ventana.geometry("300x350")

        # Lista para guardar los 5 cuadros de texto de las notas
        self.entradas = []

        # Crear los labels y campos para ingresar las 5 notas
        for i in range(5):
            lbl = tk.Label(self.ventana, text=f"Nota {i + 1}:")
            lbl.pack()
            
            txt = tk.Entry(self.ventana)
            txt.pack()
            self.entradas.append(txt)

        # Botón para calcular
        self.btn_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular_resultados)
        self.btn_calcular.pack(pady=10)

        # Labels para mostrar los resultados al final
        self.lbl_promedio = tk.Label(self.ventana, text="Promedio: ")
        self.lbl_promedio.pack()

        self.lbl_desviacion = tk.Label(self.ventana, text="Desviación estándar: ")
        self.lbl_desviacion.pack()

        self.lbl_mayor = tk.Label(self.ventana, text="Mayor nota: ")
        self.lbl_mayor.pack()

        self.lbl_menor = tk.Label(self.ventana, text="Menor nota: ")
        self.lbl_menor.pack()

    def calcular_resultados(self):
        notas_ingresadas = []

        # Validar cada entrada
        for i in range(5):
            valor = self.entradas[i].get().strip()

            # 1. Alerta si no se ingresó la nota
            if valor == "":
                messagebox.showerror("Error", f"Falta ingresar la Nota {i + 1}")
                return

            # 2. Alerta si el dato no es numérico
            try:
                nota_float = float(valor)
                notas_ingresadas.append(nota_float)
            except ValueError:
                messagebox.showerror("Error", f"La Nota {i + 1} debe ser un número")
                return

        # Si todo está bien, creamos el objeto y calculamos
        estudiante = NotasEstudiante(notas_ingresadas)

        self.lbl_promedio.config(text=f"Promedio: {estudiante.calcular_promedio():.2f}")
        self.lbl_desviacion.config(text=f"Desviación estándar: {estudiante.calcular_desviacion():.2f}")
        self.lbl_mayor.config(text=f"Mayor nota: {estudiante.obtener_mayor()}")
        self.lbl_menor.config(text=f"Menor nota: {estudiante.obtener_menor()}")

# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
