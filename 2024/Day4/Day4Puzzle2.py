with open('Day4Input.txt') as file:
    lines = file.readlines()

    for index in range(len(lines)-1):
        lines[index] = lines[index].replace("\n", "")


result = 0


def is_square_xmas(square):

    diagonal_a = square[0][0] + square[1][1] + square[2][2],
    diagonal_b = square[0][2] + square[1][1] + square[2][0],
    
    return ("MAS" in diagonal_a or "SAM" in diagonal_a) and ("MAS" in diagonal_b or "SAM" in diagonal_b)



def find_xmas(x, y):

    square = []

    for y_index in range(3):

        x_line = []
        for x_index in range(3):
            x_line.append(get_char(x + x_index - 1, y + y_index - 1))
        
        square.append(x_line)

    return is_square_xmas(square)


                
def get_char(x,y):

    if (0 <= x <= len(lines[0])-1) and (0 <= y <= len(lines)-1):
        return lines[y][x]
    else:
        return " "



for y, line in enumerate(lines):
    for x, character in enumerate(line):

        if character == "A" and find_xmas(x, y):
            result += 1
 
  
print(result)
