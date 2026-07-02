import argparse
import sys
import json
import yaml 

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"Pomyślnie wczytano plik JSON: {file_path}")
            return data
    except FileNotFoundError:
        print(f"Błąd krytyczny: Nie znaleziono pliku wejściowego '{file_path}'.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Błąd składni pliku JSON '{file_path}':\nSzczegóły: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas wczytywania pliku: {e}")
        sys.exit(1)

def save_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"Pomyślnie zapisano dane do pliku JSON: {file_path}")
    except TypeError as e:
        print(f"Błąd: Dane nie mogą zostać zapisane do formatu JSON. Szczegóły: {e}")
        sys.exit(1)
    except IOError as e:
        print(f"Błąd krytyczny: Nie można zapisać do pliku '{file_path}'.\nSzczegóły: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas zapisywania JSON: {e}")
        sys.exit(1)



def load_yml(file_path):
    """Wczytuje i weryfikuje składnię pliku YAML."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            
            data = yaml.safe_load(file)
            print(f"Pomyślnie wczytano plik YAML: {file_path}")
            return data
            
    except FileNotFoundError:
        print(f"Błąd krytyczny: Nie znaleziono pliku wejściowego '{file_path}'.")
        sys.exit(1)
        
    except yaml.YAMLError as e:
        print(f"Błąd składni pliku YAML '{file_path}':\nSzczegóły: {e}")
        sys.exit(1)
        
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd podczas wczytywania pliku YAML: {e}")
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
    
    elif args.input_file.endswith('.yml') or args.input_file.endswith('.yaml'):
        dane_z_pliku = load_yml(args.input_file)
    else:
        print(f"Format pliku wejściowego '{args.input_file}' nie jest obsługiwany.")
        sys.exit(1)
        
    
    if args.output_file.endswith('.json'):
        save_json(dane_z_pliku, args.output_file)
    else:
        print(f"Format pliku wyjściowego '{args.output_file}' nie jest jeszcze obsługiwany w fazie zapisu.")

if __name__ == "__main__":
    main()
