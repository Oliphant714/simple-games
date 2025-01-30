# Importing dictionaries
from choices import standard_phrases, wizard, fighter, rogue

# Universal variables
gate_keys = []
end_key = "story_end"
available_paths = ["wizard", "fighter", "rogue"]
keep_playing = "y"

#The storylines
def wiz_storyline(gate_keys, ending = "wizard"):
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
def fit_storyline(gate_keys, ending = "fighter"):
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
def rog_storyline(gate_keys, rogue_choices, ending = "rogue"):
    choice_count = 1
    choices = rogue
    print(choices["intro"])
    choice = input().strip()

    while choice_count < 3:
        rogue_choices.append(choice)
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

# Introducing the Crossroads


# The Game
while keep_playing.lower() == "y" and "traitor" not in gate_keys:

    display_paths = ", ".join(path.upper() for path in available_paths)
    
    path_choice = input(f"Please select the path you wish to walk: {display_paths}\n").lower()
    print("")
    
    if path_choice in available_paths:

        # Wizard Path
        if path_choice == "wizard":
            wiz_storyline(gate_keys)
            print("")
            if "traitor" in gate_keys:
                break
            elif "necromancer" not in gate_keys:
                ending_phrase = "wizard_end"
            else:
                ending_phrase = "necromancer_end"
                end_key = "special_end"
                available_paths.remove(path_choice)

        # Fighter Path
        elif path_choice == "fighter":
            fit_storyline(gate_keys)
            print("")
            if "traitor" in gate_keys:
                break
            elif "paladin" not in gate_keys:
                ending_phrase = "fighter_end"
            else:
                ending_phrase = "paladin_end"
                end_key = "special_end"
                available_paths.remove(path_choice)
        
        # Rogue Path
        elif path_choice == "rogue":
            rogue_choices = []
            rog_storyline(gate_keys, rogue_choices)
            print("")
            if "traitor" in gate_keys:
                break
            elif "castle" in rogue_choices:
                ending_phrase = "grogue_end"
            elif "castle" not in rogue_choices and "devil" not in gate_keys:
                ending_phrase = "brogue_end"
            else:
                ending_phrase = "devil_end"
                end_key = "special_end"
                available_paths.remove(path_choice)
            
        else:
            path_choice = input(standard_phrases["no_path"])

        print(standard_phrases[ending_phrase])
        if len(available_paths) > 0:
            keep_playing = input(standard_phrases[end_key])
        else:
            break
    else:
        print(standard_phrases["no_path"])

# End the game
