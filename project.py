import argparse
import sys

def main():
    
    parser = argparse.ArgumentParser(description="Program do konwersji danych między formatami .xml, .json i .yml")
    
    
    parser.add_argument("input_file", help="Ścieżka do pliku wejściowego (np. pathFile1.json)")
    parser.add_argument("output_file", help="Ścieżka do pliku wyjściowego (np. pathFile2.xml)")
    
  
    args = parser.parse_args()
    
   
    print(f"Uruchomiono program...")
    print(f"Plik wejściowy do wczytania: {args.input_file}")
    print(f"Plik wyjściowy do zapisania: {args.output_file}")

if __name__ == "__main__":
    main()
