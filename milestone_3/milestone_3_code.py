#Music Quiz 
# This is a simple music quiz coding that asks the user five questions about music.
score = 0
print("Welcome to the Music Quiz!")

# Question 1
print("What is the name of the artist who got featured in the song 'Like that'?")
print("a) Drake")
print("b) Kendrick Lamar")
print("c) Travis Scott")
print("d) J. Cole")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "b":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 2
print("Which rapper changed his name to 'Ye'?")
print("a) Kanye West")
print("b) Yellawolf")
print("c) Yella beezy")
print("d) Yellbowow")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "a":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 3
print("What is the real name of the artist 'Eminem'?")
print("a) Mathew Marshall")
print("b) Mathew Mather")
print("c) Marshall Mathew")
print("d) Marshall Mather")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "d":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 4
print("Who found the XO record label?")
print("a) Travis Scott")
print("b) Dr. Dre")
print("c) The Weeknd")
print("d) Drake")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "c":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 5
print("How many songs does the Weeknd have that are over 1 billion streams?")
print("a) 5")
print("b) 27")
print("c) 19")
print("d) 10")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "b":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 6
print("Which rapper is known for the album 'I AM MUSIC'?")
print("a) Playboi Carti")
print("b) Tyler the creator")
print("c) Lil wayne")
print("d) Kid cudi")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "a":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 7
print("Which animated series did D4vd's song 'Feel it' got played?")
print("a) Devil may cry")
print("b) My hero academia")
print("c) Tokyo Ghoul")
print("d) Invincible")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "d":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")
   
# Question 8
print("In which D4vd's album the song 'Feel it' got played?")
print("a) Weathered")
print("b) Willows in the wind")
print("c) Withered")
print("d) Witch Craft")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "c":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 9
print("What is Kali Uchis' most popular song?")
print("a) Moon Light")
print("b) See you again")
print("c) Telepatia")
print("d) I wish you roses")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "c":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Question 10
print("What is the name of the Artist who got featured in the song 'See you again' by Tyler the Creator?")
print("a) Kali Uchis")
print("b) Taylot Swift")
print("c) Don Toliver")
print("d) Charlie Puth")
answer = input("Enter your answer (a/b/c/d): ").lower()
if answer == "a":
    print("Correct!")
    print("-------------------------")
    score += 1
else:
    print("Incorrect!")
    print("-------------------------")

# Final score
print("Quiz completed!")
print("You have finished the Music Quiz")
print("Score:", score)
