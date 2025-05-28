name = input("What is your name? ")
if name == "Johan":
  print("Johan? That's a cool name!.")
else:
  print("Not bad {}, But have you considered changing it to 'Johan' for extra style points?".format(name))

age = int(input("How old are you?"))
if age < 18:
  print("Get off your laptop and go play outside.")
elif age >= 18:
 print("Hello there, unc/aunt.")

mood = input("How are you feeling today? (Happy or Sad)").lower()
if mood == "happy":
    happy_reason = input("That's awesome! Type 'lottery' if you won the lottery or 'coffee' if you just had coffee: ")
    if happy_reason == "lottery":
            print("Wow, you're rich! Can I borrow some money? Just kidding!")
    elif happy_reason == "coffee":
            print("Don't drink too much coffee or you will be hyperactive!")
    else:
     print("Whatever the reason, keep smiling!")
    
elif mood == "sad":
    print("I'm sending you a puppy gif. Hang in there!")
    print("Here's your puppy gif: https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmhuYmd2YWJ2MnpuZWtzMmY0Mnp2NWJ3cXk3bzU2cHJpOHFuZG91MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/cYZkY9HeKgofpQnOUl/giphy.gif")
