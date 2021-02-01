#Rain Fall
#Eric "Jack" Schorling
#February 1, 2021

years = int(input("How many years: "))
totalRain = 0
y = years
while y > 0:
    for x in range(12):
        question = "How much rain fell in month " + str(x+1) +": "
        monthlyRain = float(input(question))
        totalRain += monthlyRain
    y -= 1
averageFall = float(totalRain / (years*12))

print("Over the course of %d months %d inches of rain fell for an average rain fall of %.2f per month." % ((years*12), totalRain, averageFall))
