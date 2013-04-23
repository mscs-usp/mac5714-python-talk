# List comprehension example 2 (list notation)
days = range(1, 31)
hours = [day * 24 for day in days]
minutes = [hour * 60 for hour in hours]
table = zip(days, hours, minutes)