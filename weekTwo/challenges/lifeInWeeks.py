age = input("What is your age? \n")

def weeks_left(age):
    years_left = int(90 - int(age))
    time_left = int(years_left * 52)
    print(f"You have {time_left} weeks left to live, get moving")

weeks_left(age)