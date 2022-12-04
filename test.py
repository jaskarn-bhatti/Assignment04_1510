clown_stats = {"Current HP": 10, "Attack Damage": 2}
user = {"Current HP": 10, "Attack Damage": 5}


clown_dead = False
while not clown_dead:
    print(clown_stats["Current HP"])
    print("Moves punch: 1 kick: 2 run: 3 ")
    # move = int(input("Enter move: "))
    move = 1
    if clown_stats["Current HP"] <= 0:
        print("Clown had been killed")
        clown_dead = True
    elif move == 1:
        clown_stats["Current HP"] = clown_stats["Current HP"] - user["Attack Damage"]
