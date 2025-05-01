import numpy as np
import matplotlib.pyplot as plt
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from control import tf, root_locus

def sprawdz_stabilnosc(a, b, k, A):
    bieguny = np.roots([A, (a + b), (a * b) + k])
    return np.all(np.real(bieguny) < 0), bieguny

def symuluj_odpowiedz(k, a, b, t, sygnal_wejsciowy, A):
    # Parametry równania różniczkowego
    # y''(t) + (a+b)y'(t) + (a*b + k)y(t) = A*k*u(t)
    # Przekształcone do postaci:
    # y''(t) = - (a+b)y'(t) - (a*b + k)y(t) + A*k*u(t)
    
    n = len(t)
    h = t[1] - t[0]  # krok czasowy
    
    # Inicjalizacja zmiennych
    y = np.zeros(n)
    y_p = np.zeros(n)  # pierwsza pochodna
    y_pp = np.zeros(n)  # druga pochodna
    
    # Warunki początkowe
    y[0] = 0
    y_p[0] = 0
    y_pp[0] = - (a + b) * y_p[0] - (a * b + k) * y[0] + A * k * sygnal_wejsciowy[0]
    
    # Metoda Taylora (zgodnie z MMM-pomoc)
    for i in range(n - 1):
        # Obliczenie drugiej pochodnej w chwili i
        y_pp[i] = - (a + b) * y_p[i] - (a * b + k) * y[i] + A * k * sygnal_wejsciowy[i]
        
        # Obliczenie pierwszej pochodnej w chwili i+1
        y_p[i+1] = y_p[i] + h * y_pp[i]
        
        # Obliczenie y w chwili i+1
        y[i+1] = y[i] + h * y_p[i] + (h**2 / 2) * y_pp[i]
    
    return t, y

def rysuj_linie_pierwiastkowe(a, b, A, ax):
    licznik = [A]
    mianownik = [1, (a + b), (a * b)]
    system = tf(licznik, mianownik)
    
    ax.clear()
    root_locus(system, plot=True, grid=True, ax=ax)
    
    x_min, x_max = -10, 10
    y_min, y_max = -10, 10
    
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    ax.set_title("Linie pierwiastkowe")
    ax.set_xlabel("Część rzeczywista")
    ax.set_ylabel("Część urojona")
    ax.grid(True)
    
    ax.plot([x_max], [0], '>k', markersize=5, clip_on=False)
    ax.plot([0], [y_max], '^k', markersize=5, clip_on=False)

def rysuj_uklad(canvas):
    canvas.delete("all")
    canvas.configure(bg="white")
    
    canvas.create_rectangle(50, 50, 150, 100, fill="lightgray", outline="black", width=2)
    canvas.create_text(100, 75, text="k", font=("Arial", 14, "bold"), fill="black")
    canvas.create_rectangle(200, 50, 350, 100, fill="lightgray", outline="black", width=2)
    canvas.create_text(275, 75, text="A / (s + a)(s + b)", font=("Arial", 14, "bold"), fill="black")
    
    canvas.create_line(30, 75, 50, 75, arrow="last", fill="black", width=2)
    canvas.create_line(150, 75, 200, 75, arrow="last", fill="black", width=2)
    canvas.create_line(350, 75, 400, 75, arrow="last", fill="black", width=2)
    
    canvas.create_line(400, 75, 400, 130, fill="black", width=2)
    canvas.create_line(400, 130, 30, 130, fill="black", width=2)
    canvas.create_line(30, 130, 30, 75, arrow="last", fill="black", width=2)
    
    canvas.create_text(2, 75, text="u(t)", font=("Arial", 12), fill="black", anchor="w")
    canvas.create_text(410, 75, text="y(t)", font=("Arial", 12), fill="black", anchor="w")

def symuluj_i_rysuj():
    try:
        k = float(entry_k.get())
        a = float(entry_a.get())
        b = float(entry_b.get())
        A = float(entry_A.get())

        t = np.linspace(0, 10, 1000)
        if sygnal_var.get() == "Skok jednostkowy":
            sygnal_wejsciowy = np.heaviside(t, 1)
            sygnal_wejsciowy[0] = 0
        else:
            sygnal_wejsciowy = np.sin(t)

        stabilny, bieguny = sprawdz_stabilnosc(a, b, k, A)
        t_wyj, y_wyj = symuluj_odpowiedz(k, a, b, t, sygnal_wejsciowy, A)

        ax1.clear()
        ax2.clear()
        ax3.clear()

        ax1.plot(t, sygnal_wejsciowy, label="Sygnał pobudzający", color='blue')
        ax1.set_title("Sygnał pobudzający")
        ax1.set_xlabel("Czas [s]")
        ax1.set_ylabel("u(t)")
        ax1.set_xlim([-0.5, 10.5])
        ax1.set_ylim([min(sygnal_wejsciowy)-0.5, max(sygnal_wejsciowy)+0.5])
        ax1.grid(True)
        ax1.axhline(0, color='black', linewidth=0.5)
        ax1.axvline(0, color='black', linewidth=0.5)

        ax2.plot(t_wyj, y_wyj, label="Odpowiedź układu", color='red')
        ax2.set_title("Odpowiedź układu")
        ax2.set_xlabel("Czas [s]")
        ax2.set_ylabel("y(t)")
        ax2.set_xlim([-0.5, 10.5])
        ax2.set_ylim([min(y_wyj)-0.5, max(y_wyj)+0.5])
        ax2.grid(True)
        ax2.axhline(0, color='black', linewidth=0.5)
        ax2.axvline(0, color='black', linewidth=0.5)

        rysuj_linie_pierwiastkowe(a, b, A, ax3)

        plt.tight_layout()
        canvas_fig.draw()

        root.update()

        if stabilny:
            label_stabilnosc.configure(text="Układ stabilny", text_color="green")
        else:
            label_stabilnosc.configure(text="Układ niestabilny", text_color="red")
    except ValueError:
        label_stabilnosc.configure(text="Błąd: Wprowadź poprawne wartości liczbowe", text_color="red")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Symulacja układu regulacji")
root.geometry("1280x720")

canvas_uklad = ctk.CTkCanvas(root, width=450, height=150, bg="white")
canvas_uklad.pack(pady=10)
rysuj_uklad(canvas_uklad)

frame = ctk.CTkFrame(root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

ctk.CTkLabel(frame, text="A:").pack()  
entry_A = ctk.CTkEntry(frame)  
entry_A.pack()

ctk.CTkLabel(frame, text="k:").pack()
entry_k = ctk.CTkEntry(frame)
entry_k.pack()

ctk.CTkLabel(frame, text="a:").pack()
entry_a = ctk.CTkEntry(frame)
entry_a.pack()

ctk.CTkLabel(frame, text="b:").pack()
entry_b = ctk.CTkEntry(frame)
entry_b.pack()

sygnal_var = ctk.StringVar(value="Skok jednostkowy")
ctk.CTkLabel(frame, text="Wybierz sygnał pobudzający:").pack()
sygnal_menu = ctk.CTkOptionMenu(frame, variable=sygnal_var, values=["Skok jednostkowy", "Sinusoida"])
sygnal_menu.pack()

przycisk_symuluj = ctk.CTkButton(frame, text="Symuluj", command=symuluj_i_rysuj)
przycisk_symuluj.pack(pady=10)

label_stabilnosc = ctk.CTkLabel(frame, text="")
label_stabilnosc.pack()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
canvas_fig = FigureCanvasTkAgg(fig, master=frame)
canvas_fig.get_tk_widget().pack()

root.mainloop()
