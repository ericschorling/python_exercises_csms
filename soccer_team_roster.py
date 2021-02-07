#Soccer Team Roster
#Eric "Jack" Schorling
#January 31, 2021


jerseyDict = {}

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
        if weight > 0:
            weights[x] = weight
            x += 1
        else: 
            print("Enter a valid weight.")

    avgweight = 0
    totalweight = 0
    for i in weights:
        totalweight += i
    avgweight = totalweight / len(weights)

    heaviest = weights[0]

    for i in weights:
        if heaviest < i:
            heaviest = i

    print("Weights: " + weights)
    print("Average weight: %.2f" % (avgweight))
    print("Max weight: %.2f" % (heaviest))

def getJerseys(jerseyDict):
    x = 0

    while x < 5:
        jerseytxt = "Enter Player " + str(x+1) + "'s Jersey Number: "
        ratingtxt = "Enter Player " + str(x+1) + "'s Rating: "
        jersey = input(jerseytxt)
        if jersey in jerseyDict:
            print("The player with jersey number " + jersey + " has already been entered.")
        else:
            rating = input(ratingtxt)
            jerseyDict[jersey] = rating
            x += 1

    keyArr = list(jerseyDict.keys())

    for y in keyArr:
        for i in range(len(keyArr)-1):
            if keyArr[i]> keyArr[i+1]:
                holder = keyArr[i]
                keyArr[i] = keyArr[i+1]
                keyArr[i+1] = holder

    for i in keyArr:
        print("Jersey number %s, Rating: %s" % (i, jerseyDict[i]))
    return jerseyDict

def print_roster(jerseyDict):
    keyArr = list(jerseyDict.keys())
    
    for i in keyArr:
        print("Jersey number %s, Rating: %s" % (i, jerseyDict[i]))

def add_player(jerseyDict):
    new_player = input("Enter player jersey number: ")
    if new_player in jerseyDict:
        print("The player with jersey number " + new_player + " is already on the roster.")
    else:
        player_rating = input("Enter player rating: ")
        jerseyDict[new_player] = player_rating
    
    return jerseyDict

def remove_player(jerseyDict):
    player_out = input("Enter the jersey number of the player you'd like to remove: ")
    if player_out in jerseyDict:
        jerseyDict.pop(player_out)
        return jerseyDict
    else:
        print("There is no player with the jersey number " + player_out + "on the team.")

def update_player(jerseyDict):
    check_it = True
    while check_it:
        player_update = input("Which player would you like to update: ")
        if player_update in jerseyDict:
            new_rating = input("What is the new rating for the player: ")
            check = True
            while check:
                if int(new_rating) > 0:
                    jerseyDict[player_update] = new_rating
                    check = False
                    return jerseyDict
                else:
                    print("Enter rating above 0.")
        else:
            print("Please enter a player on the roster")
def player_output(jerseyDict):
    truth = True
    while truth:
        ranking = int(input("See the players above which rating: "))
        if ranking >= 0:
            truth = False
            keyArr = list(jerseyDict.keys())
            print("Current Team")
            for i in keyArr:
                if int(jerseyDict[i]) > ranking:
                   print("Jersey number %s, Rating: %s" % (i, jerseyDict[i]))


#weights()
jerseyDict = getJerseys(jerseyDict)

run_program = True

while run_program:
    option = print_menu()
    if option == "q":
        run_program = False
    elif option =="a":
        jerseyDict = add_player(jerseyDict)
    elif option == "d":
        jerseyDict = remove_player(jerseyDict)
    elif option == "u":
        jerseyDict = update_player(jerseyDict)
    elif option == "r":
        player_output(jerseyDict)
    elif option == "o":
        print_roster(jerseyDict)
    else:
        print("Enter a valid option")


