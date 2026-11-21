import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class Empleado:

  def __init__(
      self,
      nombre,
      apellidos,
      cargo,
      genero,
      salario_dia,
      dias_trabajados,
      otros_ingresos,
      pagos_salud,
      aporte_pensiones,
  ):
    self.nombre = nombre
    self.apellidos = apellidos
    self.cargo = cargo
    self.genero = genero
    self.salario_dia = salario_dia
    self.dias_trabajados = dias_trabajados
    self.otros_ingresos = otros_ingresos
    self.pagos_salud = pagos_salud
    self.aporte_pensiones = aporte_pensiones

  def calcular_salario(self):
    return (
        (self.dias_trabajados * self.salario_dia)
        + self.otros_ingresos
        - self.pagos_salud
        - self.aporte_pensiones
    )


class Nomina:

  def __init__(self):
    self.empleados = []

  def agregar_empleado(self, empleado):
    self.empleados.append(empleado)

  def calcular_total(self):
    return sum(emp.calcular_salario() for emp in self.empleados)

  def generar_texto(self):
    lineas = ["=== REPORTE DE NÓMINA ===\n"]
    for emp in self.empleados:
      lineas.append(
          f"Nombre: {emp.nombre} {emp.apellidos} | Cargo: {emp.cargo} | "
          f"Género: {emp.genero} | Días: {emp.dias_trabajados} | "
          f"Sueldo Mensual: ${emp.calcular_salario():,.2f}"
      )
    lineas.append(f"\nTOTAL NÓMINA EMPRESA: ${self.calcular_total():,.2f}")
    return "\n".join(lineas)

class InterfazNomina:

  def __init__(self, root):
    self.root = root
    self.root.title("Gestión de Nómina")
    self.root.geometry("400x250")
    self.nomina = Nomina()

    # Barra de menús
    barra_menu = tk.Menu(self.root)
    menu_opciones = tk.Menu(barra_menu, tearoff=0)
    menu_opciones.add_command(
        label="Agregar empleado", command=self.ventana_agregar
    )
    menu_opciones.add_command(
        label="Calcular nómina", command=self.ventana_calcular
    )
    menu_opciones.add_separator()
    menu_opciones.add_command(
        label="Guardar archivo", command=self.guardar_archivo
    )

    barra_menu.add_cascade(label="Menú", menu=menu_opciones)
    self.root.config(menu=barra_menu)

    tk.Label(
        self.root,
        text="Sistema de Cálculo de Nómina\n\nUse la barra superior 'Menú' para comenzar.",
        font=("Arial", 11),
        pady=60,
    ).pack()

  # --- OPCIÓN 1: AGREGAR EMPLEADO ---
  def ventana_agregar(self):
    win = tk.Toplevel(self.root)
    win.title("Agregar Empleado")
    win.geometry("360x430")
    win.grab_set()

    tk.Label(win, text="Nombre:").grid(
        row=0, column=0, sticky="w", padx=10, pady=5
    )
    ent_nombre = tk.Entry(win)
    ent_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(win, text="Apellidos:").grid(
        row=1, column=0, sticky="w", padx=10, pady=5
    )
    ent_apellidos = tk.Entry(win)
    ent_apellidos.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(win, text="Cargo:").grid(
        row=2, column=0, sticky="nw", padx=10, pady=5
    )
    lista_cargo = tk.Listbox(win, height=3, exportselection=False)
    for c in ["Directivo", "Estratégico", "Operativo"]:
      lista_cargo.insert(tk.END, c)
    lista_cargo.select_set(0)
    lista_cargo.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(win, text="Género:").grid(
        row=3, column=0, sticky="w", padx=10, pady=5
    )
    var_genero = tk.StringVar(value="Masculino")
    frame_gen = tk.Frame(win)
    frame_gen.grid(row=3, column=1, sticky="w", padx=10)
    tk.Checkbutton(
        frame_gen, text="Masculino", variable=var_genero, onvalue="Masculino"
    ).pack(side="left")
    tk.Checkbutton(
        frame_gen, text="Femenino", variable=var_genero, onvalue="Femenino"
    ).pack(side="left")

    # Salario por día
    tk.Label(win, text="Salario por día:").grid(
        row=4, column=0, sticky="w", padx=10, pady=5
    )
    ent_salario = tk.Entry(win)
    ent_salario.grid(row=4, column=1, padx=10, pady=5)

    # Días trabajados (Equivalente a JSpinner 1 a 31)
    tk.Label(win, text="Días trabajados:").grid(
        row=5, column=0, sticky="w", padx=10, pady=5
    )
    spin_dias = tk.Spinbox(win, from_=1, to=31, width=18)
    spin_dias.grid(row=5, column=1, padx=10, pady=5)

    # Otros ingresos, Salud, Pensiones
    tk.Label(win, text="Otros ingresos:").grid(
        row=6, column=0, sticky="w", padx=10, pady=5
    )
    ent_otros = tk.Entry(win)
    ent_otros.insert(0, "0")
    ent_otros.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(win, text="Pagos por salud:").grid(
        row=7, column=0, sticky="w", padx=10, pady=5
    )
    ent_salud = tk.Entry(win)
    ent_salud.insert(0, "0")
    ent_salud.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(win, text="Aporte pensiones:").grid(
        row=8, column=0, sticky="w", padx=10, pady=5
    )
    ent_pension = tk.Entry(win)
    ent_pension.insert(0, "0")
    ent_pension.grid(row=8, column=1, padx=10, pady=5)

    def guardar():
      try:
        nombre = ent_nombre.get().strip()
        apellidos = ent_apellidos.get().strip()
        if not nombre or not apellidos:
          messagebox.showwarning(
              "Aviso", "Nombre y apellidos son obligatorios.", parent=win
          )
          return

        seleccion = lista_cargo.curselection()
        cargo = lista_cargo.get(seleccion[0]) if seleccion else "Operativo"
        genero = var_genero.get()
        salario = float(ent_salario.get())
        dias = int(spin_dias.get())
        otros = float(ent_otros.get())
        salud = float(ent_salud.get())
        pension = float(ent_pension.get())

        emp = Empleado(
            nombre, apellidos, cargo, genero, salario, dias, otros, salud, pension
        )
        self.nomina.agregar_empleado(emp)
        messagebox.showinfo(
            "Éxito", "Empleado agregado correctamente.", parent=win
        )
        win.destroy()
      except ValueError:
        messagebox.showerror(
            "Error", "Verifique que los valores numéricos sean válidos.", parent=win
        )

    tk.Button(win, text="Agregar", command=guardar, width=15).grid(
        row=9, column=0, columnspan=2, pady=15
    )

  # --- OPCIÓN 2: CALCULAR NÓMINA (TABLA) ---
  def ventana_calcular(self):
    win = tk.Toplevel(self.root)
    win.title("Cálculo de Nómina")
    win.geometry("500x320")
    win.grab_set()

    columnas = ("Nombre", "Apellidos", "Sueldo Mensual")
    tabla = ttk.Treeview(win, columns=columnas, show="headings", height=10)
    for col in columnas:
      tabla.heading(col, text=col)
      tabla.column(col, width=150, anchor="center")

    for emp in self.nomina.empleados:
      tabla.insert(
          "",
          tk.END,
          values=(emp.nombre, emp.apellidos, f"${emp.calcular_salario():,.2f}"),
      )

    tabla.pack(padx=10, pady=10, fill="both", expand=True)

    total = self.nomina.calcular_total()
    tk.Label(
        win,
        text=f"Total Nómina Empresa: ${total:,.2f}",
        font=("Arial", 11, "bold"),
    ).pack(pady=10)

  # --- OPCIÓN 3: GUARDAR ARCHIVO ---
  def guardar_archivo(self):
    if not self.nomina.empleados:
      messagebox.showwarning(
          "Aviso", "No hay empleados registrados para guardar."
      )
      return

    carpeta = filedialog.askdirectory(
        title="Seleccione carpeta para guardar Nómina.txt"
    )
    if carpeta:
      ruta_archivo = os.path.join(carpeta, "Nómina.txt")
      with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(self.nomina.generar_texto())
      messagebox.showinfo("Guardado", f"Archivo generado en:\n{ruta_archivo}")


if __name__ == "__main__":
  root = tk.Tk()
  app = InterfazNomina(root)
  root.mainloop()
