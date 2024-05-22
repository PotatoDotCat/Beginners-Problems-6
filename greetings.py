def greet(name, time):
    if 0 <= time <= 12:
        print("Good morning,", name)
    elif 13 <= time <= 17:
        print("Good afternoon,", name)
    elif 18 <= time <= 23:
        print("Good evening,", name)

name = input("What's your name: ")
time = int(input("What time is it: "))
greet(name, time)
