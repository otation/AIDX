
from random import randint

print("Welcome to Python casino!")

pcChoice = randint(1,50)

playing = True

while playing:
 userChoice = int(input("Choose number.(1-50):"))
 if userChoice == pcChoice:
  print("you won!")
  playing = False
 elif userChoice > pcChoice:
  print("Lower!")
 elif userChoice < pcChoice:
  print("Higher!")
