
def amr_xmas(year):
    christmas_day = date(year=year, month=12, day=25)
    days_til_christmas = (christmas_day - date.today()).days
    return days_til_christmas


print(amr_xmas(2022))