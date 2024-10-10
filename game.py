print("""Welcome to Rock, Paper, Sicssor
--------------------------------
  In the game you will type either 
  R, for rock 
  P, for paper 
  Sc, for scissor 
  Sp, for spock
  L, for lizard 
  Yes the capitilization is required,
  and each of the player's score will 
  be tracked and displayed upon Exit""")
print()
p1Counter = 0
p2Counter = 0
keepGoing = True
while keepGoing:
    p1 = input("player 1 > ")
    print("""...
    .
    ..
    ...
    ..
    .
    ..
    ...
    ..
    .
    ..
    ...
    ..
    .
    ..
    ...
    ..
    .
    ..
    ...
    ..
    .
    no peeking!
    """)
    p2 = input("player 2 > ")
    print()
    if p1 == "R" and p2 == "S" or p2 == "L":
        print("Player 1 takes this round!")
        p1Counter += 1
    elif p1 == "P" and p2 == "R" or p2 == "Sp":
        print("Player 1 takes this round!")
        p1Counter += 1
    elif p1 == "Sc" and p2 == "P" or p2 == "L":
        print("Player 1 takes this round!")
        p1Counter += 1
    elif p1 == "Sp" and p2 == "R" or p2 == "Sc":
        print("Player 1 takes this round!")
        p1Counter += 1
    elif p1 == "L" and p2 == "P" or p2 == "Sp":
        print("Player 1 takes this round!")
        p1Counter += 1
    elif p2 == "R" and p1 == "S" or p1 == "L":
        print("Player 2 takes this round!")
        p2Counter += 1
    elif p2 == "P" and p1 == "R" or p1 == "Sp":
        print("Player 2 takes this round!")
        p2Counter += 1
    elif p2 == "Sc" and p1 == "P" or p1 == "L":
        print("Player 2 takes this round!")
        p2Counter += 1
    elif p2 == "Sp" and p1 == "R" or p1 == "Sc":
        print("Player 2 takes this round!")
        p2Counter += 1
    elif p2 == "L" and p1 == "P" or p1 == "Sp":
        print("Player 2 takes this round!")
        p2Counter += 1
    else:
        print("It was a draw, go again!")
    print()
    exit = input("Exit? > ")
    if exit == "yes" or exit == "Yes":
        keepGoing = False
    else:
        print()
if p1Counter > p2Counter:
    print("Player 1 wins with", p1Counter, "wins under their belt!")
elif p1Counter == p2Counter:
    print("Hm, it seems like you both tied with", p1Counter, "wins, well I guess you both are winners!")
else:
    print("Player 2 wins with", p2Counter, "wins under their belt")