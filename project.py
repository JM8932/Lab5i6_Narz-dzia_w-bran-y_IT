import argparse
import sys
import json

def load_json(file_path):
    """Wczytuje i weryfikuje składnię pliku JSON."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"Pomyślnie wczytano plik JSON: {file_path}")
            return data
            
    except FileNotFoundError:
        print(f"Błąd krytyczny: Nie znaleziono pliku wejściowego '{file_path}'.")
        sys.exit(1)
        
    except json.JSONDecodeError as e:
        print(f"Błąd składni pliku JSON '{file_path}':")
        print(f"Szczegóły: {e}")
        sys.exit(1)
        
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas wczytywania pliku: {e}")
        sys.exit(1)


def save_json(data, file_path):
    """Zapisuje dane z obiektu do pliku JSON."""
    try:
        
        with open(file_path, 'w', encoding='utf-8') as file:
            
            json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"Pomyślnie zapisano dane do pliku JSON: {file_path}")
            
    except TypeError as e:
        print(f"Błąd: Dane nie mogą zostać zapisane do formatu JSON. Szczegóły: {e}")
        sys.exit(1)
        
    except IOError as e:
        print(f"Błąd krytyczny: Nie można zapisać do pliku '{file_path}'. Sprawdź ścieżkę i uprawnienia.")
        print(f"Szczegóły: {e}")
        sys.exit(1)
        
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas zapisywania pliku JSON: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Program do konwersji danych między formatami .xml, .json i .yml")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego")
    
    args = parser.parse_args()
    
    print(f"Rozpoczynam pracę programu...")
    
   
    dane_z_pliku = None
    
   
    if args.input_file.endswith('.json'):
        dane_z_pliku = load_json(args.input_file)
    else:
        print(f"Format pliku wejściowego '{args.input_file}' nie jest jeszcze obsługiwany.")
        sys.exit(1) 
        
   
    if args.output_file.endswith('.json'):
        save_json(dane_z_pliku, args.output_file)
    else:
        print(f"Format pliku wyjściowego '{args.output_file}' nie jest jeszcze obsługiwany w fazie zapisu.")

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
