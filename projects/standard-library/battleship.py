import tkinter as tk
from tkinter import messagebox
import random, json

class BatallaNaval:
    VACIA, BARCO, IMPACTO, AGUA = " ", "B", "X", "O"
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Batalla Naval")
        self.tamano, self.barcos, self.dificultad = 5, 3, "Facil"
        self.jugador = self.sentinel = []
        self.menu_principal()

    def limpiar(self):
        [w.destroy() for w in self.window.winfo_children()]

    def label(self, txt, size=14, **kw):
        return tk.Label(self.window, text=txt, font=("Arial", size), **kw)

    def boton(self, txt, cmd, size=14, **kw):
        return tk.Button(self.window, text=txt, font=("Arial", size), command=cmd, **kw)

    def menu_principal(self):
        self.limpiar()
        self.label("Batalla Naval", 20).pack(pady=20)
        for txt, cmd in [("Iniciar", self.configurar), ("Cargar", self.cargar), ("Salir", self.window.quit)]:
            self.boton(txt, cmd).pack(pady=10)

    def configurar(self):
        self.limpiar()
        self.label("Configurar Juego", 18).pack(pady=10)
        self.tam_var, self.dif_var, self.bar_var = tk.IntVar(value=5), tk.StringVar(value="Facil"), tk.IntVar(value=3)
        for lbl, var, opts in [("Tamaño:", self.tam_var, [5,7,10]), ("Dificultad:", self.dif_var, ["Facil","Dificil"])]:
            self.label(lbl).pack(pady=5)
            tk.OptionMenu(self.window, var, *opts).pack()
        self.label("Barcos:").pack(pady=5)
        tk.Spinbox(self.window, from_=1, to=10, textvariable=self.bar_var).pack()
        self.boton("Iniciar", self.iniciar).pack(pady=20)

    def tablero_vacio(self):
        return [[self.VACIA]*self.tamano for _ in range(self.tamano)]

    def colocar(self, t):
        for x, y in random.sample([(i,j) for i in range(self.tamano) for j in range(self.tamano)], self.barcos):
            t[x][y] = self.BARCO

    def iniciar(self):
        self.tamano, self.barcos = self.tam_var.get(), min(self.bar_var.get(), self.tam_var.get()**2//2)
        self.dificultad = self.dif_var.get()
        self.jugador, self.sentinel = self.tablero_vacio(), self.tablero_vacio()
        self.colocar(self.jugador); self.colocar(self.sentinel)
        self.mostrar()

    def mostrar(self):
        self.limpiar()
        self.label("Tu Tablero", 16).grid(row=0, column=0, columnspan=self.tamano, padx=10)
        self.label("Sentinel", 16).grid(row=0, column=self.tamano+1, columnspan=self.tamano, padx=10)
        for i in range(self.tamano):
            for j in range(self.tamano):
                tk.Label(self.window, text=self.jugador[i][j], font=("Arial",14), width=2, borderwidth=1, relief="solid").grid(row=i+1, column=j)
                c = self.sentinel[i][j]
                txt, st = (c, "disabled") if c in (self.IMPACTO, self.AGUA) else ("?", "normal")
                tk.Button(self.window, text=txt, font=("Arial",14), width=2, state=st, command=lambda x=i,y=j: self.disparar(x,y)).grid(row=i+1, column=j+self.tamano+1)
        self.boton("Guardar", self.guardar).grid(row=self.tamano+2, column=0, columnspan=self.tamano*2+1, pady=10)
        self.verificar_fin()

    def contar(self, t):
        return sum(r.count(self.BARCO) for r in t)

    def verificar_fin(self):
        if self.contar(self.sentinel) == 0:
            messagebox.showinfo("Victoria", "¡Ganaste!"); self.menu_principal()
        elif self.contar(self.jugador) == 0:
            messagebox.showinfo("Derrota", "Perdiste"); self.menu_principal()

    def disparar(self, x, y):
        if self.sentinel[x][y] in (self.IMPACTO, self.AGUA): return
        hit = self.sentinel[x][y] == self.BARCO
        messagebox.showinfo("Resultado", "¡Impacto!" if hit else "Agua")
        self.sentinel[x][y] = self.IMPACTO if hit else self.AGUA
        self.turno_sentinel()

    def turno_sentinel(self):
        disp = [(i,j) for i in range(self.tamano) for j in range(self.tamano) if self.jugador[i][j] in (self.VACIA, self.BARCO)]
        if not disp: return self.mostrar()
        obj = None
        if self.dificultad == "Dificil":
            for i in range(self.tamano):
                for j in range(self.tamano):
                    if self.jugador[i][j] == self.IMPACTO:
                        for dx,dy in self.DIRS:
                            nx, ny = i+dx, j+dy
                            if 0<=nx<self.tamano and 0<=ny<self.tamano and self.jugador[nx][ny] in (self.VACIA, self.BARCO):
                                obj = (nx, ny); break
                    if obj: break
                if obj: break
        x, y = obj or random.choice(disp)
        if self.jugador[x][y] == self.BARCO:
            messagebox.showinfo("Sentinel", f"Impacto en ({x},{y})")
        self.jugador[x][y] = self.IMPACTO if self.jugador[x][y] == self.BARCO else self.AGUA
        self.mostrar()

    def guardar(self):
        try:
            with open("batalla_naval.json", "w") as f:
                json.dump({"t": self.tamano, "b": self.barcos, "d": self.dificultad, "j": self.jugador, "s": self.sentinel}, f)
            messagebox.showinfo("OK", "Guardado")
        except IOError as e:
            messagebox.showerror("Error", str(e))

    def cargar(self):
        try:
            with open("batalla_naval.json") as f:
                p = json.load(f)
            self.tamano, self.barcos, self.dificultad = p["t"], p["b"], p["d"]
            self.jugador, self.sentinel = p["j"], p["s"]
            self.mostrar()
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    BatallaNaval().run()