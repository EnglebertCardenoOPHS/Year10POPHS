#SELECTION

#Selection uses if/elif and else
#things people get wrong are:
#1.forgetting the colon:
#2.forgetting indentation
#3.not understanding comparison
#operators ==

SkyColour = ("blue")

if SkyColour =="blue":
    print ("The sky is blue today")

print ("Good Bye!")

baby = input("Has the baby been born yet? y or n?")

if baby == ("y"):
     print("Congratulations")
else:
     print("Call us when you have news")

food = "kebab"

if food == "kebab":
   print("ummmm, my favorite!")
   print("I feel like saying it 100 times...")
   print(100 * (food + "!"))
else:
     print("Im hungry")
