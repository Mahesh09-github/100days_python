#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("Day24/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Day24/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        strippped_name = name.strip()
        new_letter = letter_contents.replace("[name]",strippped_name)
        with open(f"Day24/Output/ReadyToSend/letter_for_{strippped_name}.txt",mode="w") as letter:
            letter.write(new_letter)

