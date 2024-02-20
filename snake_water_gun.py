import random
my_score = 0
comp_score = 0
draw = 0
n = int(input("Enter how many times you want to play the game: "))
while n >= 1:
    lst = ['snake', 'water', 'gun']
    choice = random.choice(lst)
    a = input("\nEnter your choice:\nS for snake:\nW for water:\nG for gun:\n")
    if a == 's' or a == 'S':
        if choice == 'snake':
            print("Game Draw\n")
            draw += 1
        elif choice == 'water':
            print("You Won!\n")
            my_score += 1
        elif choice == 'gun':
            print("Computer Won\n")
            comp_score += 1
    elif a == 'w' or a == 'W':
        if choice == 'snake':
            print("Computer Won\n")
            comp_score += 1
        elif choice == 'water':
            print("Game Draw\n")
            draw += 1
        elif choice == 'gun':
            print("You Won\n")
            my_score += 1
    elif a == 'g' or a == 'G':
        if choice == 'snake':
            print("You Won\n")
            my_score += 1
        elif choice == 'water':
            print("Computer Won\n")
            comp_score += 1
        elif choice == 'gun':
            print("Game Draw\n")
            draw += 1
    else:
        print("Sorry, Your Input is Invalid!!\nPlease Try Again")
    n = n-1
if my_score > comp_score:
    print("Congratulations! You Won this Game\n")
elif comp_score > my_score:
    print("Oh! Computer Won this Game\n")
else:
    print("Game Draw\n")
print("Your Score is", my_score)
print("Computer Score is", comp_score)
print("GAME OVER")
