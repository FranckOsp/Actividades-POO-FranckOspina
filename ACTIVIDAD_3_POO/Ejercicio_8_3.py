import math
import tkinter as tk
from tkinter import messagebox

class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0


class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * (self.radio ** 2) * self.altura

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.altura + self.radio)


class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self):
        return (4 / 3) * math.pi * (self.radio ** 3)

    def calcular_superficie(self):
        return 4 * math.pi * (self.radio ** 2)


class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        return ((self.base ** 2) * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lateral = 2 * self.base * self.apotema
        return area_base + area_lateral


class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcular_volumen(self):
        return self.lado ** 3

    def calcular_superficie(self):
        return 6 * (self.lado ** 2)


class Prisma(FiguraGeometrica):
    def __init__(self, largo, ancho, altura):
        super().__init__()
        self.largo = largo
        self.ancho = ancho
        self.altura = altura

    def calcular_volumen(self):
        return self.largo * self.ancho * self.altura

    def calcular_superficie(self):
        return 2 * (self.largo * self.ancho + self.largo * self.altura + self.ancho * self.altura)


# VENTANAS SECUNDARIAS PARA CADA FIGURA

class VentanaFiguraGenerica:
    """Clase base para crear la ventana secundaria de cualquier figura."""

    def __init__(self, master, titulo, campos):
        self.top = tk.Toplevel(master)
        self.top.title(titulo)
        self.top.geometry("280x260")
        self.top.resizable(False, False)

        self.campos = campos
        self.entradas = {}

        # Crear los campos de entrada etiquetados
        for i, nombre in enumerate(campos):
            lbl = tk.Label(self.top, text=nombre)
            lbl.place(x=20, y=20 + (i * 35))

            txt = tk.Entry(self.top, width=15)
            txt.place(x=130, y=20 + (i * 35))
            self.entradas[nombre] = txt

        # Posición del botón Calcular debajo de los campos
        y_boton = 20 + (len(campos) * 35) + 5
        self.btn_calcular = tk.Button(
            self.top, text="Calcular", command=self.calcular, width=12
        )
        self.btn_calcular.place(x=130, y=y_boton)

        # Etiquetas de resultados
        y_resultados = y_boton + 40
        self.lbl_volumen = tk.Label(
            self.top, text="Volumen (cm3):", font=("Arial", 9, "bold")
        )
        self.lbl_volumen.place(x=20, y=y_resultados)

        self.lbl_superficie = tk.Label(
            self.top, text="Superficie (cm2):", font=("Arial", 9, "bold")
        )
        self.lbl_superficie.place(x=20, y=y_resultados + 25)

    def obtener_valores_validados(self):
        valores = []
        for nombre, txt in self.entradas.items():
            val = txt.get().strip().replace(",", ".")
            if val == "":
                messagebox.showerror(
                    "Error", f"El campo '{nombre}' no puede estar vacío.", parent=self.top
                )
                return None
            try:
                num = float(val)
                if num <= 0:
                    messagebox.showerror(
                        "Error", f"El valor de '{nombre}' debe ser mayor a 0.", parent=self.top
                    )
                    return None
                valores.append(num)
            except ValueError:
                messagebox.showerror(
                    "Error", f"El valor de '{nombre}' debe ser un número.", parent=self.top
                )
                return None
        return valores

    def calcular(self):
        pass


class VentanaCilindro(VentanaFiguraGenerica):
    def __init__(self, master):
        super().__init__(master, "Cilindro", ["Radio (cms):", "Altura (cms):"])

    def calcular(self):
        vals = self.obtener_valores_validados()
        if vals:
            c = Cilindro(vals[0], vals[1])
            self.lbl_volumen.config(text=f"Volumen (cm3): {c.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {c.calcular_superficie():.2f}")


class VentanaEsfera(VentanaFiguraGenerica):
    def __init__(self, master):
        super().__init__(master, "Esfera", ["Radio (cms):"])

    def calcular(self):
        vals = self.obtener_valores_validados()
        if vals:
            e = Esfera(vals[0])
            self.lbl_volumen.config(text=f"Volumen (cm3): {e.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {e.calcular_superficie():.2f}")


class VentanaPiramide(VentanaFiguraGenerica):
    def __init__(self, master):
        super().__init__(
            master, "Pirámide", ["Base (cms):", "Altura (cms):", "Apotema (cms):"]
        )

    def calcular(self):
        vals = self.obtener_valores_validados()
        if vals:
            p = Piramide(vals[0], vals[1], vals[2])
            self.lbl_volumen.config(text=f"Volumen (cm3): {p.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {p.calcular_superficie():.2f}")


class VentanaCubo(VentanaFiguraGenerica):
    def __init__(self, master):
        super().__init__(master, "Cubo", ["Lado (cms):"])

    def calcular(self):
        vals = self.obtener_valores_validados()
        if vals:
            cb = Cubo(vals[0])
            self.lbl_volumen.config(text=f"Volumen (cm3): {cb.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cb.calcular_superficie():.2f}")


class VentanaPrisma(VentanaFiguraGenerica):
    def __init__(self, master):
        super().__init__(
            master, "Prisma", ["Largo (cms):", "Ancho (cms):", "Altura (cms):"]
        )

    def calcular(self):
        vals = self.obtener_valores_validados()
        if vals:
            pr = Prisma(vals[0], vals[1], vals[2])
            self.lbl_volumen.config(text=f"Volumen (cm3): {pr.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {pr.calcular_superficie():.2f}")


# VENTANA PRINCIPAL (a)

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras")
        self.root.geometry("450x100")
        self.root.resizable(False, False)

        # Marco centrado para los botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(expand=True)

        # Botones para abrir cada ventana de figura
        btn_cilindro = tk.Button(
            frame_botones,
            text="Cilindro",
            width=8,
            command=lambda: VentanaCilindro(self.root),
        )
        btn_cilindro.grid(row=0, column=0, padx=5, pady=20)

        btn_esfera = tk.Button(
            frame_botones,
            text="Esfera",
            width=8,
            command=lambda: VentanaEsfera(self.root),
        )
        btn_esfera.grid(row=0, column=1, padx=5, pady=20)

        btn_piramide = tk.Button(
            frame_botones,
            text="Pirámide",
            width=8,
            command=lambda: VentanaPiramide(self.root),
        )
        btn_piramide.grid(row=0, column=2, padx=5, pady=20)

        btn_cubo = tk.Button(
            frame_botones,
            text="Cubo",
            width=8,
            command=lambda: VentanaCubo(self.root),
        )
        btn_cubo.grid(row=0, column=3, padx=5, pady=20)

        btn_prisma = tk.Button(
            frame_botones,
            text="Prisma",
            width=8,
            command=lambda: VentanaPrisma(self.root),
        )
        btn_prisma.grid(row=0, column=4, padx=5, pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
