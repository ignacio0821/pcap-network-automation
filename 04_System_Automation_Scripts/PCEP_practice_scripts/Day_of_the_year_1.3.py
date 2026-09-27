def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    if 1 <= month <= 12:
        return month_days[month]
    return None

def is_date_valid(year, month, day):
    if year < 1 or month < 1 or month > 12:
        return False

    max_days = days_in_month(year, month)

    if 1 <= day <= max_days:
        return True

    return False

def day_of_the_year(year, month, day):
    try:
        if not is_date_valid(year, month, day):
            print(f"[!] Invalid Date: {year}--{month}--{day}")
            return None

        total_days = day
        for m in range(1, month):
            total_days += days_in_month(year, m)
        return total_days

    except TypeError:
        print("[!] Error: Please ensure year, month and day are integers")
    except ZeroDivisionError as e:
        print(f"[!] Error: --{e}--")
    except Exception as e:
        print(f"[!] An Unexpected error occurred: {e}")
    finally:
        print(f" [!]Alert:\n")

print(day_of_the_year(1917, 10, 29))
print(day_of_the_year(1415, 11, 11))
print(day_of_the_year("2000", 1, 1))


#if __name__ == "__main__":
   # day_of_the_year()




































