#Music Quiz 
# This is a simple music quiz coding that asks the user five questions about music.
score = 0
print("Welcome to the Music Quiz!")

# Question 1
answer = input("What is the name of the artist who got featured in the song 'Like that'?")
if answer== "Kendrick Lamar".lower():
    print("Correct!")
elif answer== "Kendrick Lamar ".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("Who Found the XO record label?")
if answer == "Weeknd".lower():
    print("Correct!")
elif answer== "Weekend".lower():
    print("Uhm Actually its Weeknd without the 'E', but you still got it right:)")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("Which Artist released the album ' I AM MUSIC'?")
if answer == "Playboi Carti".lower():
    print("Correct!")
elif answer== "Weekend".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("Who sang the song 'Juno'?")
if answer == "Sabrina carpenter".lower():
    print("Correct!")
    score += 2
else:
    print("Incorrect!")

# Question 5
answer = input("What is the real name of rapper Eminem?")
if answer == "Marshall Mathers".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 6
answer = int(input("How many songs does The Weeknd have that are over 1 billion streams ?")) 
if answer == 27:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Final score
print("Quiz completed!")
print("Score:", score)
