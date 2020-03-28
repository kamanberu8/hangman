def hangman(word):
    wrong=0
    stages=["",
            "______        ",
            "|             ",
            "|      |      ",
            "|      0      ",
            "|     /|\     ",
            "|      /\     ",
            ]

    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ")

    
xx
