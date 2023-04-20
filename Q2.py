#Write a program to calculate the total of a grocery list. 
#Create 5 variables to represent the items in the list and their prices. 
#Add up all the prices and print out the entire shopping list and total.
#Your output should look like this:
#    Reciept:
#    item 1: Eggs - 3.99
#    item 2: Milk - 2.50
#    ....
#    Total:        10.65

#Instead of creating 5 variables, put the items into a list and print it out.
#Again, add up the items (EX: total = thisList[1] + thisList[3])
#The user decided to put an item back. 
#Ask the user which item they would like to remove and remove the item and its price from the list
#Now reprint out the new list. 

#Do the same as HW 2 Q2 but now have the user add and remove as many grocieries as they want. (You must use loops).
#Same as before, print out the list after they have added everything. If they remove groceries, reprint out the list. 

#Azariah Muhammad
#3/20/2023
#HW3Q3
keepGoing= 'yes'
groceryList= []
while keepGoing == "yes":
  gorcery= input("Add a grocery item!: ")
  groceryList.append(gorcery)
  print("Your groceries:\n ", groceryList)
  keepGoing= input("Would you like to add another item?"+ "(Enter yes):")

keepGoing= 'yes'
while keepGoing == "yes":
  gorcery= input("remove a grocery item!: ")
  groceryList.remove(gorcery)
  print("Your groceries:\n ", groceryList)
  keepGoing= input("Would you like to remove another item?"+ "(Enter yes):")
print("Here are your groceries!", groceryList)

print(" Have a nice day!")

