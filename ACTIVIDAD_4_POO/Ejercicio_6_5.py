import tkinter as tk

class Vendedor:
    def __init__(self, nombre: str, apellidos: str, edad: int):
        # Primero verificamos la edad. Si falla, 'raise' detiene la ejecución.
        self.verificar_edad(edad)
        
        # Si no hubo excepciones, asignamos los atributos
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def verificar_edad(self, edad: int):
        # 1. Regla: Rango de edad (0 a 120)
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        
        # 2. Regla: Mayoría de edad (mínimo 18)
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años")

    def imprimir(self) -> str:
        return f"VENDEDOR REGISTRADO:\nNombre: {self.nombre} {self.apellidos}\nEdad: {self.edad} años"

class VentanaVendedor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ejercicio 6.5 - Lanzamiento de Excepciones")
        self.geometry("360x320")
        self.resizable(False, False)

        # Formulario de entrada
        tk.Label(self, text="Nombre:").pack(pady=(10, 2))
        self.txt_nombre = tk.Entry(self, width=30)
        self.txt_nombre.pack(pady=2)

        tk.Label(self, text="Apellidos:").pack(pady=(5, 2))
        self.txt_apellidos = tk.Entry(self, width=30)
        self.txt_apellidos.pack(pady=2)

        tk.Label(self, text="Edad:").pack(pady=(5, 2))
        self.txt_edad = tk.Entry(self, width=30)
        self.txt_edad.pack(pady=2)

        # Botón de acción
        tk.Button(self, text="Crear Vendedor", command=self.crear_vendedor).pack(pady=12)

        # Mensaje de resultado o error
        self.lbl_mensaje = tk.Label(self, text="", fg="black", justify="center")
        self.lbl_mensaje.pack(pady=5)

    def crear_vendedor(self):
        try:
            nom = self.txt_nombre.get().strip()
            ape = self.txt_apellidos.get().strip()
            edad = int(self.txt_edad.get().strip())

            # Intentamos instanciar al Vendedor (esto probará el 'raise')
            v = Vendedor(nom, ape, edad)
            
            # Si se creó con éxito, mostramos la información
            self.lbl_mensaje.config(text=v.imprimir(), fg="green")

        except ValueError as e:
            # Capturamos tanto errores de conversión como los lanzados por 'raise'
            if "invalid literal" in str(e):
                self.lbl_mensaje.config(text="Error: Ingrese un valor numérico en la edad.", fg="red")
            else:
                self.lbl_mensaje.config(text=f"Excepción capturada:\n{e}", fg="red")

if __name__ == "__main__":
    app = VentanaVendedor()
    app.mainloop()
