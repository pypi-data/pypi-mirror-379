import sys
from .core import calculate_age 

def main():
    if len(sys.argv) < 2:
        print("Usage: AgeCalculatorLib <birth_date> [format]")
        print("Default format: YYYY-MM-DD")
        return
    birth_date_str = sys.argv[1]
    date_format = sys.argv[2] if len(sys.argv) > 2 else "%Y-%m-%d"
    age = calculate_age(birth_date_str, date_format)
    print(f"Age: {age} years") 

if __name__ == "__main__":
    main() 
