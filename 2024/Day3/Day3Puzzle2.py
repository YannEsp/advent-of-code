with open('Day3Input.txt') as file:
    input = file.read()


result = 0
instruction = ""
ended = False
can_add_instruction = True
do_instruction = ""
dont_instruction = ""

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
    

def find_do_instruction(character):
    
    if character == "d" and do_instruction == "":
        return character, True
    
    if character == "o" and len(do_instruction) == 1:
        return character, True

    if character == "(" and len(do_instruction) == 2:
        return character, True
    
    if character == ")" and len(do_instruction) == 3:
        return character, True

    return "", False



def find_dont_instruction(character):
    
    if character == "d" and dont_instruction == "":
        return character, True
    
    if character == "o" and len(dont_instruction) == 1:
        return character, True

    if character == "n" and len(dont_instruction) == 2:
        return character, True
    
    if character == "'" and len(dont_instruction) == 3:
        return character, True
    
    if character == "t" and len(dont_instruction) == 4:
        return character, True
    
    if character == "(" and len(dont_instruction) == 5:
        return character, True
    
    if character == ")" and len(dont_instruction) == 6:
        return character, True
    
    return "", False



#Main
for index, character in enumerate(input):


    if find_do_instruction(character)[1]:
        do_instruction += find_do_instruction(character)[0]
        
        if do_instruction ==  "do()":
            can_add_instruction = True
            do_instruction = ""
    else:
        do_instruction = ""


    if find_dont_instruction(character)[1]:
        dont_instruction += find_dont_instruction(character)[0]

        if dont_instruction == "don't()":
            can_add_instruction = False
            dont_instruction = ""
    else:
        dont_instruction = ""





    new_character = add_character_to_list(character, instruction)[0]
    ended = add_character_to_list(character, instruction)[1]

    #build instruction
    if new_character != "":
        instruction += new_character
        
        if ended:
            filtered_instruction = ""
            numbers = []

            for char in instruction:
                if char.isnumeric() or char == ",":
                    filtered_instruction += char
            
            numbers = filtered_instruction.split(",")

            if can_add_instruction:
                result += int(numbers[0]) * int(numbers[1])

            instruction = ""
            
    else:
        instruction = ""

print(result)
    
 