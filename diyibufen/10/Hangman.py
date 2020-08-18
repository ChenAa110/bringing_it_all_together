def hangman(word):
    wrong = 0
    stange = ["",
              "_________________  ",
              "|          |       ",
              "|          |       ",
              "|          0       ",
              "|         \|/      ",
              "|         / \      ",
              "|                  "
              ]
    rlettere = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stange) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rlettere:
            cind = rlettere.index(char)
            board[cind] = char
            rlettere[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1

        print("\n".join(stange[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stange[0:wrong+1]))
        print("You lost")

hangman("acac")
