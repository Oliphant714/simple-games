gate_keys = []

def wiz_storyline(ending = "wizard"):
    from choices import wizard
    choice_count = 1
    choices = wizard
    print(choices["intro"])
    choice = input().strip()

    while choice_count < 3:
        if choice.lower() == "bell" and choice_count == 2:
            print(choices["bell"])
            ending = "necromancer"
            choice_count += 1
        elif choice.lower() == "leave":
            ending = "traitor"
            break
        elif choice.lower() in choices  and choice.lower() != "bell":
            print(choices[choice.lower()])
            if choice_count < 2:
                choice = input().strip()
            choice_count += 1
        else:
            choice = input(choices["error"])
    gate_keys.append(ending)

def fit_storyline(ending = "fighter"):
    from choices import fighter
    choice_count = 1
    choices = fighter
    print(choices["intro"])
    choice = input().strip()

    while choice_count < 3:
        if choice.lower() == "pray" and choice_count == 2:
            print(choices["pray"])
            ending = "paladin"
            choice_count += 1
        elif choice.lower() == "leave":
            ending = "traitor"
            break
        elif choice.lower() in choices and choice.lower() != "pray":
            print(choices[choice.lower()])
            if choice_count < 2:
                choice = input().strip()
            choice_count += 1
        else:
            choice = input(choices["error"])
    gate_keys.append(ending)

def rog_storyline(ending = "rogue"):
    from choices import rogue
    choice_count = 1
    choices = rogue
    print(choices["intro"])
    choice = input().strip()

    while choice_count < 3:
        if choice.lower() == "pendant" and choice_count == 2:
            print(choices["pendant"])
            ending = "devil"
            choice_count += 1
        elif choice.lower() == "leave":
            ending = "traitor"
            break
        elif choice.lower() in choices and choice.lower() != "pendant":
            print(choices[choice.lower()])
            if choice_count < 2:
                choice = input().strip()
            choice_count += 1
        else:
            choice = input(choices["error"])
    gate_keys.append(ending)

