import math
import tkinter as tk

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo(valor: float) -> float:
        # El logaritmo neperiano solo está definido para números mayores a 0
        if valor <= 0:
            raise ArithmeticError("El valor para el logaritmo debe ser un número positivo mayor que cero.")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor: float) -> float:
        # La raíz cuadrada (en reales) solo está definida para números >= 0
        if valor < 0:
            raise ArithmeticError("El valor para la raíz cuadrada no puede ser negativo.")
        return math.sqrt(valor)

class VentanaCalculos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.6 - Cálculos Numéricos")
        self.geometry("380x300")
        self.resizable(False, False)

        # Entrada de valor
        tk.Label(self, text="Ingrese un número:").pack(pady=(15, 2))
        self.txt_valor = tk.Entry(self, width=25)
        self.txt_valor.pack(pady=5)

        # Botones de Operación
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Logaritmo Neperiano", command=self.procesar_logaritmo).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Raíz Cuadrada", command=self.procesar_raiz).grid(row=0, column=1, padx=5)

        # Etiqueta de resultado o error
        self.lbl_resultado = tk.Label(self, text="", fg="black", justify="center", font=("Helvetica", 9))
        self.lbl_resultado.pack(pady=15, padx=10)

    def procesar_logaritmo(self):
        self.ejecutar_operacion("log")

    def procesar_raiz(self):
        self.ejecutar_operacion("raiz")

    def ejecutar_operacion(self, tipo_operacion: str):
        val_str = self.txt_valor.get().strip()

        # Demostración de múltiples 'except' (catchs múltiples)
        try:
            val = float(val_str)
            
            if tipo_operacion == "log":
                res = CalculosNumericos.calcular_logaritmo(val)
                self.lbl_resultado.config(text=f"ln({val}) = {res:.4f}", fg="green")
            elif tipo_operacion == "raiz":
                res = CalculosNumericos.calcular_raiz_cuadrada(val)
                self.lbl_resultado.config(text=f"√({val}) = {res:.4f}", fg="green")

        # Catch 1: Captura errores de conversión numérica (tipo de dato no válido)
        except ValueError:
            self.lbl_resultado.config(text="Excepción (ValueError):\nDebe ingresar un valor numérico válido.", fg="red")

        # Catch 2: Captura excepciones aritméticas de dominio matemático
        except ArithmeticError as e:
            self.lbl_resultado.config(text=f"Excepción (ArithmeticError):\n{e}", fg="red")

        # Catch 3: Captura genérica para cualquier otra excepción inesperada
        except Exception as e:
            self.lbl_resultado.config(text=f"Excepción Genérica:\n{e}", fg="red")

if __name__ == "__main__":
    app = VentanaCalculos()
    app.mainloop()
