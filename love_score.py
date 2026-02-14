def calculate_love_score(name1,name2):
    add_name = name2 + name1
    lower_names = add_name.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    
    total1 = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    
    total2 = l + o + v + e
    
    love_score = int(str(total1) + str(total2))
    print("Love score: " + str(love_score))
print("Welcome to the Love Calculator!")
ASCII_art = '''
                    .----------------.  .----------------.  .----------------.  .----------------.
                    | .--------------. || .--------------. || .--------------. || .--------------. |
                    | |     _____    | || |     ____     | || |     ____     | || |     ____     | |
                    | |    |_   _|   | || |   .'    `.   | || |   .'    `.   | || |   .'    `.   | |
                    | |      | |     | || |  /  .--.  \  | || |  /  .--.  \  | || |  /  .--.  \  | |
                    | |      | |     | || |  | |    | |  | || |  | |    | |  | || |  | |    | |  | |
                    | |     _| |_    | || |  \  `--'  /  | || |  \  `--'  /  | || |  \  `--'  /  | |
                    | |    |_____|   | || |   `.____.'   | || |   `.____.'   | || |   `.____.'   | |
                    | |              | || |              | || |              | || |              | |
                    | |______________| || |______________| || |______________| || |______________| |
                    |__________________||__________________||__________________||__________________|
'''
calculate_love_score(name1="Kanye West", name2 = "KimKardashian")
