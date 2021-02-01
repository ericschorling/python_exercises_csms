#Book Club
#Eric "Jack" Schorling
#February 8, 2021

numBooks = int(input("How many books did you buy: "))

if numBooks <= 1:
    print("0 points earned")
elif numBooks <= 3:
    print("5 points earned")
elif numBooks <= 5:
    print("15 points earned")
elif numBooks <= 7:
    print("30 points earned")
elif numBooks >= 8:
    print("60 points earned")
else:
    print("enter a positive number")
