from datetime import datetime
import tkinter as tk
from tkinter import messagebox

class Huesped:

  def __init__(self, nombre, apellidos, documento, fecha_ingreso):
    self.nombre = nombre
    self.apellidos = apellidos
    self.documento = documento
    self.fecha_ingreso = fecha_ingreso


class Habitacion:

  def __init__(self, numero, precio_dia):
    self.numero = numero
    self.precio_dia = precio_dia
    self.disponible = True
    self.huesped = None

  def ocupar(self, huesped):
    self.huesped = huesped
    self.disponible = False

  def liberar(self):
    self.huesped = None
    self.disponible = True

  def calcular_pago(self, fecha_salida):
    dias = (fecha_salida - self.huesped.fecha_ingreso).days
    total = dias * self.precio_dia
    return dias, total


class Hotel:

  def __init__(self):
    self.habitaciones = []
    # Habitaciones 1 a 5: $120.000 | Habitaciones 6 a 10: $160.000
    for i in range(1, 11):
      precio = 120000 if i <= 5 else 160000
      self.habitaciones.append(Habitacion(i, precio))

  def obtener_habitacion(self, numero):
    if 1 <= numero <= 10:
      return self.habitaciones[numero - 1]
    return None


class InterfazHotel:

  def __init__(self, root):
    self.root = root
    self.root.title("Gestión de Hotel")
    self.root.geometry("400x220")
    self.hotel = Hotel()

    # Barra de menús
    barra_menu = tk.Menu(self.root)
    menu_hotel = tk.Menu(barra_menu, tearoff=0)
    menu_hotel.add_command(
        label="Consultar habitaciones", command=self.ventana_consultar
    )
    menu_hotel.add_command(
        label="Salida de huéspedes", command=self.ventana_salida_buscar
    )

    barra_menu.add_cascade(label="Menú", menu=menu_hotel)
    self.root.config(menu=barra_menu)

    tk.Label(
        self.root,
        text="Sistema de Control Hotelero\n\nSeleccione una opción en 'Menú'.",
        font=("Arial", 11),
        pady=60,
    ).pack()

  # --- OPCIÓN 1: CONSULTAR HABITACIONES
  def ventana_consultar(self):
    win = tk.Toplevel(self.root)
    win.title("Habitaciones del Hotel")
    win.geometry("460x300")
    win.grab_set()

    frame_grid = tk.Frame(win, padx=10, pady=10)
    frame_grid.pack()

    # Cuadrícula para mostrar las 10 habitaciones
    for idx, hab in enumerate(self.hotel.habitaciones):
      fila = idx // 5
      col = idx % 5
      estado = "Disponible" if hab.disponible else "No disponible"
      color = "#d4edda" if hab.disponible else "#f8d7da"

      lbl = tk.Label(
          frame_grid,
          text=f"Hab. {hab.numero}\n${hab.precio_dia:,}\n{estado}",
          bg=color,
          relief="groove",
          width=11,
          height=4,
      )
      lbl.grid(row=fila, column=col, padx=4, pady=4)

    # Selección de habitación abajo (Pack layout)
    frame_sel = tk.Frame(win, pady=10)
    frame_sel.pack()

    tk.Label(frame_sel, text="Número de habitación a ocupar (1-10):").pack(
        side="left", padx=5
    )
    ent_num = tk.Entry(frame_sel, width=5)
    ent_num.pack(side="left", padx=5)

    def seleccionar():
      try:
        num = int(ent_num.get())
        hab = self.hotel.obtener_habitacion(num)
        if not hab:
          messagebox.showerror(
              "Error", "Ingrese un número entre 1 y 10.", parent=win
          )
        elif not hab.disponible:
          messagebox.showerror(
              "Error", f"La habitación {num} ya está ocupada.", parent=win
          )
        else:
          win.destroy()
          self.ventana_ingreso(hab)
      except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.", parent=win)

    tk.Button(frame_sel, text="Aceptar", command=seleccionar).pack(
        side="left", padx=5
    )

  # --- VENTANA DE INGRESO DE HUÉSPED ---
  def ventana_ingreso(self, habitacion):
    win = tk.Toplevel(self.root)
    win.title(f"Ingreso - Habitación {habitacion.numero}")
    win.geometry("340x240")
    win.grab_set()

    tk.Label(win, text="Fecha ingreso (AAAA-MM-DD):").grid(
        row=0, column=0, sticky="w", padx=10, pady=8
    )
    ent_fecha = tk.Entry(win)
    ent_fecha.insert(0, datetime.now().strftime("%Y-%m-%d"))
    ent_fecha.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(win, text="Nombre:").grid(
        row=1, column=0, sticky="w", padx=10, pady=8
    )
    ent_nombre = tk.Entry(win)
    ent_nombre.grid(row=1, column=1, padx=10, pady=8)

    tk.Label(win, text="Apellidos:").grid(
        row=2, column=0, sticky="w", padx=10, pady=8
    )
    ent_apellidos = tk.Entry(win)
    ent_apellidos.grid(row=2, column=1, padx=10, pady=8)

    tk.Label(win, text="Documento identidad:").grid(
        row=3, column=0, sticky="w", padx=10, pady=8
    )
    ent_doc = tk.Entry(win)
    ent_doc.grid(row=3, column=1, padx=10, pady=8)

    def registrar():
      fecha_txt = ent_fecha.get().strip()
      nombre = ent_nombre.get().strip()
      apellidos = ent_apellidos.get().strip()
      doc = ent_doc.get().strip()

      if not fecha_txt or not nombre or not apellidos or not doc:
        messagebox.showwarning(
            "Aviso", "Todos los campos son obligatorios.", parent=win
        )
        return

      try:
        fecha_ing = datetime.strptime(fecha_txt, "%Y-%m-%d").date()
      except ValueError:
        messagebox.showerror(
            "Error", "Formato de fecha inválido. Use AAAA-MM-DD.", parent=win
        )
        return

      huesped = Huesped(nombre, apellidos, doc, fecha_ing)
      habitacion.ocupar(huesped)
      messagebox.showinfo(
          "Éxito",
          f"Huésped registrado en la habitación {habitacion.numero}.",
          parent=win,
      )
      win.destroy()

    tk.Button(win, text="Registrar Ingreso", command=registrar, width=18).grid(
        row=4, column=0, columnspan=2, pady=15
    )

  # --- OPCIÓN 2: SALIDA DE HUÉSPEDES (BUSCAR HABITACIÓN) ---
  def ventana_salida_buscar(self):
    win = tk.Toplevel(self.root)
    win.title("Salida de Huéspedes")
    win.geometry("320x130")
    win.grab_set()

    tk.Label(win, text="Número de habitación a entregar (1-10):").pack(pady=10)
    ent_num = tk.Entry(win, width=10)
    ent_num.pack()

    def buscar():
      try:
        num = int(ent_num.get())
        hab = self.hotel.obtener_habitacion(num)
        if not hab:
          messagebox.showerror(
              "Error", "Número de habitación inválido (1-10).", parent=win
          )
        elif hab.disponible:
          messagebox.showerror(
              "Error",
              f"La habitación {num} no se encuentra ocupada.",
              parent=win,
          )
        else:
          win.destroy()
          self.ventana_salida_detalle(hab)
      except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.", parent=win)

    tk.Button(win, text="Aceptar", command=buscar).pack(pady=10)

  # --- VENTANA DETALLE Y CÁLCULO DE SALIDA ---
  def ventana_salida_detalle(self, habitacion):
    win = tk.Toplevel(self.root)
    win.title(f"Entrega Habitación {habitacion.numero}")
    win.geometry("360x280")
    win.grab_set()

    h = habitacion.huesped
    tk.Label(win, text=f"Huésped: {h.nombre} {h.apellidos}").pack(pady=4)
    tk.Label(win, text=f"Documento: {h.documento}").pack(pady=4)
    tk.Label(win, text=f"Fecha de ingreso: {h.fecha_ingreso}").pack(pady=4)

    frame_fecha = tk.Frame(win, pady=8)
    frame_fecha.pack()
    tk.Label(frame_fecha, text="Fecha salida (AAAA-MM-DD):").pack(side="left")
    ent_salida = tk.Entry(frame_fecha, width=12)
    ent_salida.pack(side="left", padx=5)

    lbl_resultado = tk.Label(win, text="", font=("Arial", 10, "bold"))
    lbl_resultado.pack(pady=8)

    btn_calcular = tk.Button(win, text="Calcular Total", state="disabled")
    btn_registrar = tk.Button(win, text="Registrar salida", state="disabled")

    def validar_fecha(*args):
      try:
        f_sal = datetime.strptime(ent_salida.get().strip(), "%Y-%m-%d").date()
        if f_sal > h.fecha_ingreso:
          btn_calcular.config(state="normal")
        else:
          btn_calcular.config(state="disabled")
          btn_registrar.config(state="disabled")
      except ValueError:
        btn_calcular.config(state="disabled")
        btn_registrar.config(state="disabled")

    ent_salida.bind("<KeyRelease>", validar_fecha)

    def calcular():
      f_sal = datetime.strptime(ent_salida.get().strip(), "%Y-%m-%d").date()
      dias, total = habitacion.calcular_pago(f_sal)
      lbl_resultado.config(
          text=f"Días alojado: {dias} | Total a pagar: ${total:,.0f}"
      )
      btn_registrar.config(state="normal")

    def confirmar_salida():
      habitacion.liberar()
      messagebox.showinfo(
          "Salida Exitosa",
          f"La habitación {habitacion.numero} ahora está disponible.",
          parent=win,
      )
      win.destroy()

    btn_calcular.config(command=calcular)
    btn_registrar.config(command=confirmar_salida)

    btn_calcular.pack(pady=4)
    btn_registrar.pack(pady=4)


if __name__ == "__main__":
  root = tk.Tk()
  app = InterfazHotel(root)
  root.mainloop()
