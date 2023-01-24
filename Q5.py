# Create function to check if date is in given range
from datetime import datetime

d1,m1,y1= [int(x) for x in input("Enter the starting date (DD-MM-YYYY) : ").split("-")]
d2,m2,y2= [int(x) for x in input("Enter the ending date (DD-MM-YYYY) : ").split("-")]
dc,mc,yc= [int(x) for x in input("Enter the date to be checked (DD-MM-YYYY) : ").split("-")]

start=datetime(y1,m1,d1)
end=datetime(y2,m2,d2)
tocheck=datetime(yc,mc,dc)

if tocheck>=start and tocheck<=end:
    print(f"Date {dc}-{mc}-{yc} is in range {d1}-{m1}-{y1} to {d2}-{m2}-{y2}")
else:
    print(f"Date {dc}-{mc}-{yc} is not in range {d1}-{m1}-{y1} to {d2}-{m2}-{y2}")
