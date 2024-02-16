
import datetime
from datetime import date
now = date.today()
now

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
birthday = date(2004,9, 14)
age = now - birthday
print(age.hour)
