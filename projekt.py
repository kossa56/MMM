import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

def check_stability(a, b, k):
    poles = np.roots([1, (a + b), (a * b) + k])
    return np.all(np.real(poles) < 0), poles

def simulate_response(k, a, b, t, input_signal):
    num = [k]
    den = [1, (a + b), (a * b) + k]
    system = signal.TransferFunction(num, den)
    t_out, y_out, _ = signal.lsim(system, U=input_signal, T=t)
    return t_out, y_out

def main():
    k = float(input("Podaj wartość k: "))
    a = float(input("Podaj wartość a: "))
    b = float(input("Podaj wartość b: "))
    
    t = np.linspace(0, 10, 1000)  # Zakres czasu symulacji
    step_input = np.ones_like(t)  # Skok jednostkowy
    sine_input = np.sin(t)  # Sinusoida
    
    stable, poles = check_stability(a, b, k)
    print(f"Bieguny układu: {poles}")
    print("Układ jest stabilny." if stable else "Układ jest niestabilny!")
    
    # Symulacja dla pobudzenia skokowego
    t_step, y_step = simulate_response(k, a, b, t, step_input)
    
    # Symulacja dla pobudzenia sinusoidalnego
    t_sine, y_sine = simulate_response(k, a, b, t, sine_input)
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t_step, step_input, 'r--', label="Wejście (skok)")
    plt.plot(t_step, y_step, label="Wyjście")
    plt.title("Odpowiedź na skok jednostkowy")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(t_sine, sine_input, 'r--', label="Wejście (sinusoida)")
    plt.plot(t_sine, y_sine, label="Wyjście")
    plt.title("Odpowiedź na sinusoidę")
    plt.xlabel("Czas [s]")
    plt.ylabel("Amplituda")
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()
