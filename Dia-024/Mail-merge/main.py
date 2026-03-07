#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../Mail-merge/Input/Letters/starting_letter.txt", "r") as file_letter:
    content = file_letter.read()
    with open("../Mail-merge/Input/Names/invited_names.txt", "r") as file_names:
        for name in file_names:
            clean_name = name.strip()
            final_letter = content.replace("[name]", clean_name)
            with open(f"../Mail-merge/Output/ReadyToSend/letter_for_{clean_name}.txt", "w") as output_file:
                output_file.write(final_letter)