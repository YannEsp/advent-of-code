with open('Day3Input.txt') as file:
    input = file.read()


result = 0
instruction = ""
ended = False
can_add_instruction = False


def can_add_numeric(character, instruction):

    if character.isnumeric():

        if "mul(" in instruction:
            return True
        
        return False


def add_character_to_list(character, instruction):

    if character == "m":
        return character, False
        
    
    if character == "u" and len(instruction) == 1:
        return character, False
        

    if character == "l" and len(instruction) == 2:
        return character, False
        

    if character == "(" and len(instruction) == 3:
        return character, False
    

    if can_add_numeric(character, instruction):
        return character, False
    
    
    if character == "," and "mul(" in instruction and instruction[4].isnumeric():
        return character, False
    
    
    if character == ")" and "," in instruction and instruction[instruction.index(",")+1].isnumeric():
        return character, True
    
    return "", False
    


for index, character in enumerate(input):

    new_character = add_character_to_list(character, instruction)[0]
    ended = add_character_to_list(character, instruction)[1]


    if new_character != "":
        instruction += new_character
        
        if ended:
            filtered_instruction = ""
            numbers = []

            for char in instruction:
                if char.isnumeric() or char == ",":
                    filtered_instruction += char
            
            numbers = filtered_instruction.split(",")
            result += int(numbers[0]) * int(numbers[1])

            print(instruction)
            instruction = ""
            
    else:
        instruction = ""

print(result)
    
 
