with open('Day4Input.txt') as file:
    lines = file.readlines()

    for index in range(len(lines)-1):
        lines[index] = lines[index].replace("\n", "")



text_to_find = "XMAS"
result = 0

def find_xmas(x, y):

    segment_len = (len(text_to_find) -1) *2
    segment_startpos = int(segment_len * -0.5)
    count = 0

    for direction in range(4):

        characters_to_test = ""

        match direction:

            case 0:
                for d in range(segment_startpos, abs(segment_startpos)+1):
                    characters_to_test += get_char(x + d, y)
            case 1:
                for d in range(segment_startpos, abs(segment_startpos)+1):
                    characters_to_test += get_char(x + d, y + d)
            case 2:
                for d in range(segment_startpos, abs(segment_startpos)+1):
                    characters_to_test += get_char(x, y + d)
            case 3:
                for d in range(segment_startpos, abs(segment_startpos)+1):
                    characters_to_test += get_char(x + d*-1, y + d)

        if "XMAS" in characters_to_test:
            count += 1
        if "SAMX" in characters_to_test:
            count += 1
        print(characters_to_test)
            
    
    return count


                
def get_char(x,y):

    if (0 <= x <= len(lines[0])-1) and (0 <= y <= len(lines)-1):
        return lines[y][x]
    else:
        return ""





for y, line in enumerate(lines):
    for x, character in enumerate(line):

        if character == "X":
            result +=find_xmas(x, y)
 
  
print(result)
