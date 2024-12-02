with open('Day2Input1.txt') as f:
    lines = f.readlines()


def is_safe_increasing(numbers):
    previous_numb = None
    for numb in numbers:
        numb = int(numb)
        
        if previous_numb is not None:
            #is in range
            if 1 <= (previous_numb - numb) <= 3:
                previous_numb = numb
            else:
                return False
        else:
            previous_numb = numb
    return True


def is_safe_decreasing(numbers):
    previous_numb = None
    for numb in numbers:
        numb = int(numb)

        if previous_numb is not None:
            #is in range
            if -1 >= (previous_numb - numb) >= -3:
                previous_numb = numb
            else:
                return False
        else:
            previous_numb = numb
    return True



result = 0

for i, line in enumerate(lines):
    line = line.replace("\n","")

    numbers = line.split(" ")
    
    if is_safe_increasing(numbers) or is_safe_decreasing(numbers):
        result += 1
        

print(result)



            
        
