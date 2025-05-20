name = input("What is your name? ")
if name == "Johan":
  print("Johan? That's a cool name! You must be at least 50% cooler than the average human.")
else:
  print("Not bad! But have you considered changing it to 'Johan' for extra style points?")

age = int(input("How old are you?"))
if age < 18:
  print("Get off your laptop and go play outside.")
elif age >= 18:
 print("Hello there, unc.")

mood = input("How are you feeling today? (Happy or Sad)").strip().lower()
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
    print("Here's your puppy gif: https://media.giphy.com/media/3o7aD2saq4v5g0x6cI/giphy.gif")
    
