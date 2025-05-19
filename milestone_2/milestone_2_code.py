name = input("What is your name? ")
if name == "Johan":
  print("Whoa, Johan? That's a legendary name! You must be at least 50% cooler than the average human.")
else:
  print("Not bad! But have you considered changing it to 'Johan' for extra style points?")

age = int(input("How old are you?"))
if age < 18:
  print("You are a minor and i'm gonna touch you jk.")
elif age >= 18:
 print("I hope you don't touch me.")

mood = input("How are you feeling today? ")
if mood.lower() == "happy":
  print("That's awesome! Did you win the lottery or just have coffee?")
elif mood.lower() == "sad":
  print("I'm sending you a puppy gif. Hang in there!")

number = int(input("Pick a number:"))
if number <= 10:
  print("That's a tiny number! Just like, someone I know who's tiny aswell.")
elif 10 < number <= 80:
  print("That's a medium-sized number.")
else:
  print("Whoa, that's a huge number!")
