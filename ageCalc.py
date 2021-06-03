day, month, year = input("Type in your date of birth (DD/MM/YYYY):\n").strip().split("/")
age = 2021 - int(year)
if day == "1":
    print(f"You were born on {month} 1st, {year} and you are {age} years old")
elif day == "2":
    print(f"You were born on {month} 2nd, {year} and you are {age} years old")
elif day == "3":
    print(f"You were born on {month} 3rd, {year} and you are {age} years old")
else: print(f"You were born on {month} {day}th, {year} and you are {age} years old")
