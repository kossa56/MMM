# Symulacja Układu Zamkniętego z Regulacją P

## Opis Projektu
Ten projekt implementuje symulację zamkniętego układu regulacji z regulatorem proporcjonalnym (P). Układ przedstawiony jest w postaci schematu blokowego i pozwala na analizę dynamiki systemu w odpowiedzi na różne typy pobudzenia.

### Funkcjonalności programu:
- **Definiowanie parametrów układu**: Możliwość ręcznego ustawienia wartości `k`, `a`, `b`.
- **Sprawdzanie stabilności systemu**: Analiza biegunów funkcji przejścia i określenie, czy system jest stabilny.
- **Symulacja odpowiedzi systemu**: Obliczanie i wizualizacja odpowiedzi układu na pobudzenie:
  - Skok jednostkowy
  - Sinusoida
- **Generowanie wykresów**: Graficzna prezentacja wejścia i wyjścia systemu w czasie.

## Wymagania
Projekt wymaga następujących bibliotek Pythona:
- `numpy` - do obliczeń numerycznych
- `matplotlib` - do wizualizacji wyników
- `scipy` - do analizy systemów dynamicznych

Aby zainstalować brakujące biblioteki, uruchom komendę:
```bash
pip install numpy matplotlib scipy
```

## Uruchomienie programu
Aby uruchomić symulację, wykonaj skrypt Python:
```bash
python nazwa_pliku.py
```
Po uruchomieniu użytkownik zostanie poproszony o podanie wartości parametrów `k`, `a`, `b`.

## Opis działania
1. **Wprowadzenie parametrów**
   - Program prosi użytkownika o podanie wartości `k`, `a`, `b`, które definiują układ.
2. **Sprawdzanie stabilności układu**
   - Bieguny funkcji przejścia są obliczane i analizowane. Jeśli wszystkie mają ujemną część rzeczywistą, system jest stabilny.
3. **Symulacja odpowiedzi układu**
   - Program generuje odpowiedź układu na pobudzenie skokowe oraz sinusoidalne.
4. **Wizualizacja wyników**
   - Wyniki są przedstawiane na dwóch wykresach:
     - Odpowiedź na skok jednostkowy
     - Odpowiedź na sinusoidę

## Przykładowe wartości wejściowe
```
Podaj wartość k: 2
Podaj wartość a: 1
Podaj wartość b: 3
```
**Przykładowa interpretacja wyników:**
- Jeśli bieguny mają części rzeczywiste ujemne, układ jest stabilny.
- Jeśli układ wykazuje oscylacje bez tłumienia lub narastające wartości wyjścia, układ jest niestabilny.

## Możliwe rozszerzenia projektu
- Dodanie różnych typów pobudzeń (np. impuls, rampa)
- Implementacja interfejsu graficznego do wprowadzania parametrów
- Eksport wyników do pliku CSV lub PDF




