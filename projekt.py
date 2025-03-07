import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

def sprawdz_stabilnosc(a, b, k):
    bieguny = np.roots([1, (a + b), (a * b) + k])
    return np.all(np.real(bieguny) < 0), bieguny

def symuluj_odpowiedz(k, a, b, t, sygnal_wejsciowy):
    licznik = [k]
    mianownik = [1, (a + b), (a * b) + k]
    uklad = signal.TransferFunction(licznik, mianownik)
    t_wyj, y_wyj, _ = signal.lsim(uklad, U=sygnal_wejsciowy, T=t)
    return t_wyj, y_wyj

def main():
    k = float(input("Podaj wartość k: "))
    a = float(input("Podaj wartość a: "))
    b = float(input("Podaj wartość b: "))
    
    t = np.linspace(0, 10, 1000)  # Zakres czasu symulacji
    skok = np.ones_like(t)  # Skok jednostkowy
    sinusoida = np.sin(t)  # Sinusoida
    
    stabilny, bieguny = sprawdz_stabilnosc(a, b, k)
    print(f"Bieguny układu: {bieguny}")
    print("Układ jest stabilny." if stabilny else "Układ jest niestabilny!")
    
    # Symulacja dla pobudzenia skokowego
    t_skok, y_skok = symuluj_odpowiedz(k, a, b, t, skok)
    
    # Symulacja dla pobudzenia sinusoidalnego
    t_sin, y_sin = symuluj_odpowiedz(k, a, b, t, sinusoida)
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t_skok, skok, 'r--', label="Wejście (skok)")
    plt.plot(t_skok, y_skok, label="Wyjście")
    plt.title("Odpowiedź na skok jednostkowy")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(t_sin, sinusoida, 'r--', label="Wejście (sinusoida)")
    plt.plot(t_sin, y_sin, label="Wyjście")
    plt.title("Odpowiedź na sinusoidę")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()
