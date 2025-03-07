# Symulacja Układu Regulacji

## Opis Projektu

Jest to aplikacja w języku Python umożliwiająca symulację odpowiedzi układu regulacji zamkniętego z regulatorem proporcjonalnym (P). Program pozwala na:
- Definiowanie parametrów układu: wzmocnienia regulatora `k` oraz parametrów `a` i `b` wpływających na charakterystykę układu.
- Sprawdzenie stabilności układu poprzez analizę biegunów transmitancji.
- Symulację odpowiedzi układu na pobudzenie skokowe oraz sinusoidalne.
- Wizualizację schematu blokowego układu regulacji.
- Wyświetlanie wykresów pokazujących zachowanie układu w czasie.


## Wymagania

Do uruchomienia aplikacji wymagane są następujące biblioteki:

- `numpy` – do obliczeń numerycznych,
- `matplotlib` – do wizualizacji danych,
- `scipy` – do analizy układu dynamicznego,
- `tkinter` – do stworzenia interfejsu graficznego (wbudowane w Pythona).

Można je zainstalować za pomocą polecenia:
```bash
pip install numpy matplotlib scipy
```

## Uruchomienie Programu

Aby uruchomić program, należy wykonać w terminalu:
```bash
python nazwa_pliku.py
```

## Obsługa Programu

1. Uruchom aplikację.
2. Wprowadź wartości parametrów `k`, `a`, `b` w odpowiednich polach formularza.
3. Kliknij przycisk "Symuluj".
4. Program sprawdzi stabilność układu i wyświetli bieguny oraz ich wartości.
5. Na podstawie wprowadzonych parametrów program narysuje schemat blokowy układu.
6. Wykresy odpowiedzi układu na pobudzenie skokowe i sinusoidalne zostaną wygenerowane i wyświetlone w interfejsie użytkownika.
7. Jeśli układ jest niestabilny, program poinformuje o tym użytkownika.

## Struktura Kodu

- `sprawdz_stabilnosc(a, b, k)`: Funkcja sprawdzająca stabilność układu poprzez analizę biegunów transmitancji zamkniętej.
- `symuluj_odpowiedz(k, a, b, t, sygnal_wejsciowy)`: Funkcja obliczająca odpowiedź układu na zadane pobudzenie, wykorzystując metody analizy układów dynamicznych.
- `rysuj_uklad(canvas)`: Funkcja odpowiedzialna za graficzne przedstawienie schematu blokowego układu regulacji.
- `symulacja()`: Główna funkcja programu, pobierająca wartości parametrów od użytkownika, sprawdzająca stabilność układu oraz generująca wykresy odpowiedzi dynamicznej.

## Wizualizacja

Po uruchomieniu programu użytkownik zobaczy okno z formularzem, w którym można wprowadzić wartości parametrów układu. Po kliknięciu "Symuluj" pojawi się schemat blokowy układu oraz dwa wykresy przedstawiające odpowiedź układu na pobudzenie skokowe oraz sinusoidalne. Jeśli układ jest stabilny, wykresy pokażą tłumioną odpowiedź. Jeśli układ jest niestabilny, wartości będą rosły do nieskończoności.

## Przykłady Użycia

### Przykład 1: Stabilny Układ
**Dane wejściowe:**
```
k = 5
a = 2
b = 3
```
**Oczekiwany wynik:**
- Bieguny układu mają części rzeczywiste ujemne → układ stabilny.
- Odpowiedź układu na pobudzenie skokowe dąży do wartości ustalonej.
- Odpowiedź układu na pobudzenie sinusoidalne wykazuje tłumienie drgań.

### Przykład 2: Niestabilny Układ
**Dane wejściowe:**
```
k = -5
a = -2
b = -3
```
**Oczekiwany wynik:**
- Bieguny układu mają części rzeczywiste dodatnie → układ niestabilny.
- Odpowiedź układu na pobudzenie skokowe rośnie do nieskończoności.
- Odpowiedź układu na pobudzenie sinusoidalne wykazuje narastające oscylacje.

## Możliwe Rozszerzenia

- Dodanie dodatkowych typów pobudzeń (np. impuls Diraca, szum losowy).
- Implementacja możliwości zapisu wyników do pliku CSV.
- Rozszerzenie interfejsu użytkownika o bardziej zaawansowane opcje analizy systemu.



