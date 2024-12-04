with open('Day3Input.txt') as file:
    input = file.read()


result = 0
instruction = []

instruction_template = "mul(0,0)"




def can_add_numeric(character):
    0



def add_character_to_list(character):

    if character == "m":
        instruction.append(character)
    
    if character == "u" and instruction[0] == "m":
        instruction.append(character)

    if character == "l" and instruction[1] == "u":
        instruction.append(character)

    if character == "(" and instruction[2] == "l":
        instruction.append(character)      

    if character.isnumeric():
        if can_add_numeric:
            instruction.append(character) 

        








for character in input:
    result = add_character_to_list(character)
    
