#Music Quiz 
# This is a simple music quiz coding that asks the user five questions about music.
score = 0
print("Welcome to the Music Quiz!")

# Question 1
answer = input("What is the name of the artist who got featured in the song 'Like that'?").lower()
if answer== "kendrick lamar":
    print("Correct!")
    print("-------------------------")
    score += 1
elif answer== "kendrick":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 2
answer = input("Who Found the XO record label?").lower()
if answer == "weeknd":
    print("Correct!")
    print("-------------------------")
    score += 1
elif answer== "weekend":
    print("Uhm Actually its Weeknd without the 'E', but you still got it right:)")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 3
answer = input("Which Artist released the album ' I AM MUSIC'?").lower()
if answer == "playboi carti":
    print("Correct!")
    print("-------------------------")
    score += 1
elif answer== "playboy cardi":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 4
answer = input("Which Rapper Changed his name to 'Ye'?").lower()
if answer == "kanye West":
    print("Correct!")
    print("-------------------------")
    score += 1
elif answer== "kanye":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 5
answer = input("What is the real name of rapper Eminem?").lower()
if answer == "marshall mathers":
    print("Correct!")
    print("-------------------------")
    score += 1
elif answer== "marshal mathers":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 6
correct_answer = 27
answer = int(input("How many songs does the Weeknd have that are over 1 billion streams ?"))
if answer == 27:
    print("Correct!")
    print("-------------------------")
    score += 2
else:
    print("Incorrect!")
    print("-------------------------")
   
# Final score
print("Quiz completed!")
print("Score:", score)
