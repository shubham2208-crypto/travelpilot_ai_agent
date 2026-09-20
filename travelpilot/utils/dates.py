from datetime import datetime, timedelta

def parse_date(date_str):
    for fmt in ("%Y-%m-%d", "%d %B %Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return datetime.now()

def date_range(start_date, end_date):
    start = parse_date(start_date)
    end = parse_date(end_date)
    delta = end - start
    return [start + timedelta(days=i) for i in range(max(delta.days + 1, 1))]