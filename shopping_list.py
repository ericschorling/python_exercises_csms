#Week 2 
#Eric "Jack" Schorling
#Retail Total

item1 = input("First Item: ")
item2 = input("Second Item: ")
item3 = input("Third Item: ")
item4 = input("Fourth Item: ")
item5 = input("Fifth Item: ")

subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * .07
total = subtotal + tax

print("Subtotal: %d" % (subtotal))
print("Tax: %.2f" % (tax))
print("Total: %.2f" % (total)) 