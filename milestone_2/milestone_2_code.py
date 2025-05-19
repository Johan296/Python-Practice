name = input("What is your name?")
if name == "Johan":
  print("That's a pretty cool name!")
else:
  print("That is not tuff")

mood = input("How are you feeling today?")
if mood == "happy":
  print("That's great!")
elif mood == "sad":
  print("I'm sorry to hear that.")
else:
  print("I hope your day gets better!")

number = int(input("Pick a number: "))
if number <= 10:
  print("That's a small number!")
elif number > 10 and number <= 80:
  print("That's a medium sized number")
else:
  print("Wow that's big!")
