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
            choice_count = 66
            ending = "traitor"
            break
        elif choice.lower() in choices:
            print(choices[choice.lower()])
            if choice_count < 2:
                choice = input().strip()
            choice_count += 1
        else:
            choice = input(choices["error"])
    gate_keys.append(ending)