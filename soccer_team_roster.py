#Soccer Team Roster
#Eric "Jack" Schorling
#January 31, 2021



def print_menu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - quit")
    selection = input("Choose an option: ")
    return selection

def weights ():
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

def getJerseys():
    jerseyDict = {}
    x = 0

    while x < 5:
        jerseytxt = "Enter Player " + str(x+1) + "'s Jersey Number: "
        ratingtxt = "Enter Player " + str(x+1) + "'s Rating: "
        jersey = input(jerseytxt)
        rating = input(ratingtxt)
        jerseyDict[jersey] = rating
        x += 1

    keyArr = list(jerseyDict.keys())
    print(keyArr)

    for y in keyArr:
        for i in range(len(keyArr)-1):
            if keyArr[i]> keyArr[i+1]:
                holder = keyArr[i]
                keyArr[i] = keyArr[i+1]
                keyArr[i+1] = holder

    print(keyArr)

    for i in keyArr:
        print("Jersey number %s, Rating: %s" % (i, jerseyDict[i]))

weights()
getJerseys()

run_program = True

while run_program:
    option = print_menu()
    if option == "q":
        run_program = False
