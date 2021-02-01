#Soccer Team Roster
#Eric "Jack" Schorling
#January 31, 2021

weights = [0,0,0,0]
x = 0

while x < 4:
    question = "Enter weight " + str(x+1) + ": "
    weight = float(input(question))
    weights[x] = weight
    x += 1

avgweight = 0
totalweight = 0
for i in weights:
    totalweight += i
avgweight = totalweight / len(weights)

heaviest = weights[0]

for i in weights:
    if heaviest < i:
        heaviest = i

print(weights)
print("%.2f" % (avgweight))
print("%.2f" % (heaviest))


