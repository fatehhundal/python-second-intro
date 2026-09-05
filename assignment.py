import keyword
print("MY PERSONAL GOAL PLAN")

name = input("What's your name? ")
goal = input("What skill do you want to work on? ")
month = input("What month do you want to complete this by? ")
time = int(input("How much time (in minutes) do you want to spend each day? "))
print("\n")
print("Thank you", name, end=". ")
print("Here is a one sentence summary of what you have told me:")

print("You want to work on", goal, "for", time, "minutes each day until", month + ".\nGood luck!\n")

print("Registered ® by Fateh Hundal")
print(keyword.kwlist)