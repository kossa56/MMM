import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def sprawdz_stabilnosc(a, b, k, A):
    bieguny = np.roots([A, (a + b), (a * b) + k])
    return np.all(np.real(bieguny) < 0), bieguny

def symuluj_odpowiedz(k, a, b, t, sygnal_wejsciowy, A):
    licznik = [A * k]  # Uwzględniamy A w liczniku
    mianownik = [1, (a + b), (a * b) + k]
    uklad = signal.TransferFunction(licznik, mianownik)
    t_wyj, y_wyj, _ = signal.lsim(uklad, U=sygnal_wejsciowy, T=t)
    return t_wyj, y_wyj

def rysuj_uklad(canvas):
    canvas.delete("all")
    canvas.configure(bg="white")
    
    # Bloki
    canvas.create_rectangle(50, 50, 150, 100, fill="lightgray", outline="black", width=2)
    canvas.create_text(100, 75, text="k", font=("Arial", 14, "bold"), fill="black")
    canvas.create_rectangle(200, 50, 350, 100, fill="lightgray", outline="black", width=2)
    canvas.create_text(275, 75, text="A / (s + a)(s + b)", font=("Arial", 14, "bold"), fill="black")
    
    # Linie połączeń
    canvas.create_line(30, 75, 50, 75, arrow="last", fill="black", width=2)
    canvas.create_line(150, 75, 200, 75, arrow="last", fill="black", width=2)
    canvas.create_line(350, 75, 400, 75, arrow="last", fill="black", width=2)
    
    # Sprzężenie zwrotne
    canvas.create_line(400, 75, 400, 130, fill="black", width=2)
    canvas.create_line(400, 130, 30, 130, fill="black", width=2)
    canvas.create_line(30, 130, 30, 75, arrow="last", fill="black", width=2)
    
    # Opisy wejścia i wyjścia
    canvas.create_text(2, 75, text="u(t)", font=("Arial", 12), fill="black", anchor="w")
    canvas.create_text(410, 75, text="y(t)", font=("Arial", 12), fill="black", anchor="w")

def symuluj_i_rysuj():
    try:
        k = float(entry_k.get())
        a = float(entry_a.get())
        b = float(entry_b.get())
        A = float(entry_A.get())  # Dodanie parametru A

        t = np.linspace(0, 10, 1000)
        if sygnal_var.get() == "Skok jednostkowy":
            sygnal_wejsciowy = np.heaviside(t, 1)
            sygnal_wejsciowy[0] = 0  # Początek układu współrzędnych widoczny
        else:
            sygnal_wejsciowy = np.sin(t)

        stabilny, bieguny = sprawdz_stabilnosc(a, b, k, A)  # Przekazanie parametru A
        t_wyj, y_wyj = symuluj_odpowiedz(k, a, b, t, sygnal_wejsciowy, A)  # Przekazanie parametru A

        ax1.clear()
        ax2.clear()

        ax1.plot(t, sygnal_wejsciowy, label="Sygnał pobudzający", color='blue')
        ax1.set_title("Sygnał pobudzający")
        ax1.set_xlabel("Czas [s]")
        ax1.set_ylabel("u(t)")
        ax1.set_xlim([-0.09, 10])
        ax1.set_ylim([min(sygnal_wejsciowy), max(sygnal_wejsciowy) + 0.1])
        ax1.grid()

        ax2.plot(t_wyj, y_wyj, label="Odpowiedź układu", color='red')
        ax2.set_title("Odpowiedź układu")
        ax2.set_xlabel("Czas [s]")
        ax2.set_ylabel("y(t)")
        ax2.set_xlim([0, 10])
        ax2.set_ylim([min(y_wyj) - 0.1, max(y_wyj) + 0.1])
        ax2.grid()

        canvas_fig.draw()

        # Dodanie aktualizacji GUI
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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))
canvas_fig = FigureCanvasTkAgg(fig, master=frame)
canvas_fig.get_tk_widget().pack()

root.mainloop()
