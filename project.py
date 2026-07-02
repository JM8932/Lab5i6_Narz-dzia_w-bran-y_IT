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

def main():
    parser = argparse.ArgumentParser(description="Program do konwersji danych między formatami .xml, .json i .yml")
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego (np. pathFile1.json)")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego (np. pathFile2.xml)")
    
    args = parser.parse_args()
    
    print(f"Rozpoczynam pracę programu...")
    
  
    if args.input_file.endswith('.json'):
        dane_z_pliku = load_json(args.input_file)
        
        print(f"Wczytano dane jako obiekt typu: {type(dane_z_pliku)}")
    else:
        print(f"Plik '{args.input_file}' nie jest plikiem .json. Na razie obsługujemy tylko format JSON (Task 2).")

if __name__ == "__main__":
    main()
