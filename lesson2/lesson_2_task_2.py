def is_year_leap(year):
    return f'год {year} вискокосный?: {year % 4 == 0}'
print(is_year_leap(2020))
print(is_year_leap(2021))
print(is_year_leap(2024))