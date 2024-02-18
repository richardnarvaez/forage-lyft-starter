from datetime import datetime

def add_years_to_date(base_date, years_to_add):
    if isinstance(base_date, str):
        base_date = datetime.strptime(base_date, "%Y-%m-%d")
    result = base_date.replace(year=base_date.year + years_to_add)
    return result