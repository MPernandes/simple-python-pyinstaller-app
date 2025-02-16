import sys
import argparse
import calc

def main():
    parser = argparse.ArgumentParser(description="Menjumlahkan dua angka.")
    parser.add_argument("X", type=float, help="Angka pertama")
    parser.add_argument("Y", type=float, help="Angka kedua")

    args = parser.parse_args()

    result = calc.add2(args.X, args.Y)
    print(f"\nThe result is {result}\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nError: {e}\n")
        sys.exit(1)

