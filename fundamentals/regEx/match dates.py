import re

text = input()

pattern = r"(?P<Day>\d{2})([\./-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"

dates = re.finditer(pattern, text)

for date in dates:
    date_data = date.groupdict()
    print(f"Day: {date_data['Day']}, Month: {date_data['Month']}, Year: {date_data['Year']}")