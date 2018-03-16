from classes.game import person, bcolors


magic =[{"name": "Fire", "cost": 10, "dmg": 90},
        {"name": "Thunder", "cost": 12, "dmg": 80},
        {"name": "Blizzard", "cost": 10, "dmg": 60},]


player = person(680, 65, 50, 85, magic)
enemy = person(1000, 65, 45, 35, magic)

running =True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)


while running:
    print("================================")
    player.choose_action()
    choice = input("Choose action ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for",dmg, "points of damamge:", enemy.get_hp())

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic:")) - 1
        magic_dmg = player.generate_spell_damamge(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP", "Player MP left", str(player.get_mp()) + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP", player.get_hp())

    print("=====================================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() <= 0:
        print(bcolors.OKGREEN + "You win tha battle!" + bcolors.ENDC)
        running = False

    elif player.get_hp() <= 0:
        print(bcolors.FAIL + "You have been defeated" + bcolors.ENDC)


    #player.get_max_hp()


#print("You chose", player.get_spell_name (int(choice)))print(player.generate_spell_damamge(0))
#print(player.generate_spell_damamge(1))

    #running = False
