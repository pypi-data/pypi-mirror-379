import sys
from .core import get_day_of_week

def main():
    if len(sys.argv) < 2:
        print("Usage: DayOfWeekLib <date> [format]")
        print("Default format: YYYY-MM-DD")
        return
    date_str = sys.argv[1]
    date_format = sys.argv[2] if len(sys.argv) > 2 else "%Y-%m-%d"
    day = get_day_of_week(date_str, date_format)
    print(f"Day of week: {day}")

if __name__ == "__main__":
    main()
