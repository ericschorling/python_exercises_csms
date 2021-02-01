#Alarm Clock
#Eric "Jack" Schorling
#January 31, 2021
x = 1
y = 1
while x == 1:
    time = int(input("What time is it now: "))
    if time > 24:
        print("Time must be in 24 hour clock.")
    elif time <= 0:
        print("Time must be greater than 0.")
    else:
        x = 0
while y == 1:
    hoursAhead = int(input("How long should we wait: "))
    if hoursAhead < 0:
        print("Time ahead must follow the entropy of the current universe, no time travel...")
    else:
        y = 0

addTime = time + hoursAhead
returntime = addTime % 24

print("The time you'd wake up is", returntime)