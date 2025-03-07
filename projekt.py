import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def sprawdz_stabilnosc(a, b, k):
    bieguny = np.roots([1, (a + b), (a * b) + k])
    return np.all(np.real(bieguny) < 0), bieguny

def symuluj_odpowiedz(k, a, b, t, sygnal_wejsciowy):
    licznik = [k]
    mianownik = [1, (a + b), (a * b) + k]
    uklad = signal.TransferFunction(licznik, mianownik)
    t_wyj, y_wyj, _ = signal.lsim(uklad, U=sygnal_wejsciowy, T=t)
    return t_wyj, y_wyj

def rysuj_uklad(canvas):
    canvas.create_rectangle(50, 50, 120, 100, fill="lightgray")
    canvas.create_text(85, 75, text="k")
    canvas.create_rectangle(180, 50, 280, 100, fill="lightgray")
    canvas.create_text(230, 75, text="A / (s + a)(s + b)")
    canvas.create_line(20, 75, 50, 75, arrow=tk.LAST)
    canvas.create_line(120, 75, 180, 75, arrow=tk.LAST)
    canvas.create_line(280, 75, 350, 75, arrow=tk.LAST)
    canvas.create_line(350, 75, 350, 120)
    canvas.create_line(350, 120, 20, 120)
    canvas.create_line(20, 120, 20, 75, arrow=tk.LAST)

def symulacja():
    k = float(entry_k.get())
    a = float(entry_a.get())
    b = float(entry_b.get())
    
    t = np.linspace(0, 10, 1000)
    skok = np.ones_like(t)
    sinusoida = np.sin(t)
    
    stabilny, bieguny = sprawdz_stabilnosc(a, b, k)
    label_stabilnosc.config(text=f"Bieguny: {bieguny}\n{'Stabilny' if stabilny else 'Niestabilny'}")
    
    t_skok, y_skok = symuluj_odpowiedz(k, a, b, t, skok)
    t_sin, y_sin = symuluj_odpowiedz(k, a, b, t, sinusoida)
    
    ax1.clear()
    ax1.plot(t_skok, skok, 'r--', label="Wejście (skok)")
    ax1.plot(t_skok, y_skok, label="Wyjście")
    ax1.set_title("Odpowiedź na skok")
    ax1.legend()
    
    ax2.clear()
    ax2.plot(t_sin, sinusoida, 'r--', label="Wejście (sinusoida)")
    ax2.plot(t_sin, y_sin, label="Wyjście")
    ax2.set_title("Odpowiedź na sinusoidę")
    ax2.legend()
    
    canvas_fig.draw()

root = tk.Tk()
root.title("Symulacja układu regulacji")

tk.Label(root, text="k:").grid(row=0, column=0)
entry_k = tk.Entry(root)
entry_k.grid(row=0, column=1)

tk.Label(root, text="a:").grid(row=1, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1)

tk.Label(root, text="b:").grid(row=2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1)

tk.Button(root, text="Symuluj", command=symulacja).grid(row=3, columnspan=2)
label_stabilnosc = tk.Label(root, text="")
label_stabilnosc.grid(row=4, columnspan=2)

canvas_uklad = tk.Canvas(root, width=400, height=150, bg="white")
canvas_uklad.grid(row=5, columnspan=2)
rysuj_uklad(canvas_uklad)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
canvas_fig = FigureCanvasTkAgg(fig, master=root)
canvas_fig.get_tk_widget().grid(row=6, columnspan=2)

root.mainloop()
