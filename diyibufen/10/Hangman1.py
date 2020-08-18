def hangman(word):
    wrong = 0
    stages = ["",
              "_________________    ",
              "|          |       ",
              "|          |       ",
              "|          0       ",
              "|         \|/      ",
              "|         / \      ",
              "|                  "

              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win=False

    while wrong < len(stages):
        print("\n")
        char = input("Guess a letter")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("you win")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages))
        print("you lost")


hangman("java")