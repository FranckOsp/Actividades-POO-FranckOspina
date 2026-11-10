import tkinter as tk
from tkinter import messagebox

# 1. CLASE PRINCIPAL: Maneja la lógica y las excepciones
class PruebaExcepciones:
    @staticmethod
    def dividir(num_str, den_str):
        try:
            # Convertimos las entradas de texto a números flotantes
            num = float(num_str)
            den = float(den_str)
            
            # Realizamos la división
            resultado = num / den
            return f"Resultado: {resultado}"
            
        except ValueError:
            return "Error: Debes ingresar números válidos."
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero."
        finally:
            print("Operación finalizada (bloque finally executed).")

# 2. INTERFAZ GRÁFICA
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.4 - Excepciones")
        self.geometry("320x220")
        
        # Etiquetas y Cajas de texto
        tk.Label(self, text="Numerador:").pack(pady=2)
        self.txt_num = tk.Entry(self)
        self.txt_num.pack(pady=2)

        tk.Label(self, text="Denominador:").pack(pady=2)
        self.txt_den = tk.Entry(self)
        self.txt_den.pack(pady=2)

        # Botón para ejecutar
        tk.Button(self, text="Calcular", command=self.calcular).pack(pady=10)

        # Etiqueta para mostrar la respuesta
        self.lbl_resultado = tk.Label(self, text="Esperando datos...", fg="blue")
        self.lbl_resultado.pack(pady=5)

    def calcular(self):
        # Obtenemos el valor de los campos
        n = self.txt_num.get()
        d = self.txt_den.get()
        
        # Llamamos al método que gestiona las excepciones
        mensaje = PruebaExcepciones.dividir(n, d)
        
        # Mostramos la respuesta en pantalla
        self.lbl_resultado.config(text=mensaje)

# 3. EJECUCIÓN
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
