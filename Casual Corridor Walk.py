# Pre-requisitives
from itertools import count
from random import randint
import time
from urllib import response
import random
import operator

# Game Arrays
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
stairway = ["upstairs","downstairs"]

# Main Menu
def start():
    response = ""
    while response not in yes_no:
        response = input(
            "Welcome to 'Casual Corridor Walk'\nDo you want to start?\nyes/no\n")
        if response == "yes":
            story_corridor1_1f()
        elif response == "no":
            print("Exiting Game...")
            quit()
        else:
            print("Unknown Reply.\n")

# Retry Menu
def retry():
    response = ""
    while response not in yes_no:
        response = input(
            "\nYou lost the game. Would you like to retry?\nyes/no\n")
        if response == "yes":
            story_corridor1_1f()
        elif response == "no":
            print("Exiting Game...")
            quit()
        else:
            print("Unknown Reply.\n")

# story_corridor_1f - Corridor of First Floor
def story_corridor1_1f():
    response = ""
    while response not in directions:
        response = input(
            "You were walking down the school corridor.\nWhich direction would you like to go?\nleft/right/forward/backward\n")
    if response == "left":
        story_toilet_1()
    elif response == "right":
        print("You bumped into a wall.\n")
        story_corridor1_1f()
    elif response == "forward":
        story_corridor2_1f()
    elif response == "backward":
        print("You don't feel like turning back right now.\n")
        story_corridor1_1f()
    else:
        print("Unknown Reply.\n")

# story_toilet_1 - Infront of the toilet. Player can choose to go into the female or male's toilet. Both gives different outcome.
def story_toilet_1():
    response = ""
    while response not in directions:
        response = input(
            "You walked into the toilet.\nTo your left is the female's toilet and to your right is the male's toilet.\nWhich direction would you like to go?\nleft/right\n")
    if response == "left":
        print("You walked into the female's toilet.\nThere are girls inside changing their uniform.\nThey saw you and screamed.\nYou immediately got out, but was caught by a teacher.\n")
        print("You were suspended from school...")
        retry()
    elif response == "right":
        story_toilet_2()
    else:
        print("Unkown Reply.\n")

# story_toilet_2 - Player enters male's toilet. Given option to play High-Low Game.
def story_toilet_2():
    response = ""
    while response not in yes_no:
        response = input(
            "You entered the male's toilet and see a suspicious figure.\nHe asked you if you want to play High-Low with him.\nWill you accept his request?\nyes/no\n")
    if response == "yes":
        story_toilet_hilo()
    elif response == "no":
        story_corridor2_1f()
    else:
        print("Unknown Reply.\n")

# story_toilet_3 - Player plays High-Low Game.
def story_toilet_hilo():
    value = randint(1, 10)
    count = 0
    print("Suspicious Figure: I've picked a number between 1 to 10. Make your guess. You have 5 chances.")
    while count != 5:
        guess = int(input("Make your guess:"))

        if guess > value:
            print(
                "Suspicious Figure: The number I guessed is lower than this, try again!")
            count = count+1
        elif guess < value:
            print(
                "Suspicious Figure: The number I guessed is higher than this, try again!")
            count = count+1
        elif guess == value:
            print(
                "You guessed it correctly.\nThe suspicious figure disappeared, so you decided to go out.\n")
            story_corridor2_1f()
        else:
            print("Unknown Reply.\n")
    print("I chose %i." % value)
    if count == 5:
        print("You lost a simple game.\nThe suspicious figure dashed into you and stabbed you multiple times.\nYou're dead.")
        retry()

# story_corridor2_1f - Corridor Walk Part 2 of 1F
def story_corridor2_1f():
    response = ""
    while response not in directions:
        response = input(
            "You're now some meters in front of your starting position.\nWhich direction would you like to go?\nleft/right/forward\n")
    if response == "left":
        story_classroom_math_1()
    elif response == "right":
        story_classroom_ict_1()
    elif response == "forward":
        story_corridor3_1f()
    elif response == "backward":
        print("You decided to keep moving forward like Eren Yeager.\nTherefore, no turning back.\n")
        story_corridor2_1f()
    else:
        print("Unknown Reply.\n")

# story_classroom_ict_1 - ICT Room
def story_classroom_ict_1():
    print("You entered the ICT room")
    story_classroom_ict_2()   

# story_classroom_math_1 - Math Classroom
def story_classroom_math_1():
    response = ""
    while response not in directions:
        response = input(
            "You are in the math classroomn.\nWhich direction would you like to go?\nleft/right/forward/backward\n")
    if response == "forward":
        story_classroom_mathquiz()
    elif response == "right":
        response = input(
            "There is a white board infront of you, do you want to read it?\nyes/no\n")
        if response == "yes":
            print("Never gonna give you up, Never gonna let you down, never gonna run around and desert you...")
            story_classroom_math_1()
        elif response == "no":
            story_classroom_math_1()
    elif response == "left":
        print("You met Steve and he challenged you to a 'Rock, Paper, Scissor' game.")
        rock_paper_scissors()
    elif response == "backward":
        story_corridor2_1f()

# story_classroom_math_2 - Player's given a randomly generated math question. Solve it!
def story_classroom_mathquiz():
    print("Teacher: I will give you a math question!\n")
    operators = {
        '+': operator.add,
        '-': operator.sub,
        'x': operator.mul,
        '/': operator.truediv,
    }

    num_1 = random.randint(1, 20)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print(f'what is {num_1} {operation} {num_2}?')
    chances = 0
    while chances != 5:
        myanswer = float(input("Type your answer:"))

        if myanswer == answer:
            print("You're correct")
            story_classroom_mathwin()
        elif myanswer != answer:
            print("You're wrong.")
            chances = chances+1
    if chances == 5:
        print("You failed at maths.")
    else:
        print("Unknown Reply.\n")
        
# story_classroom_mathwin - You answered the math question correctly.
def story_classroom_mathwin():
    response = ""
    while response not in yes_no:
        response = input(
            "You've solved the math question correctly.\nYou were given a certificate of not failing simple math question.\nWould you like to continue the game?\nyes/no\n")
    if response == "yes":
        story_corridor3_1f()
    elif response == "no":
        quit()

 # rock_paper_scissors - RPS Game
def rock_paper_scissors():
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, Steve chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        story_rps_ending()
    elif user_action == "rock":
        if computer_action == "scissors":
            print("The 'Rock' smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
        story_rps_ending()
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
        story_rps_ending()
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("The 'Rock' smashes scissors! You lose.")
        story_rps_ending()

# story_rps_ending - RPS Ending.
def story_rps_ending():
    print("You and Steve decided to go to the school canteen and enjoy your day together.")
    quit()

# story_corridor3_1f - End of Corridor 1F. Player will either go upstairs or downstairs.
def story_corridor3_1f():
    response = ""
    while response not in stairway:
        response = input(
            "You've reached the end of the corridor.\nTo your right is the staircase. Which way you're going?\n'upstairs/downstairs\n")
    if response == "upstairs":
        story_corridor1_2f()
    elif response == "downstairs":
        story_basement1()
    else:
        print("Unknown Reply.\n")

#story_basement1 - If player choose downstair they will be directed to story basement 
def story_basement1():
    response = ""
    while response not in directions:
        response = input("You are now in the basement of the school.Which direction do you want to go?\nright/left/forward/upstairs\n")
    if response == "right":
        print("You see a suspicious door infront of you and you open it, you see a cleaner is cleaning up a storage room.")
        storage_room()
    elif response == "upstairs":
        story_corridor3_1f()
    elif response == "forward":
        print("You met the suspicious figure again")


#storage_room - if player choose right, they will be directed to a conversation(random output) with the cleaner
def storage_room():
    cleanerconvo1 = ("Cleaner: Hello there, are you here to help me?")
    cleanerconvo2 = ("Cleaner: Hello you must be that student everyone were talking about, do you mind helping me cleaning up this room?")
    cleanerconvo3 = ("Do you like cleaning up room?")
 
    cleanerconvolist = [cleanerconvo1, cleanerconvo2, cleanerconvo3]

    convo = random.choice(cleanerconvolist)
    print(convo)   

#Continues the conversation
    if convo == cleanerconvo1:
       convo1()
    elif convo == cleanerconvo2:
        time.sleep(1)
        print("You: I think you refer to the wrong guy.")
        convo2()
    elif convo == cleanerconvo3:
            time.sleep(1)
            print("You: I dont really like cleaning up room but sure Ill help you")
            time.sleep(1)
            print("Cleaning up progress: 10%")
            time.sleep(2)
            print("Cleaning up progress: 45%")
            time.sleep(3)
            print("Cleaning up progress: 63%")
            time.sleep(3)
            print("Cleaning up progress: 89%")
            time.sleep(4)
            print("Cleaning up progress: 100%")
            print("Cleaner: Great, now let's exit the room")
            story_basement1()

#If they get convo 1
def convo1():
    response = ""
    while response not in yes_no:
        response = input("Type your answer\nyes/no\n")
    if response == "yes":
        print("Cleaner: Great, now grab that broom and lets clean up this dusty space!")
        time.sleep(1)
        print("Cleaning up progress: 10%")
        time.sleep(5)
        print("Cleaning up progress: 45%")
        time.sleep(6)
        print("Cleaning up progress: 69%")
        time.sleep(7)
        print("Cleaning up progress: 90%")
        time.sleep(8)
        print("Cleaning up progress: 100%")
        print("Cleaner: Nice work! thankyou for the helping hand, now you may get out of this room")
        story_basement1()
    elif response == "no":
        print("Cleaner: Fine I'll do it all by myself")
        story_basement1()

#If they get convo 2
def convo2():
    response = ""
    while response not in yes_no:
        response = input("Will you help the cleaner?\nyes/no\n")
    if response == "yes":
        print("Cleaner: Free labour?! Ill take it!")
        time.sleep(1)
        print("Cleaning up progress: 10%")
        time.sleep(2)
        print("Cleaning up progress: 30%")
        time.sleep(2)
        print("Cleaning up progress: 54%")
        time.sleep(4)
        print("Cleaning up progress: 70%")
        time.sleep(5)
        print("Cleaning up progress: 90%")
        time.sleep(6)
        print("Cleaning up progress: 100%")
        print("Cleaner: Great job kid, now you shall get out of this room")
        story_basement1()
    elif response == "no":
        print("Cleaner:*Smh*")
        story_basement1()
     

      



start()


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡦⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣮⣮⣮⣮⣮⣎⣌⣌⢌⢈⢈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠁⠀⠀⢂⣑⡳⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣎⢌⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⡈⠂⠀⠀⠀⠀⢀⡀⠠⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠌⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠠⠑⠀⠑⢑⢙⠙⠑⠑⠱⠳⡷⣷⣿⣿⣿⣿⠀⠄⡷⡷⡷⠳⠳⠳⡳⣿⣿⣿⣿⣿⣿⠈⠀⠀⠀⠀
# ⠀⠀⠀⡈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠈⠐⠁⠀⠠⠀⠀⢀⢈⠀⢈⠀⠱⣿⣿⢟⠀⠀⠀⡦⠆⠀⠀⢙⣈⣾⣿⣿⣿⣿⣿⣯⢌⠀⠀⠀
# ⠀⠀⡠⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⡻⣷⣿⣿⣿⡿⠓⠀⠀⠀⠀⣿⣿⣿⣿⠀⠎⣦⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠎⠀⠀
# ⠀⠀⠇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠒⠀⠤⠱⣷⡿⠁⠀⠈⡄⠀⠀⣷⣿⣿⣿⠈⡃⠈⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀
# ⠀⠀⠰⠀⠈⡀⠂⠤⠀⠀⠀⠀⠀⢀⠤⠁⢀⠔⠀⠀⠐⠁⠀⠜⠀⠄⠀⡄⡰⣿⣿⣿⣿⠌⠐⠂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
# ⠀⠀⠀⠀⢄⠁⠐⠀⠀⠀⢀⡄⠂⠁⢀⠤⠁⠀⠀⠁⠐⠀⠀⢃⠀⣢⠀⢀⠀⠱⠳⡷⠓⠀⢈⣼⣿⣿⣿⣿⣿⠏⣳⣿⣿⣿⣿⡿⠀⠀⠀
# ⠀⠀⠀⠀⠐⢆⠀⠀⠀⠂⠀⠀⡀⡆⡄⡄⡄⠄⠀⠀⠀⠀⠢⠀⠠⠀⡀⡄⠄⣈⣮⣮⣮⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠹⣷⣿⣿⠃⠀⠀⠀
# ⠀⠀⠀⠀⠀⠐⠆⠀⠇⠀⠎⠀⢀⠀⠀⠀⠀⠀⡄⡄⡄⡄⡄⡄⡄⣄⣌⣌⣌⢈⢙⠙⠑⠱⠳⠳⠳⠳⠳⠳⠳⠳⠑⠁⠰⣿⠇⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠐⢄⡠⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣮⣮⣾⣿⣿⣿⣿⣾⠿⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⡀⠩⠀⡡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⢅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⡀⠄⠈⠀⠀⠀⠀⠀⠀⠀⠠⠀⡰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠠⠂⡄⢀⠈⠀⠐⠁⠀⡳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠢⠀⡄⡔⠳⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠷⠁⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠑⠑⠑⠑⠑⠑⠑⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#                      Xuě huā piāo piāo běi fēng xiāo xiāo
#                          iān dì yí piàn cāng máng                   