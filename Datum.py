import datetime
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
d, m = map(int, input().split())
x_date = datetime.date(2009, m, d).weekday()
print(days[x_date])