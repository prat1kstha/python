#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names_path = "MailMerge/Input/Names/invited_names.txt"
starting_letter_path = "MailMerge/Input/Letters/starting_letter.txt"
output_path = "MailMerge/Output/ReadyToSend/"

with open(invited_names_path) as file_names:
    namelist = file_names.readlines()

with open(starting_letter_path) as letter:
    letter_template = letter.read()

for name in namelist:
    receiver = name.strip()

    with open(output_path + f"letter_for_{receiver}.txt", mode="w") as output_letter:
        output_letter.write(letter_template.replace("[name]", receiver))