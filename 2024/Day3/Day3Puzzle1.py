with open('Day3Input.txt') as file:
    input = file.read()


result = 0
instruction = ""


def can_add_numeric(character, instruction):

    if character.isnumeric():

        if "mul(" in instruction:
            return True
        
        return False



def add_character_to_list(character, instruction):

    if character == "m":
        return character
        
    
    if character == "u" and len(instruction) == 1:
        return character
        

    if character == "l" and len(instruction) == 2:
        return character
        

    if character == "(" and len(instruction) == 3:
        return character   
    

    if can_add_numeric(character, instruction):
        return character
    
    
    if character == "," and "mul(" in instruction and instruction[4].isnumeric():
        return character
    
    
    if character == ")" and "," in instruction and instruction[instruction.index(",")+1].isnumeric():
        return character





for index, character in enumerate(input):

    new_character = add_character_to_list(character, instruction)

    if new_character is not None:
        instruction += new_character
    else:
        print(0)
        instruction = ""

    
 
