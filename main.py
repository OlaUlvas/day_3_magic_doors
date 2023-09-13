print('''

                         .

                     o  .

                       o        ___________
                     O       ,-'        ,-'|
                         o   |""""""""""|  |
                      .x     |_ /""""\ _|,-'
                    .    x   |_|  |   |_|,-' 
                      x`     | |,-]   | |  |
             /\         `x   |_],-'   [_|,-'
            / />     \"/           
           /  \}     / `-')            ____ _____   
          /`---\   .-`---'-.        ,-'  ,-'_ ,-'|   
          |  \__D  \`--.--'/       |""-'" ,-'|   |   
         /     /    \     /        ||""""|   |,-'   
        /_____/\   _//^-^\\_.____   |____|,-'   
                   ____ _,-'_ ,-'|                 
                ,-'  ,-'  ,-'|   |       
               |""""|""""|   |,-'      brojek
               |____|____|,-'      
                                    ''')

print("Welcome to the Magic Maze.")
print("Can you find the way out of the Magic Maze, and at the same time find some money on the way.\n")

magic_score = 0

door1 = int(input("You will arrive at 10 doors numbered from left to right as 1, 2, 3, 4, 5, 6, 7, 8, 9, 0."

                  "Which door do you choose?\n"))

if door1 == 3:
    magic_score += 100
    print("Lucky You!")
    print(f"You now own {magic_score} Magic Money")
else:
    print("Nothing here!")

door2 = int(input("Again, You will arrive at 10 doors numbered from left to right as 1, 2, 3, 4, 5, 6, 7, 8, 9, 0."

                  "Which door do you choose?\n"))

if door2 == 1:
    if magic_score == 0:
        magic_score = 20
    magic_score *= 2
    print("Lucky You!")
    print(f"You now own {magic_score} Magic Money")
else:
    magic_score /= 2
    print("oh oh, wrong door, you're loosing money.")
    print(f"You now own {round(magic_score)} Magic Money")

door3 = int(input("Again, You will arrive at 10 doors numbered from left to right as 1, 2, 3, 4, 5, 6, 7, 8, 9, 0."

                  "Which door do you choose?\n"))

if door3 == 4:
    if magic_score == 0:
        magic_score = 20
    magic_score *= 2
    print("Lucky You!")
    print(f"You now own {round(magic_score)} Magic Money")
else:
    magic_score /= 2
    print("oh oh, wrong door, you're loosing money.")
    print(f"You now own {round(magic_score)} Magic Money")

door4 = int(input("Again, You will arrive at 10 doors numbered from left to right as 1, 2, 3, 4, 5, 6, 7, 8, 9, 0."

                  "Which door do you choose?\n"))

if door4 == 1:
    if magic_score == 0:
        magic_score = 20
    magic_score *= 2
    print("Lucky You!")
    print(f"You now own {round(magic_score)} Magic Money")
else:
    magic_score /= 2
    print("oh oh, wrong door, you're loosing money.")
    print(f"You now own {round(magic_score)} Magic Money")

door5 = int(input("Again, You will arrive at 10 doors numbered from left to right as 1, 2, 3, 4, 5, 6, 7, 8, 9, 0."

                  "Which door do you choose?\n"))

if door5 == 5:
    if magic_score == 0:
        magic_score = 20
    magic_score *= 2
    print("Lucky You!")
    print(f"You now own {round(magic_score)} Magic Money")
else:
    magic_score /= 2
    print("oh oh, wrong door, you're loosing money.")
    print(f"You now own {round(magic_score)} Magic Money")

door6 = int(input("Again, You will arrive at 10 doors numbered from left to right as 1, 2, 3, 4, 5, 6, 7, 8, 9, 0."

                  "Which door do you choose?\n"))

if door6 == 9:
    if magic_score == 0:
        magic_score = 20
    magic_score *= 2
    print("Lucky You!")
    print(f"You now own {round(magic_score)} Magic Money")
else:
    magic_score /= 2
    print("oh oh, wrong door, you're loosing money.")
    print(f"You now own {round(magic_score)} Magic Money")

door7 = int(
    input("For the last time, You will arrive at 10 doors numbered from left to right as 1, 2, 3, 4, 5, 6, 7, 8, 9, 0."

          "Which door do you choose?\n"))

if door7 == 2:
    if magic_score == 0:
        magic_score = 20
    magic_score *= 2
    print("Lucky You!")
    print(f"You now own {round(magic_score)} Magic Money")
else:
    magic_score /= 2
    print("oh oh, wrong door, you're loosing money.")
    print(f"You now own {round(magic_score)} Magic Money")

print(f"\nCongratulation, you have passed the Magic Maze and you won {round(magic_score)} Magic Money.")




