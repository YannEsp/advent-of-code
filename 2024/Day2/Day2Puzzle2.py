with open('Day2Input.txt') as f:
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

    for x in range(len(numbers)):
        tolerate_numbers = numbers.copy()
        del tolerate_numbers[x]

        if is_safe_increasing(tolerate_numbers) or is_safe_decreasing(tolerate_numbers):
            result += 1
            break




print(result)



            
        
