import tkinter as tk

class Programador:
    def __init__(self, nombre: str, apellidos: str):
        self.validar_texto(nombre, "Nombre del Programador")
        self.validar_texto(apellidos, "Apellidos del Programador")
        self.nombre = nombre
        self.apellidos = apellidos

    @staticmethod
    def validar_texto(texto: str, campo: str):
        if not texto.strip():
            raise ValueError(f"El campo '{campo}' no puede estar vacío.")

        if len(texto.strip()) >= 20:
            raise ValueError(f"El campo '{campo}' no puede tener 20 o más caracteres.")

        if any(char.isdigit() for char in texto):
            raise ValueError(f"El campo '{campo}' solo debe contener texto, no números.")

class EquipoMaratonProgramacion:
    CAPACIDAD_MAXIMA = 3

    def __init__(self, nombre_equipo: str, universidad: str, lenguaje: str):
        Programador.validar_texto(nombre_equipo, "Nombre del Equipo")
        Programador.validar_texto(universidad, "Universidad")
        Programador.validar_texto(lenguaje, "Lenguaje de Programación")
        
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores = []

    def esta_completo(self) -> bool:
        return len(self.programadores) >= self.CAPACIDAD_MAXIMA

    def anadir_programador(self, programador: Programador):
        if self.esta_completo():
            raise Exception("El equipo está lleno. No se pueden añadir más de 3 programadores.")
        self.programadores.append(programador)

class VentanaEquipo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.7 - Maratón de Programación")
        self.geometry("420x580")
        self.resizable(False, False)

        self.equipo = None

        # --- SECCIÓN 1: DATOS DEL EQUIPO ---
        tk.Label(self, text="1. Registrar Equipo", font=("Helvetica", 10, "bold")).pack(pady=(10, 2))

        tk.Label(self, text="Nombre del Equipo:").pack(pady=1)
        self.txt_equipo = tk.Entry(self, width=32)
        self.txt_equipo.pack(pady=2)

        tk.Label(self, text="Universidad:").pack(pady=1)
        self.txt_universidad = tk.Entry(self, width=32)
        self.txt_universidad.pack(pady=2)

        tk.Label(self, text="Lenguaje de Programación:").pack(pady=1)
        self.txt_lenguaje = tk.Entry(self, width=32)
        self.txt_lenguaje.pack(pady=2)

        self.btn_crear_equipo = tk.Button(self, text="Crear Equipo", command=self.crear_equipo)
        self.btn_crear_equipo.pack(pady=8)

        # --- SECCIÓN 2: DATOS DEL PROGRAMADOR ---
        tk.Label(self, text="2. Añadir Integrantes (Máx 3)", font=("Helvetica", 10, "bold")).pack(pady=(10, 2))

        tk.Label(self, text="Nombre del Programador:").pack(pady=1)
        self.txt_nombre_p = tk.Entry(self, width=32, state="disabled")
        self.txt_nombre_p.pack(pady=2)

        tk.Label(self, text="Apellidos del Programador:").pack(pady=1)
        self.txt_apellidos_p = tk.Entry(self, width=32, state="disabled")
        self.txt_apellidos_p.pack(pady=2)

        self.btn_add_p = tk.Button(self, text="Añadir Programador", command=self.agregar_integrante, state="disabled")
        self.btn_add_p.pack(pady=8)

        # --- SECCIÓN 3: RESUMEN Y MENSAJES ---
        self.lbl_lista = tk.Label(self, text="Primero crea el equipo.", fg="blue", justify="left")
        self.lbl_lista.pack(pady=5)

        self.lbl_error = tk.Label(self, text="", fg="red", justify="center", font=("Helvetica", 9))
        self.lbl_error.pack(pady=5)

    def crear_equipo(self):
        self.lbl_error.config(text="")
        nom_eq = self.txt_equipo.get().strip()
        uni = self.txt_universidad.get().strip()
        leng = self.txt_lenguaje.get().strip()

        try:
            # Crea e instancia la clase EquipoMaratonProgramacion
            self.equipo = EquipoMaratonProgramacion(nom_eq, uni, leng)

            # Bloquea campos del equipo y habilita campos de programador
            self.txt_equipo.config(state="disabled")
            self.txt_universidad.config(state="disabled")
            self.txt_lenguaje.config(state="disabled")
            self.btn_crear_equipo.config(state="disabled")

            self.txt_nombre_p.config(state="normal")
            self.txt_apellidos_p.config(state="normal")
            self.btn_add_p.config(state="normal")

            self.actualizar_lista()

        except Exception as e:
            self.lbl_error.config(text=f"Error: {e}")

    def agregar_integrante(self):
        self.lbl_error.config(text="")
        nom = self.txt_nombre_p.get().strip()
        ape = self.txt_apellidos_p.get().strip()

        try:
            p = Programador(nom, ape)
            self.equipo.anadir_programador(p)

            self.txt_nombre_p.delete(0, tk.END)
            self.txt_apellidos_p.delete(0, tk.END)
            self.actualizar_lista()

            if self.equipo.esta_completo():
                self.txt_nombre_p.config(state="disabled")
                self.txt_apellidos_p.config(state="disabled")
                self.btn_add_p.config(state="disabled")

        except Exception as e:
            self.lbl_error.config(text=f"Error: {e}")

    def actualizar_lista(self):
        texto = f"Equipo: {self.equipo.nombre_equipo} ({self.equipo.universidad} - {self.equipo.lenguaje})\n"
        texto += "Integrantes:\n"
        for i, p in enumerate(self.equipo.programadores, 1):
            texto += f" {i}. {p.nombre} {p.apellidos}\n"

        if self.equipo.esta_completo():
            texto += "\n¡EQUIPO COMPLETO (3/3)!"

        self.lbl_lista.config(text=texto)

if __name__ == "__main__":
    app = VentanaEquipo()
    app.mainloop()
