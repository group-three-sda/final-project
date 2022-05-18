import datetime
from .forms import GoToForm


def get_today():
    now = datetime.datetime.now()
    return now


def get_monday(date=get_today()):
    monday = date - datetime.timedelta(days=date.weekday())
    formatted_monday = datetime.datetime.strptime(monday.strftime("%Y-%m-%d"), "%Y-%m-%d")
    year = int(formatted_monday.year)
    month = int(formatted_monday.month)
    day = int(formatted_monday.day)
    monday = datetime.date(year, month, day)
    return monday


def get_week_number(date=get_monday()):
    week_number = datetime.date.isocalendar(get_monday(date))[1]
    return week_number


def get_days_of_week(monday=get_monday()):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    year = int(monday.year)
    month = int(monday.month)
    day = int(monday.day)
    counter = 0
    days_of_week: dict[str, datetime] = {}
    for day_name in week:
        delta = datetime.timedelta(days=counter)
        date = datetime.date(year, month, day) + delta
        pair = {f"{day_name}": date.strftime("%d-%m")}
        counter += 1
        days_of_week.update(pair)
    return days_of_week


def get_time_slots():
    start_time = datetime.time(7, 00)
    end_time = datetime.time(16, 00)
    unit = start_time
    my_slots: list[datetime.time] = []
    while unit <= end_time:
        yield unit.strftime('%H:%M')
        unit = (datetime.datetime.combine(datetime.date.today(), unit) + datetime.timedelta(minutes=30)).time()
        my_slots.append(unit)
    return my_slots


def generate_content(date):
    WEEK_RANGE = 7
    TIMESLOTS = list(get_time_slots())
    form = GoToForm()
    monday = get_monday(date)
    days_of_week = get_days_of_week(monday)
    week_number = get_week_number(monday)
    year = monday.year
    extra_context = {
        'form': form,
        'year': year,
        'date': monday,
        'timeslots': TIMESLOTS,
        'week_range': range(WEEK_RANGE),
        'week_number': week_number,
        'days_of_week': days_of_week,
    }
    return extra_context
