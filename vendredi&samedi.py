import calendar
import datetime

def get_fridays_and_saturdays(start_date, end_date):
    fridays_and_saturdays = []
    current_date = start_date
    while current_date <= end_date:
        if calendar.weekday(current_date.year, current_date.month, current_date.day) in [4, 5]:
            fridays_and_saturdays.append(current_date.strftime('%Y-%m-%d'))
        if current_date.day == calendar.monthrange(current_date.year, current_date.month)[1]:
            current_year, current_month = current_date.year + (current_date.month == 12), current_date.month % 12 + 1
            current_date = datetime.date(current_year, current_month, 1)
        else:
            current_date += datetime.timedelta(days=1)
    return fridays_and_saturdays

today = datetime.date.today()
end_date = datetime.date(2024, 4, 8)
fridays_and_saturdays = get_fridays_and_saturdays(today, end_date)

with open('./cache/vendredi&samedi.txt', 'w') as f:
    for date in fridays_and_saturdays:
        f.write(f'{date}\n')
