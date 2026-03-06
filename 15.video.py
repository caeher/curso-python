x = 10
print("Condicional if-else")
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than 5")

print("Fuera del programa")
print("-"*25)

print("Condicional if-elif-else")
y = 10
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

print("Fuera del programa")
print("-"*25)


x = 15
y = 20
if x > 10 and y > 25:
    print("x is greater than 10 and y is greater than 25")
else:
    print("x is less than 10 or y is less than 25")

print("Fuera del programa")
print("-"*25)

if x > 10 or y > 25:
    print("x is greater than 10 or y is greater than 25")
else:
    print("x is less than 10 and y is less than 25")

print("Fuera del programa")
print("-"*25)

if not x > 10:
    print("x is not greater than 10")
else:
    print("x is greater than 10")

print("Fuera del programa")
print("-"*25)


is_member = True
age = 15

if is_member:
    if age >= 15:
        print("You are a member")
    else:
        print("You are a member, but you don't have access to the club")
else:
    print("You are not a member")



# Piedra, papel, tijeras

user_choice = input("Enter your choice (rock, paper, scissors): ")
computer_choice = random.choice(["rock", "paper", "scissors"])

if user_choice == computer_choice:
    print("It's a tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win")
else:
    print("You lose")
