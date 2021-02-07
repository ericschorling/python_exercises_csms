#Drivers License
#Eric "Jack" Schoring
#February 9, 2021

answerKey = ["A","C","A","A","D","B","C","A","C","B","A","D","C","A","D","C","B","B","D","A"]
correct = 0
wrongArr = []

answers = open("answers.txt")
y = 0
for x in answers:
    if answerKey[y] == x[0]:
        correct += 1
    else:
        wrongArr.append((y+1))
    y += 1
answers.close()

print("You got %d correct and %d incorrect. " % (correct, (20-correct)))
print("You missed", wrongArr)