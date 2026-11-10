import os
import tkinter as tk
from tkinter import filedialog

# ==========================================
# 1. CLASE LÓGICA (LeerArchivo)
# ==========================================
class LeerArchivo:
    @staticmethod
    def leer_contenido(ruta_archivo: str) -> str:
        # Validar ruta vacía
        if not ruta_archivo.strip():
            raise ValueError("Debe ingresar o seleccionar la ruta de un archivo.")

        # Intentar abrir y leer el archivo
        try:
            # Se lee en modo texto con codificación utf-8
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                return contenido

        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe o no fue encontrado.")
        except IsADirectoryError:
            raise IsADirectoryError("La ruta ingresada corresponde a una carpeta, no a un archivo.")
        except Exception as e:
            raise IOError(f"Error inesperado al intentar leer el archivo: {e}")


# ==========================================
# 2. INTERFAZ GRÁFICA (Tkinter)
# ==========================================
class VentanaLector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.8 - Lector de Archivos")
        self.geometry("480x420")
        self.resizable(False, False)

        # Selección de archivo
        tk.Label(self, text="Ruta del archivo (ej. prueba.txt):", font=("Helvetica", 10, "bold")).pack(pady=(12, 2))

        frame_ruta = tk.Frame(self)
        frame_ruta.pack(pady=5, padx=10)

        self.txt_ruta = tk.Entry(frame_ruta, width=38)
        self.txt_ruta.insert(0, "prueba.txt")  # Nombre por defecto
        self.txt_ruta.pack(side="left", padx=5)

        btn_examinar = tk.Button(frame_ruta, text="Buscar...", command=self.buscar_archivo)
        btn_examinar.pack(side="left")

        # Botón para Cargar / Leer
        btn_leer = tk.Button(self, text="Leer Contenido del Archivo", command=self.cargar_archivo)
        btn_leer.pack(pady=8)

        # Área de Visualización
        tk.Label(self, text="Contenido del archivo:").pack(anchor="w", padx=20, pady=(5, 2))
        
        self.txt_contenido = tk.Text(self, width=54, height=12, font=("Consolas", 9))
        self.txt_contenido.pack(pady=5, padx=15)

        # Mensaje de estado / error
        self.lbl_estado = tk.Label(self, text="", fg="black", font=("Helvetica", 9))
        self.lbl_estado.pack(pady=5)

    def buscar_archivo(self):
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if filename:
            self.txt_ruta.delete(0, tk.END)
            self.txt_ruta.insert(0, filename)

    def cargar_archivo(self):
        self.txt_contenido.delete("1.0", tk.END)
        self.lbl_estado.config(text="")
        ruta = self.txt_ruta.get().strip()

        try:
            contenido = LeerArchivo.leer_contenido(ruta)
            self.txt_contenido.insert(tk.END, contenido)
            self.lbl_estado.config(text="¡Archivo leído con éxito!", fg="green")

        except Exception as e:
            self.lbl_estado.config(text=f"Excepción: {e}", fg="red")


# ==========================================
# 3. EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    # Creamos un archivo 'prueba.txt' de prueba si no existe
    if not os.path.exists("prueba.txt"):
        with open("prueba.txt", "w", encoding="utf-8") as f:
            f.write("¡Hola! Este es el contenido de prueba del archivo prueba.txt.\nEjercicio 6.8 resuelto correctamente.")

    app = VentanaLector()
    app.mainloop()
